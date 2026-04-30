import tkinter as tk
from sklearn.ensemble import RandomForestClassifier

# Train model
X = [[10,0,0],[50,1,1],[12,0,0],[60,1,0]]
y = [0,1,0,1]

model = RandomForestClassifier()
model.fit(X, y)

def check_url():
    url = entry.get()
    features = [[len(url), int("@" in url), int("-" in url)]]
    prediction = model.predict(features)

    if prediction[0] == 1:
        result_label.config(text="⚠️ Malicious URL", fg="red")
    else:
        result_label.config(text="✅ Safe URL", fg="green")

root = tk.Tk()
root.title("Threat Intelligence System")
root.geometry("400x200")

tk.Label(root, text="Enter URL", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack()

tk.Button(root, text="Check URL", command=check_url).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()