import PIL.Image
 
img_flag = True
path = "./logo.png"
 
try:
  img = PIL.Image.open(path)
  img_flag = True
except Exception as e:
  print(f"{path} Unable to find image: {str(e)}")
 
width, height = img.size
aspect_ratio = height/width
new_width = 60
new_height = aspect_ratio * new_width * 0.45
img = img.resize((new_width, int(new_height)))
 
img = img.convert('L')
chars = ["*", "*", "*", "*", "*", "*", "*", " ", " ", " ", " "]
 
pixels = img.getdata()
new_pixels = [chars[pixel//24] for pixel in pixels]
new_pixels = ''.join(new_pixels)
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
 
with open("ascii_image.txt", "w") as f:
 f.write(ascii_image)