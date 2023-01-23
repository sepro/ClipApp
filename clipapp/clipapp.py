import tkinter as tk
import os
from tkinter import PhotoImage
from .images_handler import ImagesHandler
from .text_handler import TextHandler


def image_to_text_path(image_path: str) -> str:
    """
    Given an image path, return the corresponding text file path by replacing the extension with '.txt'
    :param image_path: The file path of the image
    :return: The file path of the text file with the same name
    """
    path, ext = os.path.splitext(image_path)
    return path + ".txt"


class ClipApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x900")
        self.image_handler = ImagesHandler()
        self.text_handler = None

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
        self.text_box = tk.Entry(middle_frame)
        self.text_box.grid(row=1, column=0, padx=50)

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
        self.save_text()
        print("OK button pressed")

    def cancel_button_handler(self):
        self.cancel_text()
        print("Cancel button pressed")

    def open_folder_handler(self):
        self.image_handler.select_folder()
        self.update_image(self.image_handler.current_image)

    def update_image(self, image_path: str):
        """
        Update the image displayed in the app with a new image
        :param image_path: the path of the image file to be displayed
        """
        new_image = PhotoImage(file=image_path)
        self.image_label.configure(image=new_image)
        self.image_label.image = new_image

        text_path = image_to_text_path(image_path)
        self.text_handler = TextHandler(text_path)
        self.text_box.delete(0, tk.END)
        self.text_box.insert(0, self.text_handler.original_text)

    def save_text(self):
        """
        Save the text in the text box to the corresponding text file
        """
        new_text = self.text_box.get()
        self.text_handler.save_text(new_text)

    def cancel_text(self):
        """
        Cancel any changes made to the text and set it back to the original text
        """
        self.text_box.delete(0, tk.END)
        self.text_box.insert(0, self.text_handler.original_text)