# Temperature Control System with Web Visualization

A Raspberry Pi-based temperature monitoring system that reads real-time temperature data from a **DS18B20 digital temperature sensor** and displays it through a **Flask-powered web interface**. The application hosts the temperature readings on a local web server, allowing any device on the same network to monitor the current temperature.

## Overview

This project demonstrates how to interface a DS18B20 temperature sensor with a Raspberry Pi using the 1-Wire communication protocol and visualize the sensor data on a web page.

The system:
- Reads temperature data from the DS18B20 sensor
- Processes the data using Python
- Serves the temperature through a Flask web application
- Displays the live temperature on a browser over the local network

## Features

- Real-time temperature monitoring
- Web-based visualization using Flask
- Accessible from any device on the same local network
- Uses Raspberry Pi's built-in 1-Wire interface
- Implemented entirely in Python

## Hardware Requirements

- Raspberry Pi 5
- DS18B20 Digital Temperature Sensor
- Jumper wires
- Power supply

## Software Requirements

- Python 3
- Flask
- Raspberry Pi OS
- 1-Wire interface enabled

## Project Structure

```
.
├── temp.py                 # Reads sensor data and runs Flask server
├── templates/
│   └── web.html            # Web interface
└── README.md
```

## Hardware Connection

| DS18B20 Pin | Raspberry Pi |
|-------------|--------------|
| VCC (Red)   | 3.3V |
| GND (Black) | Ground |
| DATA (Yellow) | GPIO4 (1-Wire) |

> **Note:** The DS18B20 data line requires a pull-up resistor (typically 4.7 kΩ). GPIO4 supports the standard 1-Wire configuration used by Raspberry Pi.

## Running the Project

1. Enable the Raspberry Pi 1-Wire interface.
2. Connect the DS18B20 sensor.
3. Install the required dependencies:

```bash
pip install flask
```

4. Run the application:

```bash
python3 temp.py
```

5. Open a browser and navigate to:

```
http://<RaspberryPi-IP>:5000
```

The current temperature will be displayed on the webpage.

## Technologies Used

- Python
- Flask
- HTML
- Raspberry Pi 5
- DS18B20 Temperature Sensor
- 1-Wire Communication Protocol

## Results

The application successfully:
- Reads live temperature values from the DS18B20 sensor.
- Hosts a Flask web server on port **5000**.
- Displays real-time temperature updates on any device connected to the same local network.

## Future Improvements

- Automatic page refresh using AJAX
- Historical temperature logging
- Temperature graphs and analytics
- Email/SMS alerts for threshold temperatures
- Remote access via cloud deployment
- Mobile-responsive dashboard

## Author

**Kirthika Gopalan**

Automation & Control
