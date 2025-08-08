import tkinter as tk
from tkinter import ttk
import random
import math

# Multipliers for moods
MOOD_MULTIPLIER = {
    "Calm": 0.6,
    "Irked": 1.0,
    "Angry": 1.6,
    "Legendary": 3.2
}

# Funny explanations
FLAVOUR_TEXTS = [
    "Calculated with grandma-level precision.",
    "Consulted three neighbours and a dog.",
    "Applied the ancient Chappal Theorem.",
    "Excluded physics for dramatic effect.",
    "Adjusted for dramatic lighting.",
    "Fact-checked by local gossip auntie."
]

class ChappalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🩴 Chappal Distance Calculator (Cool Edition)")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e2f")

        # Title
        tk.Label(root, text="🩴 Chappal Distance Calculator", font=("Arial", 20, "bold"),
                 bg="#1e1e2f", fg="white").pack(pady=10)

        # Frame for inputs
        input_frame = tk.Frame(root, bg="#1e1e2f")
        input_frame.pack(pady=5)

        # Mood
        tk.Label(input_frame, text="Mother's Mood:", bg="#1e1e2f", fg="white").grid(row=0, column=0, sticky="w")
        self.mood_var = tk.StringVar(value="Irked")
        ttk.Combobox(input_frame, textvariable=self.mood_var, values=list(MOOD_MULTIPLIER.keys()),
                     state="readonly", width=15).grid(row=0, column=1, padx=5)

        # Strength
        tk.Label(input_frame, text="Throw Strength:", bg="#1e1e2f", fg="white").grid(row=1, column=0, sticky="w")
        self.strength_var = tk.IntVar(value=6)
        ttk.Scale(input_frame, variable=self.strength_var, from_=0, to=10, orient="horizontal").grid(row=1, column=1, padx=5)

        # Wind Level
        tk.Label(input_frame, text="Wind Level:", bg="#1e1e2f", fg="white").grid(row=2, column=0, sticky="w")
        self.wind_var = tk.IntVar(value=1)
        ttk.Scale(input_frame, variable=self.wind_var, from_=0, to=10, orient="horizontal").grid(row=2, column=1, padx=5)

        # Number of Past Offenses
        tk.Label(input_frame, text="Number of Past Offenses:", bg="#1e1e2f", fg="white").grid(row=3, column=0, sticky="w")
        self.offenses_var = tk.IntVar(value=3)
        ttk.Spinbox(input_frame, textvariable=self.offenses_var, from_=0, to=50, width=5).grid(row=3, column=1, padx=5)

        # Throw Button
        ttk.Button(input_frame, text="Throw Chappal!", command=self.throw_chappal).grid(row=4, column=0, pady=10)
        ttk.Button(input_frame, text="Reset", command=self.reset).grid(row=4, column=1, pady=10)

        # Result Box
        self.result_box = tk.Label(root, text="Awaiting the sacred launch...", bg="#1e1e2f", fg="white")
        self.result_box.pack(pady=10)

        # Log
        self.log_box = tk.Text(root, height=10, bg="#1e1e2f", fg="white")
        self.log_box.pack(pady=10)

    def throw_chappal(self):
        mood = self.mood_var.get()
        strength = self.strength_var.get()
        wind = self.wind_var.get()
        offenses = self.offenses_var.get()

        # Calculate distance (fake formula)
        distance = strength * MOOD_MULTIPLIER[mood] * (1 + math.log(offenses + 1)) + random.uniform(-wind, wind)

        # Update result box
        self.result_box.config(text=f"Chappal thrown! Distance: {distance:.2f} meters")

        # Log the action
        self.log_box.insert(tk.END, f"Throwing chappal with strength {strength}, wind {wind}, offenses {offenses}...\n")
        self.log_box.see(tk.END)

    def reset(self):
        self.mood_var.set("Irked")
        self.strength_var.set(6)
        self.wind_var.set(1)
        self.offenses_var.set(3)
        self.result_box.config(text="Awaiting the sacred launch...")
        self.log_box.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChappalApp(root)
    root.mainloop()