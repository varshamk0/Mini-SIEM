# Mini-SIEM
A lightweight SIEM system that uses honeyfiles, Canarytokens, and real-time monitoring to detect unauthorized access attempts and generate security alerts.

# Mini SIEM - Honeyfile-Based Intrusion Detection System

## Overview

Mini SIEM is a lightweight Security Information and Event Management (SIEM) system developed to demonstrate real-time security monitoring, intrusion detection, and incident visibility using deception-based security techniques. The project utilizes strategically placed honeyfiles to identify unauthorized access attempts and generate security events for analysis.

The system continuously monitors honeyfiles located within user directories and records suspicious activities such as file modification and deletion. When an event is detected, detailed information including timestamps, user details, host information, and affected file paths is collected and forwarded to a centralized monitoring dashboard. The dashboard provides real-time visibility into security incidents through interactive visualizations, event statistics, and alert notifications.

This project showcases fundamental SIEM concepts such as event collection, centralized logging, security event correlation, alert generation, and incident monitoring while maintaining a lightweight and cost-effective architecture suitable for educational and research purposes.

---

## Features

* Real-time honeyfile monitoring using filesystem event detection
* Detection of unauthorized file modification and deletion attempts
* Centralized log collection and event storage
* Web-based monitoring dashboard built using Flask
* Real-time security event visualization
* Event statistics and incident tracking
* Search and filtering capabilities
* Severity-based event classification
* Telegram-based security alerts
* Lightweight architecture suitable for educational environments

---

## System Architecture

```text
Honeyfiles
     │
     ▼
Filesystem Monitoring Engine
     │
     ▼
Event Collection Module
     │
     ▼
Centralized Log Storage
     │
     ▼
Flask Dashboard
     │
     ├── Real-Time Alerts
     ├── Event Statistics
     ├── Event Timeline
     └── Security Event Logs
```

---

## Technologies Used

### Backend

* Python
* Flask
* Flask-CORS

### Monitoring

* Watchdog
* Psutil

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

### Alerting

* Telegram Bot API

### Logging & Storage

* JSON Log Storage
* Python Logging Module

---

## Dashboard Features

The dashboard provides:

* Total security event count
* Modified file statistics
* Deleted file statistics
* High-risk alert indicators
* Real-time event timeline visualization
* Searchable event logs
* Live security alert notifications
* Severity-based event categorization

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/mini-siem.git
cd mini-siem
```

### Install Dependencies

```bash
pip install flask flask-cors watchdog psutil requests
```

### Start Dashboard Server

```bash
python flask2.py
```

### Start Monitoring Service

```bash
python hfsiem.py
```

### Open Dashboard

```text
http://localhost:5000
```

---

## Project Structure

```text
mini-siem/
│
├── flask2.py
├── hfsiem.py
├── templates/
│   └── index.html
│
├── screenshots/
│   └── dashboard.png
│
└── README.md
```

---

## Sample Workflow

1. Honeyfiles are generated within monitored directories.
2. The monitoring engine continuously observes file activity.
3. An attacker or user modifies/deletes a honeyfile.
4. The event is captured and logged.
5. The SIEM server receives the security event.
6. The dashboard updates in real time.
7. Security alerts are generated and displayed.
8. Telegram notifications are sent to the administrator.

---

## Applications

* Security Monitoring
* Intrusion Detection
* Deception-Based Security Research
* Cybersecurity Education
* Security Awareness Demonstrations
* SIEM Concept Demonstrations

---

## Future Enhancements

* Threat Intelligence Integration
* MITRE ATT&CK Mapping
* Geolocation-Based Attack Visualization
* User Authentication and Role-Based Access
* Database-Based Log Storage
* Machine Learning-Based Anomaly Detection
* Multi-Host Event Aggregation
* Automated Incident Response

---

## Author

**Varsha M Kumar**
B.Tech Computer Science Engineering (Honours in Cybersecurity)
Christ (Deemed to be University), Bengaluru

---

## License

This project is intended for educational and research purposes.
