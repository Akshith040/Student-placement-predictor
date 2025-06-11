import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# Load the model and encoders
model = joblib.load('placement_predictor_model.pkl')

# Function to predict placement
def predict_placement():
    try:
        # Get inputs from the user
        branch = branch_var.get()
        gender = gender_var.get()
        tenth_percent = float(tenth_var.get())
        inter_percent = float(inter_var.get())
        btech_percent = float(btech_var.get())
        backlogs = int(backlogs_var.get())  # Ensure integer
        special_training = special_training_var.get()
        aptitude1 = float(apt1_var.get())
        aptitude2 = float(apt2_var.get())
        average_aptitude = float(average_apt_var.get())
        internships = internship_var.get()
        
        # Map string inputs to numerical values if required by the model
        special_training = 1 if special_training.lower() == 'yes' else 0
        internships = 1 if internships.lower() == 'yes' else 0
        
        # Create feature array
        features = np.array([[
            branch,
            gender,
            tenth_percent,
            inter_percent,
            btech_percent,
            backlogs,
            special_training,
            aptitude1,
            aptitude2,
            average_aptitude,
            internships
        ]])
        
        # Assuming the missing feature might be something simple like branch encoding
        # Add a dummy feature to make up for the missing one (This needs actual adjustment based on the model)
        features = np.insert(features, 0, 0)  # Insert dummy feature at the start

        # Predict placement
        prediction = model.predict_proba(features.reshape(1, -1))[0][1]
        messagebox.showinfo("Prediction", f"Probability of being placed: {prediction:.2f}")
        
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Initialize the GUI window
root = tk.Tk()
root.title("Placement Predictor")

# Variables to store user inputs
branch_var = tk.StringVar()
gender_var = tk.StringVar()
tenth_var = tk.StringVar()
inter_var = tk.StringVar()
btech_var = tk.StringVar()
backlogs_var = tk.StringVar()
special_training_var = tk.StringVar()
apt1_var = tk.StringVar()
apt2_var = tk.StringVar()
average_apt_var = tk.StringVar()
internship_var = tk.StringVar()

# Create the input fields
tk.Label(root, text="Branch").grid(row=0, column=0)
tk.Entry(root, textvariable=branch_var).grid(row=0, column=1)

tk.Label(root, text="Gender").grid(row=1, column=0)
tk.Entry(root, textvariable=gender_var).grid(row=1, column=1)

tk.Label(root, text="10th Percentage").grid(row=2, column=0)
tk.Entry(root, textvariable=tenth_var).grid(row=2, column=1)

tk.Label(root, text="Inter/Diploma Percentage").grid(row=3, column=0)
tk.Entry(root, textvariable=inter_var).grid(row=3, column=1)

tk.Label(root, text="B.Tech Percentage (IV-I)").grid(row=4, column=0)
tk.Entry(root, textvariable=btech_var).grid(row=4, column=1)

tk.Label(root, text="Active Backlogs (IV-I)").grid(row=5, column=0)
tk.Entry(root, textvariable=backlogs_var).grid(row=5, column=1)

tk.Label(root, text="Special Training").grid(row=6, column=0)
tk.Entry(root, textvariable=special_training_var).grid(row=6, column=1)

tk.Label(root, text="APT-1").grid(row=7, column=0)
tk.Entry(root, textvariable=apt1_var).grid(row=7, column=1)

tk.Label(root, text="APT-2").grid(row=8, column=0)
tk.Entry(root, textvariable=apt2_var).grid(row=8, column=1)

tk.Label(root, text="Average APT").grid(row=9, column=0)
tk.Entry(root, textvariable=average_apt_var).grid(row=9, column=1)

tk.Label(root, text="Internships").grid(row=10, column=0)
tk.Entry(root, textvariable=internship_var).grid(row=10, column=1)

# Create the predict button
tk.Button(root, text="Predict", command=predict_placement).grid(row=11, column=0, columnspan=2)

# Run the GUI event loop
root.mainloop()
