import tkinter as tk
from sklearn.ensemble import RandomForestClassifier

# ML model
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

# GUI
root = tk.Tk()
root.title("Threat Intelligence System")

tk.Label(root, text="Enter URL").pack()
entry = tk.Entry(root, width=40)
entry.pack()

tk.Button(root, text="Check", command=check_url).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()