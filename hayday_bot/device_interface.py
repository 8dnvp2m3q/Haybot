import subprocess
from typing import Tuple
import cv2
import numpy as np


def _adb_command(*args: str) -> subprocess.CompletedProcess:
    cmd = ["adb", *args]
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


def tap(x: int, y: int) -> None:
    _adb_command("shell", "input", "tap", str(x), str(y))


def swipe(x1: int, y1: int, x2: int, y2: int, duration_ms: int = 500) -> None:
    _adb_command(
        "shell",
        "input",
        "swipe",
        str(x1),
        str(y1),
        str(x2),
        str(y2),
        str(duration_ms),
    )


def get_screenshot() -> np.ndarray:
    result = _adb_command("exec-out", "screencap", "-p")
    img_array = np.frombuffer(result.stdout, dtype=np.uint8)
    return cv2.imdecode(img_array, cv2.IMREAD_COLOR)


def get_screen_resolution() -> Tuple[int, int]:
    result = _adb_command("shell", "wm", "size")
    output = result.stdout.decode()
    # Expect output like: "Physical size: 1080x1920"
    for token in output.split():
        if "x" in token and token.replace("x", "").isdigit():
            width, height = token.strip().split("x")
            return int(width), int(height)
    return 1280, 720
