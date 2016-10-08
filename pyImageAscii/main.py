# coding=utf-8

from PIL import Image
import argparse


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '

    length = len(ascii_char)
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=80)
parser.add_argument('--height', type=int, default=80)
args = parser.parse_args()


if __name__ == '__main__':
    im = Image.open(args.file)
    im = im.resize((args.width, args.height), Image.NEAREST)

    txt = ""

    for i in range(args.height):
        for j in range(args.width):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print txt

    if args.output:
        with open(args.output, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)
