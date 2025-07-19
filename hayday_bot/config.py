import json
from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class BotConfig:
    number_of_farms: int
    crop_to_plant: str
    sell_price_per_stack: int
    crop_stack_size: int
    wait_time_between_cycles_sec: int


def load_config(path: str = "config.json") -> BotConfig:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    validate_config(data)
    return BotConfig(**data)


def validate_config(data: Dict[str, Any]) -> None:
    required_keys = {
        "number_of_farms": int,
        "crop_to_plant": str,
        "sell_price_per_stack": int,
        "crop_stack_size": int,
        "wait_time_between_cycles_sec": int,
    }
    for key, typ in required_keys.items():
        if key not in data:
            raise ValueError(f"Missing config key: {key}")
        if not isinstance(data[key], typ):
            raise ValueError(f"Invalid type for {key}: expected {typ.__name__}")

