import tkinter as tk
import time
import psutil
root = tk.Tk()

# Quitar bordes
root.overrideredirect(True)

# Siempre encima
root.attributes("-topmost", True)

# Transparencia opcional
root.attributes("-alpha", 0.6)

# Posición (x, y)
root.geometry("135x25+1400+50")

label = tk.Label(root, font=("Arial", 12), bg="black", fg="white")
label.pack(fill="both", expand=True)


def update_info():
    battery = psutil.sensors_battery()
    percent = battery.percent

    current_time = time.strftime("%H:%M:%S")
    label.config(text=f"{current_time} | 🔋 {percent}%")

    root.after(1000, update_info)


update_info()
root.mainloop()

