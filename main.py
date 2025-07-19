# 🧠 Build a modular Python bot to automate Hay Day gameplay using ADB and OpenCV
# ✅ Features:
# - Runs silently in background using ADB (no GUI/mouse)
# - Harvests ripe crops, replants specified crop, opens roadside shop, and sells harvested items
# - Rotates between multiple farms (optional)
# - Fully configurable using `config.json`

# 📂 Folder structure to generate:
# hayday_bot/
# ├── assets/                  # Template images (crop icons, fields, shop buttons, etc.)
# ├── config.json             # Bot behavior settings (crop type, price, farms)
# ├── config.py               # Load and validate config
# ├── device_interface.py     # ADB command wrappers: tap, swipe, screencap
# ├── image_recognition.py    # OpenCV template matching utilities
# ├── actions.py              # Main game logic: harvest, plant, sell
# ├── scheduler.py            # Optional random delay system
# └── main.py                 # Bot entrypoint

# ✅ Start by generating `config.json` with:
# {
#   "number_of_farms": 3,
#   "crop_to_plant": "wheat",
#   "sell_price_per_stack": 180,
#   "crop_stack_size": 10,
#   "wait_time_between_cycles_sec": 300
# }

# ✅ Next, generate `config.py`
# - load_config(path="config.json")
# - validate_config(config)

# ✅ Then, generate `device_interface.py`
# - tap(x, y)
# - swipe(x1, y1, x2, y2)
# - get_screenshot() -> returns OpenCV image
# - get_screen_resolution()

# ✅ Then, generate `image_recognition.py`
# - match_template(image, template_path) -> list of (x, y) matches
# - single best match using cv2.minMaxLoc

# ✅ Then, generate `actions.py`
# - run_farm_cycle(config)
#   - harvest_ready_fields(config)
#   - plant_crop(config)
#   - open_shop_and_sell(config)

# ✅ Then, generate `scheduler.py` (optional delays with jitter)

# ✅ Finally, generate `main.py`
# - load config
# - run loop across all farms
# - call `run_farm_cycle(config)` N times with optional sleep between

# ✅ Make sure:
# - All ADB commands are silent using subprocess
# - All paths use "assets/{filename}" format
# - All image matches assume 1280x720 resolution unless config says otherwise
# - Add error handling for missing template matches

# 🚀 Codex: Generate the complete implementation file by file, starting with config.py.
