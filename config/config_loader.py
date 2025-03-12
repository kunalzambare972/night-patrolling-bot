import json

def load_config(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Load settings
settings = load_config("config/settings.json")
gpio_pins = load_config("config/gpio_pins.json")

# Example usage
patrol_speed = settings["patrol_speed"]
print(f"Patrol Speed: {patrol_speed}")

left_motor_in1 = gpio_pins["motors"]["left_motor_in1"]
print(f"Left Motor IN1 is on GPIO {left_motor_in1}")
