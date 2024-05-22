import tkinter as tk
from PIL import ImageTk, Image
import random
import time

class MyProgram:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Program")

        # Create a label for entering your name
        self.name_label = tk.Label(self.root, text="Enter your name:")
        self.name_label.pack()
        self.entry_field = tk.Entry(self.root)
        self.entry_field.pack()

        # Create a button to process the data
        self.process_button = tk.Button(self.root, text="Process", command=self.process_data)
        self.process_button.pack()

        # Create a label to display the results
        self.result_label = tk.Label(self.root, text="Results:")
        self.result_label.pack()
        self.text_box = tk.Text(self.root)
        self.text_box.pack()

    def process_data(self):
        name = self.entry_field.get()
        if not name:
            messagebox.showerror("Error", "Please enter your name!")
            return

        # Process the data here...
        results = ["Result 1", "Result 2", ...]
        for result in results:
            self.text_box.insert(tk.END, result + "\n")

    def run(self):
        self.root.mainloop()

class Tamagotchi:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tamagotchi")

        # Create a canvas for the animation
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        # Initialize the Tamagotchi's age and hunger levels
        self.age = 0
        self.hunger = 10

        # Create an image of the Tamagotchi (replace with your own image file)
        self.tamagotchi_image = ImageTk.PhotoImage(Image.open("Python/tamagotchi.png"))
        self.tamagotchi = self.canvas.create_image(200, 200, image=self.tamagotchi_image)

        # Create a label for the hunger level
        self.hunger_label = tk.Label(self.root, text="Hunger: 10")
        self.hunger_label.pack()

        # Create buttons for feeding and playing with Tamagotchi
        self.feed_button = tk.Button(self.root, text="Feed", command=self.feed)
        self.feed_button.pack()
        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.play_button.pack()

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
            self.hunger_label.config(text=f"Hunger: {self.hunger}")
        else:
            print("Tamagotchi is too hungry!")

    def play(self):
        if self.age < 10:
            self.age += 1
            self.hunger -= 1
            self.hunger_label.config(text=f"Hunger: {self.hunger}")
            self.canvas.delete(self.tamagot)
