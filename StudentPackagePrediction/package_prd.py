import tkinter as tk
import joblib
import pandas as pd
import numpy as np

model = joblib.load("package_predictor.joblib")


def checking():
    cgpaa = ent.get()
    cgpa = float(cgpaa)
    # cgpa_arr = np.array([[cgpa]])
    cgpa_arr = np.array(cgpa).reshape(-1, 1)

    predicted_pkg = model.predict(cgpa_arr)

    indx_pkg = predicted_pkg[0]

    org_pkg = str(indx_pkg)[: 4]

    lblshow.config(text=f"Your package will be : {org_pkg} lakh.")


app = tk.Tk()
app.geometry("800x400")
app.title("Student package predictor")
app.config(background="#40f720")

lbl = tk.Label(app, text="Package Predictor", font=("robort", 40, "bold"), bg="darkgreen", fg="white")
lbl.pack(fill="x", pady=16, ipady=10)

ent = tk.Entry(app, font=("robort", 30))
ent.pack()

btn = tk.Button(app, text="Check package", font=("robort", 20, "bold"), bg="darkgreen", fg="white", command=checking)
btn.pack(pady=16)

lblshow = tk.Label(app, text="", font=("robort", 20), bg="#40f720", fg="black")
lblshow.pack()

app.mainloop()
