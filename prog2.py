from PIL import Image
import module

img = Image.open('l.jpg')
img = module.resize(img,788,900)
img = module.resize_auto(img,50)
img = module.invert_color(img)
# img = module.invert_hor(img)
# img = module.invert_ver(img)
img.save('ch.jpg')
module.convert(img,2)
