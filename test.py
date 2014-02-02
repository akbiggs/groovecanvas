#Import the library

from midiutil.MidiFile import MIDIFile
from PIL import Image
import random

RED = 0
BLUE = 1
GREEN = 2

def addNotesFrom(image, song):
    pointInTrack = 0
    noteDistances = [0.5, 1]

    for pixel in image.getdata():
      pointInTrack += random.choice(noteDistances)
      addNoteFrom(pixel, song, pointInTrack)

def addNoteFrom(pixel, song, pointInTrack = 0):
    track = 0
    channel = 0
    duration = 0.5

    brightnessRatio = float(sum(pixel)) / 765
    pitch = 40 + brightnessRatio * 30

    # track, channel, pitch, time, duration, volume
    song.addNote(track, channel, pitch, pointInTrack, duration, 100)

if __name__ == '__main__':

    testImage = Image.open("mona.jpg")
    testImage.thumbnail((24, 24), Image.ANTIALIAS)

    song = MIDIFile(1)

    track = 0
    time = 0

    song.addTrackName(track, time, "Sample Track")
    song.addTempo(track, time, 120)

    addNotesFrom(testImage, song)

    binfile = open("output.mid", 'wb')
    song.writeFile(binfile)
    binfile.close()

    print "Wrote track."
