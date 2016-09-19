from PIL import Image


def resizer(image):
    image1 = Image.open(image)

# Change to resize images
    width = 1060
    height = 750

    image1 = image1.resize((width, height))
    image1.save(image)
