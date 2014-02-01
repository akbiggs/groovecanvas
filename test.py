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

    pitch = 60
    if pixel[RED] > 190:
      pitch = 70
    elif pixel[BLUE] > 180:
      pitch = 50
    elif pixel[GREEN] > 120:
      pitch = 38

    # track, channel, pitch, time, duration, volume
    song.addNote(track, channel, pitch, pointInTrack, duration, 100)

if __name__ == '__main__':

    image = Image.open("mona.jpg").crop((0, 0, 20, 20))

    song = MIDIFile(1)

    track = 0
    time = 0

    song.addTrackName(track, time, "Sample Track")
    song.addTempo(track, time, 120)

    addNotesFrom(image, song)

    binfile = open("output.mid", 'wb')
    song.writeFile(binfile)
    binfile.close()

    print "Wrote track."
