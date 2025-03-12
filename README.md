# Automated Night Patrolling Robot 🚔🤖

## Overview
The Automated Night Patrolling Robot is a Raspberry Pi 4B-powered autonomous system designed for surveillance and security patrolling at night. It features obstacle detection, real-time video streaming, and remote control via a web interface. The robot follows a predefined patrol path while avoiding obstacles and capturing footage.

## Features
✅ Autonomous Patrolling – Follows a predefined path
✅ Obstacle Avoidance – Uses ultrasonic sensors to detect and avoid obstacles
✅ Real-Time Video Streaming – Live camera feed via a web interface
✅ Remote Control – Web-based UI for manual control
✅ Motion Detection – Captures images when movement is detected
✅ Configurable Settings – JSON-based configuration for easy customization

## Hardware Requirements
1.Raspberry Pi 4B (or 3B+)
2.Motor Driver Module (L298N)
3.DC Motors with Wheels
4.Ultrasonic Sensor (HC-SR04)
5.Raspberry Pi Camera Module
6.12V Battery
7.Jumper Wires
8.Chassis for mounting components

## Software Requirements
1.Raspberry Pi OS (Bullseye)
2.Python 3
3.Flask (for web interface)
4.OpenCV (for image processing)
5.RPi.GPIO (for controlling hardware)

##Setup Instructions
1. Clone the Repository
```
git clone https://github.com/your-repo/night_patrolling_robot.git
cd night_patrolling_robot
```

2. Configure GPIO & Settings
Modify config/gpio_pins.json and config/settings.json based on your hardware.

3. Run the Web Interface
Start the Flask server for remote control and live streaming.
```
python3 web_interface/app.py
```
Access the web interface by opening:
```
http://<your_raspberry_pi_ip>:5000/
```
4. Run the Autonomous Patrolling
To start automatic patrol mode:
```
python3 navigation/path_planning.py
```
5. Enable Obstacle Avoidance
```  
python3 navigation/obstacle_avoidance.py
```
##How It Works
1. Motion Detection
Uses the Raspberry Pi Camera Module to detect motion.
Captures images if movement is detected.
Stores images in the /data/images/ folder.
2. Path Planning
The robot moves along a predefined set of waypoints.
Configurable via navigation/path_planning.py.
3. Obstacle Avoidance
Uses the HC-SR04 Ultrasonic Sensor.
If an obstacle is detected within 30cm, the robot stops and finds an alternate path.
4. Remote Monitoring
Flask Web Interface streams live video.
Control the robot using buttons (move forward, stop, etc.).
Accessible from any device connected to the same network.
