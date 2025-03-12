# Night Patrolling Robot

## Overview
The Automated Night Patrolling Robot is a Raspberry Pi 4B-powered autonomous system designed for surveillance and security patrolling at night. It features obstacle detection, real-time video streaming, and remote control via a web interface. The robot follows a predefined patrol path while avoiding obstacles and capturing footage.

## Features
✅ Autonomous Patrolling – Follows a predefined path <br/>
✅ Obstacle Avoidance – Uses ultrasonic sensors to detect and avoid obstacles <br/>
✅ Real-Time Video Streaming – Live camera feed via a web interface <br/>
✅ Remote Control – Web-based UI for manual control <br/>
✅ Motion Detection – Captures images when movement is detected <br/>
✅ Configurable Settings – JSON-based configuration for easy customization <br/>

## Hardware Requirements<br/>
1.Raspberry Pi 4B (or 3B+)<br/>
2.Motor Driver Module (L298N)<br/>
3.DC Motors with Wheels<br/>
4.Ultrasonic Sensor (HC-SR04)<br/>
5.Raspberry Pi Camera Module<br/>
6.12V Battery<br/>
7.Jumper Wires<br/>
8.Chassis for mounting components<br/>

## Software Requirements<br/>
1.Raspberry Pi OS (Bullseye)<br/>
2.Python 3<br/>
3.Flask (for web interface)<br/>
4.OpenCV (for image processing)<br/>
5.RPi.GPIO (for controlling hardware)<br/>

## Setup Instructions<br/>
1. Clone the Repository
```
git clone https://github.com/your-repo/night_patrolling_robot.git
cd night_patrolling_robot
```
<br/>
2. Configure GPIO & Settings<br/>
Modify config/gpio_pins.json and config/settings.json based on your hardware.
<br/>

4. Run the Web Interface<\br>
Start the Flask server for remote control and live streaming.
```
python3 web_interface/app.py
```
Access the web interface by opening:
```
http://<your_raspberry_pi_ip>:5000/
```
<br/>

5. Run the Autonomous Patrolling<br/>
To start automatic patrol mode:
```
python3 navigation/path_planning.py
```
<br/>

6. Enable Obstacle Avoidance
```  
python3 navigation/obstacle_avoidance.py
```
<br/>

## How It Works<br/>
1. Motion Detection<br/>
-- Uses the Raspberry Pi Camera Module to detect motion.<br/>
-- Captures images if movement is detected.<br/>
-- Stores images in the /data/images/ folder.<br/>
2. Path Planning<br/>
-- The robot moves along a predefined set of waypoints.<br/>
-- Configurable via navigation/path_planning.py.<br/>
3. Obstacle Avoidance<br/>
-- Uses the HC-SR04 Ultrasonic Sensor.<br/> 
-- If an obstacle is detected within 30cm, the robot stops and finds an alternate path.<br/>
4. Remote Monitoring<br/>
-- Flask Web Interface streams live video.<br/>
-- Control the robot using buttons (move forward, stop, etc.).<br/>
-- Accessible from any device connected to the same network.<br/>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
