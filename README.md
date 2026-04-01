# drone_monitoring
# Autonomous Drone for Air Pollution Monitoring

A modular drone system for real-time air pollution monitoring using embedded sensors, GPS tracking, and telemetry communication.

---

## 📌 Overview

This project enables a drone to:
- Measure air quality (PM2.5, optional gases like CO2)
- Track geographic location using GPS
- Log pollution data over time
- Transmit or store environmental data for analysis

The system is designed with a **modular, production-grade architecture** suitable for research and scalable deployments.

---

## 🧠 System Architecture

- **Flight Controller**: STM32-based (e.g., ArduPilot-compatible hardware)
- **Autopilot Firmware**: ArduPilot  
- **Companion System**: Optional (Raspberry Pi or embedded Linux device)
- **Sensors**:
  - PM2.5 sensor (PMS5003 or similar)
  - GPS module (u-blox M8N recommended)
- **Communication**:
  - MAVLink telemetry
  - Optional MQTT / cloud streaming

---

## 📁 Project Structure
