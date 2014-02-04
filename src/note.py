import random

def fromPixelBrightness(pixel, song, time, duration, volume=100, track=0, channel=0):
  """Creates a note from the brightness of the given pixel."""
  brightnessRatio = float(sum(pixel)) / 765
  pitch = 40 + brightnessRatio * 30

  return create(pitch, time, duration, volume, track, channel)

# I keep forgetting the order of the arguments for adding a note to a song,
# so this function reduces the number of arguments and gives reasonable defaults
# to the ones that don't always need to be specified.
def create(pitch, time, duration, volume=100, track=0, channel=0):
  """Create a tuple representing the args that should be passed into
  a song when adding a note."""
  return (track, channel, pitch, time, duration, volume)
