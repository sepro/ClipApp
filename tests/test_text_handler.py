from clipapp.text_handler import TextHandler


def test_init(tmpdir):
    text_path = tmpdir.join('test_text.txt')
    text_handler = TextHandler(text_path)
    assert text_handler.text_path == text_path
    assert text_handler.original_text == ""


def test_load_text(tmpdir):
    text_path = tmpdir.join('test_text.txt')
    text_path.write("test text")
    text_handler = TextHandler(text_path)
    text_handler.load_text()
    assert text_handler.original_text == "test text"


def test_save_text(tmpdir):
    text_path = tmpdir.join('test_text.txt')
    text_handler = TextHandler(text_path)
    text_handler.save_text("new text")
    assert text_path.read() == "new text"
    assert text_handler.original_text == "new text"