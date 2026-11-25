import json
import os

# Default configuration
default = {
    "application": "Student Management",
    "version": "1.0",
    "settings": {
        "theme": "light",
        "language": "English",
        "notifications": True
    }
}

# Create config.json if it does not exist
if not os.path.exists("config.json"):
    with open("config.json", "w") as file:
        json.dump(default, file, indent=4)

# Load configuration
with open("config.json", "r") as file:
    config = json.load(file)

# Read nested settings
print("Application:", config["application"])
print("Theme:", config["settings"]["theme"])
print("Language:", config["settings"]["language"])

# Modify a setting
config["settings"]["theme"] = "dark"

# Save updated configuration
with open("config.json", "w") as file:
    json.dump(config, file, indent=4)

print("Configuration updated!")