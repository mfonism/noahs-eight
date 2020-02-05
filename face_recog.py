import face_recognition
from PIL import Image, ImageDraw

import face_detection


def get_face_encodings(image_file_path, known_face_locations=None):
    """
    Return an array of encodings which make up the respective signatures of the
    faces in the image at argument file path.
    """
    image = face_recognition.load_image_file(image_file_path)
    face_encodings = face_recognition.face_encodings(
        image, known_face_locations=known_face_locations
    )
    return face_encodings


def get_known_face_encodings_dict():
    """
    Return a dictionary of encodings for the faces known to us.

    The keys are the names of the face owners, while the values are the
    respective encodings.
    """
    return dict(
        (image_file_path.stem, get_face_encodings(image_file_path)[0])
        for image_file_path in utils.deep_iterdir(constants.THE_EIGHT_FACES_PATH)
    )


def recognize_faces(image_file_path):
    """
    Recognize any faces known to us in image at argument file path.
    """
    image_pil = Image.open(image_file_path)
    draw = ImageDraw.Draw(image_pil)

    known_face_encodings_dict = get_known_face_encodings_dict()
    known_names = list(known_face_encodings_dict.keys())
    known_face_encodings = list(known_face_encodings_dict.values())

    del known_face_encodings_dict

    for face_location in face_detection.get_face_locations(image_file_path):
        face_encoding = get_face_encodings(
            image_file_path, known_face_locations=[face_location]
        )[0]

        recognition_flags = face_recognition.compare_faces(
            known_face_encodings, face_encoding
        )

        for flag, name in zip(recognition_flags, known_names):
            if not flag:
                continue

            top, right, bottom, left = face_location
            draw.rectangle((left, top, right, bottom), outline="#FF1493")
            text_width, text_height = draw.textsize(name)
            draw.rectangle(
                (left, bottom, right, bottom + text_height + 10),
                fill="#FF1493",
                outline="#FF1493",
            )
            draw.text((left + 6, bottom + 5), name, fill="white")

    del draw  # conserve resources
    image_pil.show()


if __name__ == "__main__":

    import constants
    import utils

    for image_file_path in utils.deep_iterdir(constants.UNKNOWN_FACES_PATH):
        recognize_faces(image_file_path)
