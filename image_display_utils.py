from PIL import Image


def display_image(image_file_path):
    """
    Display image which exists at argument file path.
    """
    image_pil = Image.open(image_file_path)
    image_pil.show()


if __name__ == "__main__":
    import constants
    import utils

    for image_file_path in utils.deep_iterdir(constants.THE_EIGHT_FACES_PATH):
        display_image(image_file_path)
