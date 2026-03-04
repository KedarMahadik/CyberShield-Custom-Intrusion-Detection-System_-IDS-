

## 🛠️ Phase 1: Installation & Best Setup

To ensure the project runs smoothly on Windows, we will isolate the dependencies and configure the environment variables.

### **1. System Requirements**

* **Python 3.8+** installed.
* **Nmap** installed and added to the System **Path** (Environment Variables).
* **Administrative Privileges** (required to modify firewall rules via `netsh`).

### **2. Virtual Environment Setup**

Open your VS Code terminal and run:

```powershell
# Create the environment
python -m venv ids_env

# Activate the environment
.\ids_env\Scripts\activate

# Install all dependencies
pip install scapy pandas streamlit matplotlib numpy

```

---

## 🚀 Phase 2: Execution & Operations

This project utilizes a **Multi-Terminal Architecture** to separate the detection engine from the visualization dashboard.

### **Terminal 1: The Detection Engine**

This is the "Back-end" that performs **Deep Packet Inspection (DPI)**.

```powershell
.\ids_env\Scripts\activate
python cybershield_engine.py

```

* **Function:** Sniffs raw traffic, detects anomalies (DDoS, Port Scans, SQLi), and triggers firewall blocks.

### **Terminal 2: The Security Dashboard**

This is the "Front-end" powered by **Pandas** and **Streamlit**.

```powershell
.\ids_env\Scripts\activate
streamlit run ids_dashboard.py

```

* **Function:** Reads `ids_security_events.log` and generates real-time traffic analysis charts.

---

## 🧪 Phase 3: Simulating Attacks (The Test Plan)

To see results, you must generate "malicious" traffic in a **Third Terminal**.

| Attack Type | Command to Run | What it Triggers |
| --- | --- | --- |
| **Port Scan** | `nmap -F 127.0.0.1` | **Layer 4 Detection:** Identifies reconnaissance and blocks the source IP. |
| **DDoS Simulation** | `python -c "from scapy.all import send, IP, ICMP; send(IP(dst='127.0.0.1')/ICMP()/'X'*100, count=110)"` | **Rate Limiting:** Detects 100+ identical packet sizes and triggers a Critical Block. |
| **Large Packet** | `ping 127.0.0.1 -l 2000` | **Anomaly Detection:** Flags packets exceeding the MTU limit (1500 bytes). |
| **Web Attack** | `curl "http://localhost/?id=1' UNION SELECT NULL--"` | **Layer 7 DPI:** Detects SQL Injection keywords in raw payloads. |

---

## 📊 Phase 4: Interpreting Results

After running the tests, you will see the following results:

### **1. Security Logs (`ids_security_events.log`)**

The log file provides the "Proof of Work" for your IDS logic.

* **Example Entry:** `2026-03-04 | WARNING | PORT_SCAN | Source: 127.0.0.1 | Unique Ports: 24`.

### **2. Visual Dashboard (Streamlit)**

* **Metric Cards:** Display real-time counts of intercepted threats.
* **Bar Charts:** Show the frequency of different attack levels (Warning vs. Critical).
* **Incident Table:** A Pandas-filtered view of the most recent 10 threats.

### **3. Active Firewall Verification**

To see the automated remediation in action, run:

```powershell
netsh advfirewall firewall show rule name=all | findstr CyberShield

```

* **Result:** You will see active "BLOCK" rules created dynamically by your Python script.

---



> ### 🛡️ CyberShield Adaptive-IDS
> 
> 
> **Automated Intrusion Detection & Response System**
> #### **Key Features**
> 
> 
> * **Stateful Packet Inspection:** Utilizes Scapy for real-time stream analysis across OSI Layers 3, 4, and 7.
> * **Automated Remediation:** Programmatic integration with Windows/Linux firewalls for Zero-Hour IP blocking.
> * **Statistical Intelligence:** A Pandas-driven pipeline for identifying "Low and Slow" exfiltration patterns.
> * **Security Visualization:** Real-time dashboards built with Streamlit and Matplotlib for SOC visibility.
> 
> 
> #### **How It Works**
> 
> 
> 1. The **Engine** captures raw packets and evaluates them against behavioral heuristics.
> 2. Detections are logged into a structured security event file.
> 3. The **Dashboard** ingests logs via Pandas for real-time visualization.
> 4. Malicious actors are automatically neutralized at the firewall level.
> 
> 

---

**Would you like me to generate a "Sample Presentation Script" for your interview?** It will give you the exact words to say while demonstrating the Dashboard and the Firewall blocks.
