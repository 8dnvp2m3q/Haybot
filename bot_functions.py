import time
from typing import Tuple

import config
import buttons_data as btn
from adb_controller import tap, swipe, screenshot
from image_functions import best_match, find_all


def harvest_ready_fields() -> None:
    img = screenshot()
    fields = find_all(img, btn.CROP_READY)
    if not fields:
        print("No ready crops found")
        return
    print(f"Harvesting {len(fields)} fields")
    for x, y in fields:
        tap(x + 5, y + 5)
        time.sleep(0.1)


def plant_crop() -> None:
    img = screenshot()
    empty = find_all(img, btn.EMPTY_FIELD)
    if not empty:
        print("No empty fields found")
        return
    try:
        bx, by = best_match(img, btn.WHEAT_ICON)
    except FileNotFoundError:
        print("Crop icon not found")
        return
    print(f"Planting on {len(empty)} fields")
    for x, y in empty:
        tap(x + 5, y + 5)
        time.sleep(0.1)
        tap(bx + 5, by + 5)
        time.sleep(0.1)


def open_shop_and_sell() -> None:
    img = screenshot()
    try:
        sx, sy = best_match(img, btn.SHOP_BUTTON)
    except FileNotFoundError:
        print("Shop button not found")
        return
    tap(sx + 5, sy + 5)
    time.sleep(1)
    img = screenshot()
    slots = find_all(img, btn.EMPTY_SLOT)
    if not slots:
        print("No empty slots to sell")
        return
    print(f"Selling {len(slots)} stacks")
    for x, y in slots:
        tap(x + 5, y + 5)
        time.sleep(0.2)
        tap(sx + 120, sy)  # approximate ok button
        time.sleep(0.2)


def rotate_farm() -> None:
    # swipe left to right to switch farms
    swipe(1200, 360, 100, 360, duration_ms=500)
    time.sleep(1)


def run_farm_cycle() -> None:
    harvest_ready_fields()
    plant_crop()
    open_shop_and_sell()
