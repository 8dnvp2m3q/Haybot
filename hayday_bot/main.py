import time

from .config import load_config
from .actions import run_farm_cycle
from .scheduler import random_delay


def main() -> None:
    config = load_config()
    while True:
        for _ in range(config.number_of_farms):
            run_farm_cycle(config)
        random_delay(config.wait_time_between_cycles_sec)


if __name__ == "__main__":
    main()
