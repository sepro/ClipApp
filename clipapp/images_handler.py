
from tkinter import filedialog
import os


class ImagesHandler:
    """
    Handles the images in the application.
    Allows the user to select a folder containing images, navigate through the images and get the current image
    """
    def __init__(self):
        self.image_files = []
        self.current_image_index = -1

    def get_image_files(self, folder_path):
        """
        Get all the image files in a folder
        :param folder_path: the path of the folder containing the images
        :return: a list of file paths of the images in the folder
        """
        image_files = []
        for file in os.listdir(folder_path):
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".gif") or file.endswith(".bmp"):
                image_files.append(os.path.join(folder_path, file))
        return image_files

    def select_folder(self):
        """
        Opens a file dialog for the user to select a folder containing images
        :return: a list of file paths of the images in the selected folder
        """
        folder_path = filedialog.askdirectory()
        print(f"Selected folder: {folder_path}")
        self.image_files = self.get_image_files(folder_path)
        self.current_image_index = 0
        return self.image_files

    def navigate_images(self, direction):
        """
        Navigate through the images
        :param direction: "previous" or "next" to navigate to the previous or next image
        :return: the file path of the current image
        """
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
        """
        :return: the file path of the current image
        """
        return self.image_files[self.current_image_index]