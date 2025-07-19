from .device_interface import tap, swipe, get_screenshot
from .image_recognition import best_match
from .config import BotConfig


FIELD_TEMPLATE = "assets/field.png"
SHOP_TEMPLATE = "assets/shop.png"


def harvest_ready_fields(config: BotConfig) -> None:
    image = get_screenshot()
    try:
        x, y = best_match(image, FIELD_TEMPLATE)
        tap(x, y)
    except FileNotFoundError:
        pass


def plant_crop(config: BotConfig) -> None:
    # Placeholder coordinates for planting
    tap(100, 100)


def open_shop_and_sell(config: BotConfig) -> None:
    image = get_screenshot()
    try:
        x, y = best_match(image, SHOP_TEMPLATE)
        tap(x, y)
    except FileNotFoundError:
        pass


def run_farm_cycle(config: BotConfig) -> None:
    harvest_ready_fields(config)
    plant_crop(config)
    open_shop_and_sell(config)
