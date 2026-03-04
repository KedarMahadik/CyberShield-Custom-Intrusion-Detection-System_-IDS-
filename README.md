Terminal 1: The Engine
.\ids_env\Scripts\activate
python cybershield_engine.py
(Starts the Scapy sniffer.)

Terminal 2: The Dashboard
.\ids_env\Scripts\activate
streamlit run ids_dashboard.py
(Launches the Pandas-powered visual monitor.)

Terminal 3: The Attack Simulation
Now, you can simply run:
nmap -F 127.0.0.1

What will happen?

Engine (T1): Will detect multiple unique ports being hit and log a PORT_SCAN event.

Dashboard (T2): Will show a sudden spike in the "Warning" bar chart and a new entry in the data table.

Firewall: Your block_ip function will trigger a netsh command to block your own IP.


"I integrated Nmap into my development workflow to perform rigorous Regression Testing on the IDS engine. By automating port-scan simulations, I verified that the Scapy-based detection logic correctly identifies reconnaissance patterns and triggers the appropriate state-level firewall remediation. Adding Nmap to the environment variables was a key step in ensuring the system could be tested across different terminal environments seamlessly."
