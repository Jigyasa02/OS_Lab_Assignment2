# OS Lab Assignment 2 – System Startup, Process Creation, and Termination Simulation

## 📌 Overview
This project simulates basic operating system behavior during system startup, process creation, execution, and termination using **Python 3**, the **multiprocessing** module, and the **logging** module.  
It demonstrates how processes are spawned, executed concurrently, and properly terminated while maintaining system-like logs.

---

## 🚀 Features
- Simulates **system startup and shutdown**
- Creates **two parallel processes** using `multiprocessing`
- Logs process lifecycle events with **timestamps** and **process names**
- Generates a log file `process_log.txt` as execution proof

---

## 📂 Files Included
- `system_simulation.py` → Main Python script  
- `process_log.txt` → Generated log file showing process start and end times  
- `report.pdf` → Short report explaining the implementation  
- *(Optional)* `README.md` → Documentation of the project  

---

## ⚙️ Requirements
- Python 3.x  
- Linux environment (tested on Kali Linux)  

Install Python and pip if not already installed:
```bash
sudo apt update && sudo apt install python3 python3-pip -y
