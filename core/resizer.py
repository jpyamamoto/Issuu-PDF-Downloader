from PIL import Image


def scale(image, width, height):
    image_data = Image.open(image)

    image_data = image_data.resize((width, height))
    image_data.save(image)
