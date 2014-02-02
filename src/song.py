from midiutil.MidiFile import MIDIFile
import note
import random

noteDistances = [0.5, 1]

def addNotesfromPixelBrightness(image, song):
  addNotesPerPixel(image, song, note.fromPixelBrightness)

def addNotesPerPixel(image, song, noteGenerator):
  time = 0
  for pixel in image.getdata():
    time += random.choice(noteDistances)

    generated = noteGenerator(pixel, song, time, 0.5)
    note.addTo(song, generated)

def createFromImage(image, method=addNotesfromPixelBrightness, tempo=120):
  song = initializeTrack(tempo)

  method(image, song)

  return song

def initializeTrack(tempo=120):
  song = MIDIFile(1)

  track = 0
  time = 0

  song.addTrackName(track, time, "Sample Track")
  song.addTempo(track, time, tempo)

  return song
