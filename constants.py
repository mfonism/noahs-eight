import pathlib

BP = BASE_PATH = pathlib.Path(__file__).absolute().parent
IP = IMAGES_PATH = BASE_PATH.joinpath("Images")

TEFP = THE_EIGHT_FACES_PATH = IMAGES_PATH.joinpath("TheEightFaces")
TEFXP = THE_EIGHT_FACES_EXTRA_PATH = IMAGES_PATH.joinpath("TheEightFacesExtra")

SP = SKINNIES_PATH = IMAGES_PATH.joinpath("Skinnies")
UFP = UNKNOWN_FACES_PATH = IMAGES_PATH.joinpath("UnknownFaces")
