from sklearn.ensemble import RandomForestClassifier
from colorama import Fore, Style, init
init()

# Training data
X = [
    [10, 0, 0],
    [50, 1, 1],
    [12, 0, 0],
    [60, 1, 0],
    [70, 1, 1],
    [15, 0, 0]
]
y = [0, 1, 0, 1, 1, 0]

model = RandomForestClassifier()
model.fit(X, y)

def extract_features(url):
    return [[len(url), int("@" in url), int("-" in url)]]

def check_url(url):
    print(Fore.CYAN + "="*55)
    print("     AI CYBERSECURITY ANALYSIS PLATFORM")
    print("="*55 + Style.RESET_ALL)

    features = extract_features(url)
    prediction = model.predict(features)

    print("\n===== ANALYSIS REPORT =====")
    print("Module: Threat Intelligence")
    print("Input URL:", url)

    if prediction[0] == 1:
        result = "Malicious"
        print(Fore.RED + "Result: ⚠️ Malicious URL")
    else:
        result = "Safe"
        print(Fore.GREEN + "Result: ✅ Safe URL")

    print("===========================\n")

    with open("threat_report.txt", "w") as f:
        f.write(url + " -> " + result)


url = input("Enter URL: ")
check_url(url)