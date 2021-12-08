# Osnovna manipulacijama slikama pomocu Pillow biblioteke

from PIL import Image

print("hello")

# TODO
image = Image.open("vehicle.jpg")
width, height = image.size
print(width, height)

rotated= image.rotate(270)


rotated.save("vehicle_90.jpg")

x = 200
y = 0 


rotated2= rotated.crop((x,y,width-x,height))
rotated2.show()


image2= Image.open("vehicle.jpg")
image2.show()

concatenated_images = Image.new("RGB", ((image.width + rotated2.width), max(image.height, rotated2.height)))
concatenated_images.paste(image, (0,0))
concatenated_images.paste(rotated2, (image.width, 0))
concatenated_images.show()

