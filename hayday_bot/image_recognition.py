from typing import List, Tuple
import cv2
import numpy as np


def match_template(image: np.ndarray, template_path: str, threshold: float = 0.8) -> List[Tuple[int, int]]:
    template = cv2.imread(template_path)
    if template is None:
        raise FileNotFoundError(f"Template not found: {template_path}")
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    return list(zip(loc[1], loc[0]))


def best_match(image: np.ndarray, template_path: str) -> Tuple[int, int]:
    template = cv2.imread(template_path)
    if template is None:
        raise FileNotFoundError(f"Template not found: {template_path}")
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_loc
