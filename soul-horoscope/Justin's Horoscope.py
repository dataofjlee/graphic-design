import tkinter as tk
from tkinter import ttk
import time
import threading

def calculate():
    if not entries[0].get():
        result_label.config(text="Please fill out the 'Birth Sign' field. ❗")
        return
    result_label.config(text="Calculating... ⏳")
    progress_bar["maximum"] = 100

    for i in range(101):
        time.sleep(0.05)
        progress_bar["value"] = i
        root.update_idletasks()

    result_label.config(text="Done! According to our advanced AI techniques, \nyour soulmate has the following attributes: 🌟")
    soulmate_info.config(state="normal")
    soulmate_info.delete(1.0, tk.END)
    soulmate_info.insert(tk.END, "Hair: same as yours\nHobby: Composes Classical Music\nEthnicity: White, if possible\nTrue passion: Bouldering\nMain Skill: Programming\nSide talent: Climbing\nPersonality Type: protective\nBuild: Bodyguard\nJob: Olypmic Climber\nSide Hustle: Optiver\n\nProbability: 93.7%")
    soulmate_info.config(state="disabled")

root = tk.Tk()
root.title("Justin's Horoscope")
root.geometry('400x500')
root.resizable(0, 0)

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

labels = ["Birth Sign:", "Day of Birth:", "Favorite Color:", "Ideal Holiday Destination:", "Food Last Eaten:", "Favorite Book:", "Name of First Crush:"]
combobox_values = [["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"],
                   None, 
                   ["Red", "Blue", "Green", "Yellow", "Black", "White"],
                   None,
                   None,
                   None,
                   None]

entries = []

for i, label in enumerate(labels):
    ttk.Label(frame, text=label).grid(row=i, column=0, sticky=tk.W)
    if combobox_values[i]:
        entry = ttk.Combobox(frame, values=combobox_values[i])
    else:
        entry = ttk.Entry(frame)
    entry.grid(row=i, column=1)
    entries.append(entry)

submit_button = ttk.Button(frame, text="Submit", command=lambda: threading.Thread(target=calculate).start())
submit_button.grid(row=len(labels), columnspan=2)

result_label = ttk.Label(frame, text="")
result_label.grid(row=len(labels)+1, columnspan=2)

progress_bar = ttk.Progressbar(frame, orient="horizontal", mode="determinate")
progress_bar.grid(row=len(labels)+2, columnspan=2, sticky=(tk.W, tk.E))

soulmate_info = tk.Text(frame, wrap=tk.WORD, width=40, height=12, state="disabled")
soulmate_info.grid(row=len(labels)+3, columnspan=2)

root.mainloop()
