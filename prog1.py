from PIL import Image

def resize_auto(img,height_new):
    width, height = img.size
    width = width // (height//height_new)
    height = height_new
    img = img.resize((width, height), Image.ANTIALIAS)
    return img

def resize(img,width_new,height_new):
    width = width_new
    height = height_new
    img = img.resize((width,height), Image.ANTIALIAS)
    return img

def invert_color(img):
    width,height = img.size
    for c in range(height):
        for a in range(width):
            r,g,b = img.getpixel((a,c))
            img.putpixel((a,c),(255 - r, 255 - g, 255 - b))
    return img

def invert_hor(img):
    width,height = img.size
    inverted = Image.new('RGB',(width,height))
    for c in range(height):
        for a in range(width):
            inverted.putpixel((width - (a + 1), c),img.getpixel((a,c)))
    img = inverted
    return img

def invert_ver(img):
    width,height = img.size
    inverted = Image.new('RGB',(width,height))
    for c in range(height):
        for a in range(width):
            inverted.putpixel((a, height - (c + 1)),img.getpixel((a,c)))
    img = inverted
    return img

def convert(img,n):
    width, height = img.size
    infile = open('symbols.ini')
    outfile = open('done.txt','w')
    symbols = ''
    for i in range(n):
        symbols = infile.readline()[3:-1]
    count = len(symbols)
    full = 256 + 256 + 256  # максимальное значение
    segment = full // count  # длина сегмента
    result = ''
    for c in range(height):
        for a in range(width):
            r, g, b = img.getpixel((a,c))
            color = r + g + b
            pos = (color // segment) - 1
            result += symbols[pos] * 2
        result += '\n'
    outfile.write(result)
    infile.close()
    outfile.close()
