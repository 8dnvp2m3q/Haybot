# Haybot

This project provides a simple Hay Day automation bot that interacts with an Android device using ADB and OpenCV.

## Setup
Follow these steps to run the bot:
1. Install Python 3.8+ and pip.
2. Install dependencies:
   ```bash
   pip install opencv-python numpy pillow
   ```
3. Enable USB debugging on your Android device.
4. Connect your phone and verify adb works with `adb devices`.
5. Create a `screenshots/` folder and add cropped template PNGs:
   - `wheat_icon.png`
   - `crop_ready.png`
   - `empty_field.png`
   - `shop_button.png`
   - `empty_slot.png`
   - `coin_icon.png`
6. Edit `config.py` to adjust the settings.
7. Run the bot:
   ```bash
   python main.py
   ```
