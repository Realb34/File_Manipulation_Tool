import os
import time
import webbrowser as web
import pyautogui as py
from pathlib import Path


ID = str(input('please type in the Site ID: '))
time.sleep(0.2)
print('-')
print('please select a pilot:')
print('-')
cwd = os.chdir(r'/Users/qa_share/Desktop')#add cwd
pilotlist = (sorted(os.listdir(r'')))#add cwd
print('\n'.join(pilotlist))
print()
pilotname = input('Enter here: ')
print('-')
print('processing, please wait')
time.sleep(2)


#change the cwd to the desired location (in our case it will be R2D2)
os.chdir(r'/' + pilotname)#add cwd
cwd = os.getcwd()


# searches for the file within R2D2
def find_r_2():
    for directory in Path.cwd().glob(f'{ID}*'):
        if directory.is_dir():
            os.chdir(r'/')# classified- enter a directory path here
            DESKTOP = Path.cwd()
            directory.replace(DESKTOP/directory.name)# DESKTOP is named after the folder
            print('Success! The droid was found!')
            print('File transferred to desktop.')
        else:
            print('the droid youre looking for is not here.')
            break
find_r_2()

# consider the gui automation requires two thingsa1 is that chrome will need to be opened full screen on one monitor
# and 2 is that a destination folder will be made in the top left of the left monitor that holds the Site IDs

# below is gui automation that requires x & y coordinants- set them appropriately
def open_talon():
    talonview = '' #classifed- link to webpage
    web.open(talonview)
    time.sleep(2)
    py.click(1479, 164)# opens dashboard
    py.click(1454, 208)
    py.moveTo(361, 214)# searches ID
    time.sleep(0.95)
    py.doubleClick()
    py.write(ID)
    py.press('return')# change to enter if using windows keyboard
    py.moveTo(140, 354)# opens the site for the next function to follow
    time.sleep(1.45)
    py.click()
open_talon()

# also set the x y coordinants here
def file_trans():
    py.moveTo(2479, 10)
    py.click(2479, 10)# open folder
    py.keyDown('command')
    py.keyDown('o')
    py.keyUp('command')
    py.keyUp('o')
    py.moveTo(1544,353)
    py.click()
    py.keyDown('command')
    py.keyDown('o')
    py.keyUp('command')
    py.keyUp('o')
    py.click(1276, 473)
    py.keyDown('command')
    py.keyDown('a')
    py.keyUp('command')
    py.keyUp('a')
    py.dragTo(2498, 665, button='left', duration=.75)#grab site id and drag
    time.sleep(1)# sleep just in case any network lag
file_trans()
