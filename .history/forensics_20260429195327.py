from sklearn.ensemble import IsolationForest
import numpy as np
from colorama import Fore

def analyze_logs(filename):
    try:
        with open(filename, "r") as f:
            logs = f.readlines()
    except:
        print(Fore.RED + "Error reading file")
        return

    # Convert logs to numeric values (simple simulation)
    values = [int(x.strip()) for x in logs]

    data = np.array(values).reshape(-1, 1)

    model = IsolationForest(contamination=0.2)
    model.fit(data)

    predictions = model.predict(data)

    anomalies = [values[i] for i in range(len(values)) if predictions[i] == -1]

    if anomalies:
        print(Fore.RED + "⚠️ Anomalies Detected:", anomalies)
    else:
        print(Fore.GREEN + "✅ No anomalies detected")

    # Save report
    with open("forensics_report.txt", "w") as f:
        f.write("Anomalies: " + str(anomalies))


# Run
file = input("Enter log file name (numbers only): ")
analyze_logs(file)