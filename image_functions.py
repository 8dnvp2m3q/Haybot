import cv2
import numpy as np


def load_template(path: str) -> np.ndarray:
    template = cv2.imread(path)
    if template is None:
        raise FileNotFoundError(f"Template not found: {path}")
    return template


def find_all(screen: np.ndarray, template_path: str, threshold: float = 0.9):
    template = load_template(template_path)
    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    return list(zip(loc[1], loc[0]))


def best_match(screen: np.ndarray, template_path: str):
    template = load_template(template_path)
    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    _min_val, _max_val, _min_loc, max_loc = cv2.minMaxLoc(res)
    return max_loc
