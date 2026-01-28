import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# Load trained model
model = joblib.load("package_predictor.joblib")

#Predict function
def predict_package():
    try:
        cgpa=float(ent.get())
        prediction=model.predict(np.array([[cgpa]]))
        result_label.config(text=f"Predicted Package: {prediction[0]: .2f} LPA")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid input")


#Create main window
app=tk.Tk()
app.geometry("400x200")
app.title("Student Package Predictor")

#UI Elements

#Application Label
lbl=tk.Label(app, text="Package Prediction System", font=("Ariel", 16, "bold"))
lbl.pack(pady=10)

#Creating Box to enter CGPA
ent=tk.Entry(app, text="Enter CGPA", font=("Ariel", 14))
ent.pack(pady=5)

#Creating Button to predict the package
btn=tk.Button(app, text="Predict Package", font=("Ariel", 12), command=predict_package)
btn.pack(pady=10)

#Creating Message Box after predicted the package
result_label=tk.Label(app, text="", font=("Ariel", 12), fg="green")
result_label.pack(pady=10)


app.mainloop()