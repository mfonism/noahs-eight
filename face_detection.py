import face_recognition


def get_face_locations(image_file_path):
    """
    Return the locations of the faces in the image at argument file path.
    """
    image = face_recognition.load_image_file(image_file_path)
    face_locations = face_recognition.face_locations(image)
    return face_locations


if __name__ == "__main__":
    from PIL import Image, ImageDraw

    import constants
    import utils

    for image_file_path in utils.deep_iterdir(constants.SKINNIES_PATH):
        face_locations = get_face_locations(image_file_path)

        if not face_locations:
            continue

        image_pil = Image.open(image_file_path)
        draw = ImageDraw.Draw(image_pil)

        for (top, right, bottom, left) in face_locations:
            draw.rectangle((left, top, right, bottom), outline="#FF1493")

        del draw  # to conserve resources
        image_pil.show()
