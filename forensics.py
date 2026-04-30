from sklearn.ensemble import IsolationForest
import numpy as np
from colorama import Fore, Style, init
init()

def analyze_logs(filename):
    print(Fore.CYAN + "="*55)
    print("     AI CYBERSECURITY ANALYSIS PLATFORM")
    print("="*55 + Style.RESET_ALL)

    try:
        with open(filename, "r") as f:
            logs = f.readlines()
    except:
        print(Fore.RED + "Error reading file")
        return

    values = [int(x.strip()) for x in logs]
    data = np.array(values).reshape(-1, 1)

    model = IsolationForest(contamination=0.2)
    model.fit(data)

    predictions = model.predict(data)

    anomalies = [values[i] for i in range(len(values)) if predictions[i] == -1]

    print("\n===== ANALYSIS REPORT =====")
    print("Module: Digital Forensics\n")

    if anomalies:
        print(Fore.RED + "⚠️ Anomalies Detected:", anomalies)
    else:
        print(Fore.GREEN + "✅ No anomalies detected")

    print("===========================\n")

    with open("forensics_report.txt", "w") as f:
        f.write("Anomalies: " + str(anomalies))


file = input("Enter log file name (e.g., logs.txt): ")
analyze_logs(file)