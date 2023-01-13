import tkinter as tk
from tkinter import PhotoImage
from tkinter import filedialog
import os

image_files = []


def get_image_files(folder_path):
    image_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".gif") or file.endswith(".bmp"):
            image_files.append(os.path.join(folder_path, file))
    return image_files


def select_folder():
    folder_path = filedialog.askdirectory()
    print(f"Selected folder: {folder_path}")
    global image_files
    image_files = get_image_files(folder_path)
    print(image_files)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("1000x900")

    # Creating Frame
    middle_frame = tk.Frame(root)
    middle_frame.pack(pady=50)

    # Creating Image
    image = PhotoImage(file="./img/empty_file.png")
    image_label = tk.Label(middle_frame, image=image)
    image_label.grid(row=0, column=1, padx=50)

    # Creating navigate button
    previous_button = tk.Button(middle_frame, text="Previous", command=lambda: print("previous button pressed"))
    previous_button.grid(row=0, column=0)

    next_button = tk.Button(middle_frame, text="Next", command=lambda: print("next button pressed"))
    next_button.grid(row=0, column=2)

    # Creating Text Box
    text_box = tk.Entry(middle_frame)
    text_box.grid(row=1, column=0, padx=50)

    # Creating Ok button
    ok_button = tk.Button(middle_frame, text="OK", command=lambda: print("OK button pressed"))
    ok_button.grid(row=1, column=1)

    # Creating Cancel button
    cancel_button = tk.Button(middle_frame, text="Cancel", command=lambda: print("Cancel button pressed"))
    cancel_button.grid(row=1, column=2)

    # Creating main menu
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    # Creating File menu
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=lambda: select_folder())
    file_menu.add_command(label="Exit", command=root.destroy)

    root.mainloop()


