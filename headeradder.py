import os,sys,struct
from io import BytesIO

from PIL import Image

def getFileNameWithoutExtension(path):
    return path.split('\\').pop().split('/').pop().rsplit('.', 1)[0]

def headeradder(file):
    fl = open(file, 'rb')
    header = open("header", 'rb')
    filename = getFileNameWithoutExtension(file)
    #wrf = open(file+".dds", 'wb')
    wrf = BytesIO()
    wrf.write(header.read())
    wrf.write(fl.read())
    fl.close()
    header.close()
    pic = Image.open(wrf)
    pic = pic.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    #pic = pic.transpose(Image.Transpose.ROTATE_180)
    pic.save(filename + '.png', 'png')
    wrf.close()
    print("ddsheaderadder: '" + file + "' convert png success! Save as '" + filename + '.png' + "'")
    
def ddscov(file):
    pic = Image.open(file)
    pic.transpose(Image.FLIP_TOP_BOTTOM)
    pic.save(file + '.png', 'png')


if __name__ == '__main__':
    if len(sys.argv) < 2 :
        exit()
    files=[]
    files=sys.argv[1:]
    for file in files:
        headeradder(file)
