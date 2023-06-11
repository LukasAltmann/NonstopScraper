from scrape import translate_file
import os

directory = './input/'

for filename in os.listdir(directory):
    translate_file(filename)
    print(filename + ' done!')
