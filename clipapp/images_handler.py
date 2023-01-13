
from tkinter import filedialog
import os


class ImagesHandler:
    def __init__(self):
        self.image_files = []
        self.current_image_index = -1

    def get_image_files(self, folder_path):
        image_files = []
        for file in os.listdir(folder_path):
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".gif") or file.endswith(".bmp"):
                image_files.append(os.path.join(folder_path, file))
        return image_files

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        print(f"Selected folder: {folder_path}")
        self.image_files = self.get_image_files(folder_path)
        self.current_image_index = 0
        return self.image_files

    def navigate_images(self, direction):
        if direction == "previous":
            self.current_image_index -= 1
        elif direction == "next":
            self.current_image_index += 1
        if self.current_image_index < 0:
            self.current_image_index = len(self.image_files) - 1
        elif self.current_image_index >= len(self.image_files):
            self.current_image_index = 0
        return self.image_files[self.current_image_index]

    @property
    def current_image(self):
        return self.image_files[self.current_image_index]