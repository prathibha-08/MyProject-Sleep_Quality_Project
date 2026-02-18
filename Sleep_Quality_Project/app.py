import tkinter as tk
from tkinter import messagebox
import joblib

# Load encoders (still useful if needed later)
le_caffeine = joblib.load("le_caffeine.pkl")
le_interruptions = joblib.load("le_interruptions.pkl")

# Prediction Function
def predict():
    try:
        sleep = float(entry_sleep.get())
        exercise = float(entry_exercise.get())
        screen = float(entry_screen.get())
        stress = float(entry_stress.get())
        caffeine_value = caffeine_var.get()
        interruptions_value = interrupt_var.get()

        # Convert interruptions to numeric
        interruptions = 1 if interruptions_value == "Yes" else 0

        # Count bad habits
        bad_count = 0

        if sleep < 6:
            bad_count += 1

        if exercise < 15:
            bad_count += 1

        if screen > 120:
            bad_count += 1

        if stress > 7:
            bad_count += 1

        if interruptions == 1:
            bad_count += 1

        # Classification
        if bad_count == 0:
            result = "Good"
        elif bad_count <= 2:
            result = "Average"
        else:
            result = "Poor"

        # Suggestions
        tips = ""

        if sleep < 6:
            tips += "• Try to sleep at least 6–8 hours.\n"
        if exercise < 15:
            tips += "• Increase daily exercise.\n"
        if screen > 120:
            tips += "• Reduce screen time before bed.\n"
        if stress > 7:
            tips += "• Practice meditation to reduce stress.\n"
        if interruptions == 1:
            tips += "• Improve sleep environment to avoid interruptions.\n"

        if tips == "":
            tips = "Great job! Your sleep habits look healthy. Keep it up!"

        label_result.config(
            text=f"Predicted Sleep Quality: {result}\n\nSuggestions:\n{tips}"
        )

    except:
        messagebox.showerror("Error", "Please enter valid numeric values.")


# Reset Function
def reset():
    entry_sleep.delete(0, tk.END)
    entry_exercise.delete(0, tk.END)
    entry_screen.delete(0, tk.END)
    entry_stress.delete(0, tk.END)
    caffeine_var.set("Low")
    interrupt_var.set("No")
    label_result.config(text="")


# GUI Window
root = tk.Tk()
root.title("Sleep Quality Predictor")
root.geometry("400x520")

tk.Label(root, text="Sleep Duration (hours)").pack()
entry_sleep = tk.Entry(root)
entry_sleep.pack()

tk.Label(root, text="Exercise Duration (minutes)").pack()
entry_exercise = tk.Entry(root)
entry_exercise.pack()

tk.Label(root, text="Screen Time Before Bed (minutes)").pack()
entry_screen = tk.Entry(root)
entry_screen.pack()

tk.Label(root, text="Stress Level (0-10)").pack()
entry_stress = tk.Entry(root)
entry_stress.pack()

tk.Label(root, text="Caffeine Intake").pack()
caffeine_var = tk.StringVar()
caffeine_var.set("Low")
tk.OptionMenu(root, caffeine_var, "None", "Low", "Moderate", "High").pack()

tk.Label(root, text="Sleep Interruptions").pack()
interrupt_var = tk.StringVar()
interrupt_var.set("No")
tk.OptionMenu(root, interrupt_var, "Yes", "No").pack()

tk.Button(root, text="Predict Sleep Quality", command=predict).pack(pady=10)
tk.Button(root, text="Reset", command=reset).pack()

label_result = tk.Label(root, text="", wraplength=350)
label_result.pack(pady=15)

root.mainloop()
