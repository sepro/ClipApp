import pytest
from clipapp.images_handler import ImagesHandler


@pytest.fixture
def images_handler():
    return ImagesHandler()


@pytest.fixture
def test_folder():
    return 'tests/test_images'


def test_get_image_files(images_handler, test_folder):
    image_files = images_handler.get_image_files(test_folder)
    assert len(image_files) == 2
    assert all([f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')) for f in image_files])


def test_navigate_images(images_handler, test_folder):
    images_handler.image_files = images_handler.get_image_files(test_folder)
    images_handler.current_image_index = 0

    assert images_handler.navigate_images('next') == images_handler.image_files[1]
    assert images_handler.navigate_images('previous') == images_handler.image_files[0]
    images_handler.current_image_index = len(images_handler.image_files) - 1
    assert images_handler.navigate_images('next') == images_handler.image_files[0]
    images_handler.current_image_index = 0
    assert images_handler.navigate_images('previous') == images_handler.image_files[-1]


def test_current_image(images_handler, test_folder):
    images_handler.image_files = images_handler.get_image_files(test_folder)
    images_handler.current_image_index = 0
    assert images_handler.current_image == images_handler.image_files[0]
    images_handler.current_image_index = 1
    assert images_handler.current_image == images_handler.image_files[1]