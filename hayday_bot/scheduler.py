import random
import time


def random_delay(base_seconds: int) -> None:
    jitter = random.uniform(-0.1, 0.1) * base_seconds
    time.sleep(max(0, base_seconds + jitter))
