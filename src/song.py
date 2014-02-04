from PIL import Image
from midiutil.MidiFile import MIDIFile
import note
import random

noteDistances = [0.5, 1, 2, 4]

def addNotesFromColors(colors, song, noteGenerator, track=0):
  """Use the given colors and note generator to create notes and
  put them into the song."""
  time = 0
  for color in colors:
    time += random.choice(noteDistances)
    generatedNote = noteGenerator(color, song, time, 1, track=track)

    # unpack tuple as arguments for function
    song.addNote(*generatedNote)

def addNotesFromPixelBrightness(image, song):
  """Use the brightness of the individual pixels in the image to populate
  the given song with notes."""
  addNotesFromColors(image.getdata(), song, note.fromPixelBrightness)

def averageColorSequencer(image, song):
  """Use the average colors of squares in the image to add notes to the
  given song."""
  averageColorGrid = getAverageColors(image)

  for i in range(len(averageColorGrid)):
    row = averageColorGrid[i]
    addNotesFromColors(row, song, note.fromPixelBrightness, track=i)

  # addNotesFromColors(averageColorGrid[0], song, note.fromPixelBrightness)

def getAverageColors(image, resolution=80):
  """Get the average colors of each row of the image, with each square
  having a length of the given resolution."""
  data = image.getdata()
  width, height = image.size
  squareWidth, squareHeight = width / resolution, height / resolution

  rows = []
  for y in range(squareHeight):
    row = []
    for x in range(squareWidth):
      region = (x * resolution, y * resolution, resolution, resolution)
      row.append(getAverageColorFromRegion(region, data, width))

    rows.append(row)

  return rows

def getAverageColorFromRegion((x, y, w, h), pixelData, rowWidth):
  """Get the average colors from a given region of the pixel data.
  Requires the width of each row to index into the pixel data."""
  numPixels = w * h
  colorSum = [0, 0, 0]
  for y in range(y, y + h):
    start = x + rowWidth * y
    for index in range(start, start + w):
      # add color at the current pixel to the sum
      pixel = pixelData[index]
      colorSum[0] = colorSum[0] + pixel[0]
      colorSum[1] = colorSum[1] + pixel[1]
      colorSum[2] = colorSum[2] + pixel[2]

  return tuple(component / numPixels for component in colorSum)

def createFromImage(image, method=averageColorSequencer, tempo=100):
  """Create a song from the given image, using the provided method to add
  notes and playing at the given tempo."""
  song = initializeTrack(tempo)

  method(image, song)

  return song

def initializeTrack(tempo=100, numTracks=15):
  """Create a song with the given tempo."""
  song = MIDIFile(numTracks)

  time = 0
  for track in range(numTracks):
    song.addTrackName(track, time, "Track " + str(track))
    song.addTempo(track, time, tempo)

  return song
