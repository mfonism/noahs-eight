import pathlib

BP = BASE_PATH = pathlib.Path(__file__).absolute().parent
IP = IMAGES_PATH = BASE_PATH.joinpath("Images")

KFP = KNOWN_FACES_PATH = IMAGES_PATH.joinpath("KnownFaces")
UFP = UNKNOWN_FACES_PATH = IMAGES_PATH.joinpath("UnknownFaces")

SP = SKINNIES_PATH = IMAGES_PATH.joinpath("Skinnies")
