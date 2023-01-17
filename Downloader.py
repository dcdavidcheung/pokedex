import requests
import re
import os.path

# This script will download all files from the URLs/URLs.txt and put them in Downloads directory
import os
cwd = os.getcwd()
# downloadDir = f"{cwd}/serebii_download/"
downloadDir = f"{cwd}/normal/"

import time
# while(True):
#     response = input('Redownload All files ?(Y,N): ')
#     if(response in ['Y', 'y']):
#         ReDownloadOnlyCorruptedFiles = False
#         break
#     if(response in ['n', 'n']):
#         ReDownloadOnlyCorruptedFiles = True
#         # Re-download only corrupted files (sometimes <1kb corrupted files are downloaded from Bulbapedia)
#         print('Only new/ corrupted fniles will be downloaded')
#         break

def Download(FileName):
    with open(FileName, 'wb') as file:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
        print("Downloaded: "+url)

def convert_to_3_digit_string(number):
    number = int(number)
    if number < 100:
        if number < 10:
            return "00"+str(number)
        return "0"+str(number)
    return str(number)

# f = open('URLs/URLs.txt', 'r')
# f = open('URLs/test_serebii.txt', 'r')
# Lines = f.readlines()
URLs = []
# for line in Lines:
#     URLs.append(line.strip())  # Striping the newline character
# Exceed max at 513, need to restart at 513
# Exceed max at 532, need to restart at 532
# Exceed max at 571, need to restart at 571
# for i in range(571, 905):
# Exceed max at 19, need to restart at 19
for i in range(19, 905):
    # Shiny
    # URLs.append(f'https://www.serebii.net/Shiny/SWSH/{convert_to_3_digit_string(i+1)}.png')
    # Regular
    URLs.append(f'https://www.serebii.net/swordshield/pokemon/{convert_to_3_digit_string(i+1)}.png')
# f.close()

# Downloading
ticker = 0
for url in URLs:
    ticker += 1
    if ticker % 10 == 0:
        time.sleep(10)
    try:
        id = re.search("/\d\d\d", url).group(0)
        id = id[1:]
    except AttributeError:
        print('An Error Occured for: ' + id)
    fileToDownload = downloadDir+id+".png"
    r = requests.get(url, stream=True)
    # if(not ReDownloadOnlyCorruptedFiles):  # (Re-)Download all files unconditionally
    #     Download(fileToDownload)
    # elif(os.path.exists(fileToDownload)):
    #     file_stat = os.stat(fileToDownload)
    #     if(file_stat.st_size < 1000):  # Re-download only corrupted files
    #         Download(fileToDownload)
    # else:
    Download(fileToDownload)  # Download new file