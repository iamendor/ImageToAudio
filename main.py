from PIL import Image
from numpy import array, random
import soundfile
from random import randint

im =  input("Fájl: ")
image = Image.open(im)
ar = array(image)
freq = []
output = randint(0, 1_000_000)
random = random.uniform(-1, 1, 44100)


for i in range(len(ar)):
    for j in range(len(ar[i])):
        code = ar[i][j]
        freq.append(sum(code)/1000) 

freq = array(freq)
soundfile.write(f"{output}.wav", freq, 44100)   
