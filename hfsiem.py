import os
import random
import string
import time
import requests
import psutil
import getpass
import socket
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuration
USER_DIRS = [
    os.path.join(os.environ['USERPROFILE'], d)
    for d in ['Desktop', 'Documents', 'Downloads']
]
FILE_EXTENSIONS = ['.docx', '.xlsx', '.pdf', '.txt']
HONEYFILE_NAMES = [
    "Financial_Records", "Business_Plans", "Customer_Data",
    "User_Credentials", "Passwords_Backup", "Confidential_Report"
]
HONEYFILE_COUNT = 3
SIEM_LOG_ENDPOINT = "http://localhost:5000/siem-log"

# Setup logging
LOG_DIR = os.path.join(os.environ['USERPROFILE'], 'HoneyfileLogs')
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, 'monitor.log')),
        logging.StreamHandler()
    ]
)

honeyfile_paths = []

def generate_filename():
    name = random.choice(HONEYFILE_NAMES)
    ext = random.choice(FILE_EXTENSIONS)
    rand = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return f"sensitive_{name}_{rand}{ext}"

def create_honeyfiles():
    for folder in USER_DIRS:
        if not os.path.exists(folder):
            continue
        for _ in range(HONEYFILE_COUNT):
            filename = generate_filename()
            path = os.path.join(folder, filename)
            try:
                with open(path, 'w') as f:
                    f.write("CONFIDENTIAL — DO NOT OPEN\n")
                os.chmod(path, 0o444)  # Read-only
                honeyfile_paths.append(path)
                logging.info(f"Honeyfile created: {path}")
            except Exception as e:
                logging.error(f"Failed to create {path}: {str(e)}")

def send_log(event_type, filepath):
    data = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "user": getpass.getuser(),
        "host": socket.gethostname(),
        "event_type": event_type,
        "file": filepath,
    }
    
    for attempt in range(3):  # Retry up to 3 times
        try:
            resp = requests.post(SIEM_LOG_ENDPOINT, json=data, timeout=5)
            if resp.status_code == 200:
                logging.info(f"Alert sent for {filepath}")
                return
            else:
                logging.warning(f"Unexpected response: {resp.status_code}")
        except Exception as e:
            logging.warning(f"Attempt {attempt+1} failed: {str(e)}")
            time.sleep(2)
    
    # Fallback to local log if SIEM is unreachable
    with open(os.path.join(LOG_DIR, 'local_alerts.log'), 'a') as f:
        f.write(f"{data}\n")

def kill_intruder(filepath):
    for proc in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            for f in proc.info['open_files'] or []:
                if f.path.lower() == filepath.lower():
                    proc.kill()
                    logging.warning(f"Suspicious process killed: {proc.info['name']}")
                    return
        except Exception:
            continue

class MonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.src_path in honeyfile_paths:
            logging.warning(f"Honeyfile modified: {event.src_path}")
            send_log("MODIFIED", event.src_path)
            kill_intruder(event.src_path)

    def on_deleted(self, event):
        if not event.is_directory and event.src_path in honeyfile_paths:
            logging.warning(f"Honeyfile deleted: {event.src_path}")
            send_log("DELETED", event.src_path)
            kill_intruder(event.src_path)

def start_monitoring():
    observer = Observer()
    handler = MonitorHandler()
    for folder in USER_DIRS:
        observer.schedule(handler, folder, recursive=False)
    observer.start()
    logging.info(f"Monitoring started on {len(USER_DIRS)} directories")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    logging.info(f"Starting honeyfile monitor. Logs stored in: {LOG_DIR}")
    create_honeyfiles()
    start_monitoring()