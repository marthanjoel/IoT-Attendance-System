# Project Title: IoT Attendance System Simulator

## Objective
This project simulates an IoT Attendance System that logs attendance when an RFID card is scanned.  
It uses a Python Tkinter GUI to mimic card scanning, attendance logging, and banned card alerts without requiring hardware.

> Example: Tracks attendance for students or employees using simulated RFID scans with a GUI interface.

---

## Tools & Technologies
- **Programming Language**: Python 3.x
- **Frameworks**: Tkinter
- **Simulator**: Custom GUI
- **Dependencies**: Listed in `requirements.txt`

---

## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/marthanjoel/IoT-Attendance-System.git
cd IoT-Attendance-System
2. Create Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the Project
bash
Copy code
python3 main.py
Simulation Details
Sensor Emulated: RFID card scanner (simulated)

Actuator Emulated: GUI listbox displaying logs, alert labels for banned users

Trigger Logic: Clicking "Scan Card" randomly selects a card; banned cards trigger red alerts while allowed cards log attendance with timestamp.



---
Screenshots
Screenshot 1: <img width="739" height="733" alt="Screenshot from 2025-09-18 04-23-28" src="https://github.com/user-attachments/assets/4280b215-526e-466d-bf4e-1ef478205b17" />


Screenshot 2:<img width="739" height="733" alt="Screenshot from 2025-09-18 04-25-55" src="https://github.com/user-attachments/assets/5853446a-c566-40ed-93e0-ffc1e7e7130d" />
 

Screenshot 3: <img width="739" height="733" alt="Screenshot from 2025-09-18 04-25-18" src="https://github.com/user-attachments/assets/4ff86ac8-8323-4ad8-bdad-ec39f79b1af0" />
---

Observations
Worked well: GUI loads correctly, attendance logs appear in real-time.

Bugs/Challenges: Random card selection may repeat users; can be extended to prevent duplicates.

Validation: Simulation verified by scanning multiple cards and checking logs and alert behavior.

--
Future Improvements
Export attendance logs to CSV

Integrate LED/buzzer simulation in GUI

Add multiple banned card detection

Integrate cloud logging or Google Sheets connectivity
