from sklearn.ensemble import RandomForestClassifier
from colorama import Fore

# Training dataset (synthetic)
X = [
    [10, 0, 0],
    [50, 1, 1],
    [12, 0, 0],
    [60, 1, 0],
    [70, 1, 1],
    [15, 0, 0]
]

y = [0, 1, 0, 1, 1, 0]  # 1 = malicious

model = RandomForestClassifier()
model.fit(X, y)

def extract_features(url):
    return [[len(url), int("@" in url), int("-" in url)]]

def check_url(url):
    features = extract_features(url)
    prediction = model.predict(features)

    if prediction[0] == 1:
        print(Fore.RED + "⚠️ Malicious URL Detected")
        result = "Malicious"
    else:
        print(Fore.GREEN + "✅ Safe URL")
        result = "Safe"

    # Save report
    with open("threat_report.txt", "w") as f:
        f.write(url + " -> " + result)


# Run
url = input("Enter URL: ")
check_url(url)