"""Hay Day Automation Bot

Setup Instructions:
1. Install Python 3.8+ and pip
2. Install dependencies: pip install opencv-python numpy pillow
3. Enable USB Debugging on your Android device
4. Connect your phone and ensure adb works: adb devices
5. Create a folder named "screenshots/" and add cropped template PNGs:
   - wheat_icon.png, crop_ready.png, empty_field.png, shop_button.png, empty_slot.png, coin_icon.png
6. Edit config.py to customize the behavior
7. Run the bot: python main.py
"""

import time
import config
import bot_functions as bot


def run_bot_loop() -> None:
    while True:
        for farm_index in range(config.number_of_farms):
            print(f"\nRunning farm {farm_index + 1}/{config.number_of_farms}")
            bot.run_farm_cycle()
            if farm_index < config.number_of_farms - 1:
                bot.rotate_farm()
        print(f"Waiting {config.wait_time_between_cycles_sec} seconds before next cycle")
        time.sleep(config.wait_time_between_cycles_sec)


if __name__ == "__main__":
    run_bot_loop()
