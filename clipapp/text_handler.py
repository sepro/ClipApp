import os


class TextHandler:
    def __init__(self, text_path:str):
        """
        Initialize a TextHandler instance with a text file path
        :param text_path: the path to the text file
        """
        self.text_path = text_path
        self.original_text: str = ""
        self.load_text()

    def load_text(self) -> None:
        """
        Load the text from the file, if the file doesn't exist, it will create an empty one.
        """
        if os.path.exists(self.text_path):
            with open(self.text_path, "r") as f:
                self.original_text = f.read()
        else:
            with open(self.text_path, "w") as f:
                pass

    def save_text(self, new_text: str) -> None:
        """
        Save a new text to the file
        :param new_text: the text to be written to the file
        """
        self.original_text = new_text
        with open(self.text_path, "w") as f:
            f.write(new_text)
