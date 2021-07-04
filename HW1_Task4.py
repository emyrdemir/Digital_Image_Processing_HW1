

from PIL import Image, ImageFilter, ImageOps

size_64 = (64,64)
image1 = Image.open('img.jpg')
image2 = Image.open('img2.jpg')
image3 = Image.open('img3.png')
image4 = Image.open('img4.jpg')
image1.show()
image2.show()
image3.show()
image4.show()

image1 = image1.filter(ImageFilter.CONTOUR)
image1.save('img_contour.png')

image2.thumbnail(size_64)
image2.save('img2_64.png')

image3 = ImageOps.grayscale(image3)
image3.save('image3_grayscale.png')

image1.show()
image2.show()
image3.show()
image4.rotate(180).show()