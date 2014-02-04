#Import the library

from PIL import Image
import song

RED = 0
BLUE = 1
GREEN = 2

if __name__ == '__main__':
    testImage = Image.open("resources/images/mona.jpg")

    songGenerated = song.createFromImage(testImage)

    binfile = open("resources/sounds/output.mid", 'wb')
    songGenerated.writeFile(binfile)
    binfile.close()

    print "Wrote track."
