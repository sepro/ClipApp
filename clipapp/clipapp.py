import tkinter as tk
from tkinter import PhotoImage
from .images_handler import ImagesHandler


class ClipApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x900")
        self.image_handler = ImagesHandler()

        self.create_layout()
        self.create_menu()

    def create_layout(self):
        # Creating Frame
        middle_frame = tk.Frame(self.root)
        middle_frame.pack(pady=50)

        # Creating Image
        image = PhotoImage(file="./img/empty_file.png")
        self.image_label = tk.Label(middle_frame, image=image)
        self.image_label.grid(row=0, column=1, padx=50)

        # Creating navigate button
        previous_button = tk.Button(middle_frame, text="Previous", command=self.previous_button_handler)
        previous_button.grid(row=0, column=0)

        next_button = tk.Button(middle_frame, text="Next", command=self.next_button_handler)
        next_button.grid(row=0, column=2)

        # Creating Text Box
        text_box = tk.Entry(middle_frame)
        text_box.grid(row=1, column=0, padx=50)

        # Creating Ok button
        ok_button = tk.Button(middle_frame, text="OK", command=self.ok_button_handler)
        ok_button.grid(row=1, column=1)

        # Creating Cancel button
        cancel_button = tk.Button(middle_frame, text="Cancel", command=self.cancel_button_handler)
        cancel_button.grid(row=1, column=2)

    def create_menu(self):
        # Creating main menu
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Creating File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_folder_handler)
        file_menu.add_command(label="Exit", command=self.root.destroy)

    def previous_button_handler(self):
        previous_image = self.image_handler.navigate_images("previous")
        self.update_image(previous_image)
        print("previous button pressed")

    def next_button_handler(self):
        next_image = self.image_handler.navigate_images("next")
        self.update_image(next_image)
        print("next button pressed")

    def ok_button_handler(self):
        print("OK button pressed")

    def cancel_button_handler(self):
        print("Cancel button pressed")

    def open_folder_handler(self):
        self.image_handler.select_folder()
        self.update_image(self.image_handler.current_image)

    def update_image(self, image_path):
        new_image = PhotoImage(file=image_path)
        self.image_label.configure(image=new_image)
        self.image_label.image = new_image
