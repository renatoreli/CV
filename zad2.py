import glob
from PIL import Image
imgPath = "images" 
files = glob.glob(imgPath + '/**/*.jpg', recursive=True)

# TODO ispisite sve putanje
print(files)

# TODO svaku sliku pretvorite u grayscale i spremite u output direktorij pod nazivom img_x.jpg pri cemu je x redni broj slike
for index, imagePath in enumerate(files):
    print(index, imagePath)
    greyscale= Image.open(imagePath).convert("L")
    greyscale.save(f"output/img_{index}.jpg")