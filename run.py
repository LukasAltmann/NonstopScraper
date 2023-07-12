from extract import translate_file
from scrape import scrape
import glob
import os

def delete_files(path):
    files = glob.glob(path + '*')
    for f in files:
        os.remove(f)


amount = 10
input_directory = './input/'
output_directory = './output/'

delete_files(input_directory)
delete_files(output_directory)

scrape(amount)

for filename in os.listdir(input_directory):
    translate_file(filename)

print()
print('Successfully scraped and parsed ' + str(amount) + ' days of program')
