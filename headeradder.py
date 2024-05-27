import os,sys,struct
from io import BytesIO

from PIL import Image


def build_header(width, height, has_alpha):
    if has_alpha:
        header_file = "header-bc7-template"
    else:
        header_file = "header-dxt1-template"
    with open(header_file, mode="rb") as f:
        header_bytes = bytearray(f.read())
    width_bytes = width.to_bytes(4, byteorder="little", signed=False)
    height_bytes = height.to_bytes(4, byteorder="little", signed=False)
    header_bytes[0xc:0x10] = height_bytes
    header_bytes[0x10:0x14] = width_bytes
    return header_bytes


def getFileNameWithoutExtension(path):
    return path.split('\\').pop().split('/').pop().rsplit('.', 1)[0]


def getDimensionsFromFooter(file_bytes: bytes):
    arr = bytearray(file_bytes)[-0x50:]
    width = int.from_bytes(arr[:4], byteorder="little", signed=False)
    height = int.from_bytes(arr[4:8], byteorder="little", signed=False)
    return (width, height)


def headeradder(file, has_alpha=False):
    fl = open(file, 'rb')
    file_bytes = fl.read()
    (width, height) = getDimensionsFromFooter(file_bytes)
    header = build_header(width, height, has_alpha)
    filename = getFileNameWithoutExtension(file)
    #wrf = open(file+".dds", 'wb')
    wrf = BytesIO()
    wrf.write(header)
    wrf.write(file_bytes)
    fl.close()
    pic = Image.open(wrf)
    pic = pic.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    # pic = pic.transpose(Image.Transpose.ROTATE_180)
    pic.save(filename + '.png', 'png')
    wrf.close()
    print("ddsheaderadder: '" + file + "' convert png success! Save as '" + filename + '.png' + "'")


def ddscov(file):
    pic = Image.open(file)
    pic.transpose(Image.FLIP_TOP_BOTTOM)
    pic.save(file + '.png', 'png')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit()

    has_alpha = sys.argv[1] == "-alpha"
    if has_alpha:
        files = sys.argv[2:]
    else:
        files = sys.argv[1:]

    for file in files:
        headeradder(file, has_alpha)