#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import subprocess
from waterTank import waterTanks_control

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Make the window full screen
        self.title("Tkinter with External Matplotlib Plot")
        self.state('zoomed')  

        # Configure layout
        self.left_frame = tk.Frame(self, width=300, bg="lightgray")
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.right_frame = tk.Frame(self, bg="white")
        self.right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Label
        self.label = tk.Label(self.left_frame, text="Click to load external plot", font=("Arial", 12), bg="lightgray")
        self.label.pack(pady=10, padx=10)

        # Button to show the plot
        self.plot_button = tk.Button(self.left_frame, text="Show Plot", command=self.display_plot)
        self.plot_button.pack(pady=10, padx=10)

        # Placeholder for Matplotlib figure
        self.canvas = None  

    def display_plot(self):
        """Loads and displays the Matplotlib figure inside the frame."""
        if self.canvas:
            self.canvas.get_tk_widget().destroy()  # Remove previous plot

        fig = waterTanks_control()  # Call the function from plot.py

        # Embed the figure into the Tkinter Frame
        self.canvas = FigureCanvasTkAgg(fig, master=self.right_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas.draw()

# Run the Tkinter application
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
