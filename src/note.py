import random

def fromPixelBrightness(pixel, song, time, duration):
  brightnessRatio = float(sum(pixel)) / 765
  pitch = 40 + brightnessRatio * 30

  return create(pitch, time, duration)

def create(pitch, time, duration, volume=100, track=0, channel=0):
  """Create a tuple representing the args that should be passed into
  a song when adding a note."""
  return (track, channel, pitch, time, duration, volume)

def addTo(song, note):
  song.addNote(*note)
