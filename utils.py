import pathlib


def deep_iterdir(path):
    return _deep_iterdir(pathlib.Path(path))


def _deep_iterdir(path):
    for child in path.iterdir():
        if child.is_dir():
            for leaf in _deep_iterdir(child):
                yield leaf
        else:
            yield child


if __name__ == "__main__":
    from constants import IMAGES_PATH

    for file in deep_iterdir(IMAGES_PATH):
        print(file.name)
