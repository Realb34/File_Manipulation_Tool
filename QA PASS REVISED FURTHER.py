import os
import time
import pyautogui as py

talonview_link = input('copy and paste talonview link here:  ')
ID = input('enter file name:  ')
print(os.getcwd())

def ACCESS_ROAD():
    try:
        cwd = os.chdir(r'/Users/qa_share/Desktop/' + ID + '/Access Road')
        count = os.listdir(r'/Users/qa_share/Desktop/' + ID + '/Access Road')
        print('-')
        print('Access road:')
        length = (len((count)))
        print(length)
        time.sleep(0.5)
    except:
        pass
ACCESS_ROAD()
AR = ACCESS_ROAD()

def CABLE_RUN():
    try:
        cwd = os.chdir(r'/Users/qa_share/Desktop/' + ID + '/Cable Run')
        count = os.listdir(r'/Users/qa_share/Desktop/' + ID + '/Cable Run')
        print('Cable run:')
        length = (len((count)))
        print(length)
        time.sleep(0.5)
    except:
        pass
CABLE_RUN()
CR = CABLE_RUN()

def DOWNLOOK():
    try:
        cwd = os.chdir(r'/Users/qa_share/Desktop/' + ID + '/Downlook')
        count = os.listdir(r'/Users/qa_share/Desktop/' + ID + '/Downlook')
        print('Downlook:')
        length = (len((count)))
        print(length)
        time.sleep(0.5)
    except:
        pass
DOWNLOOK()
DL = DOWNLOOK()

def DOWN_ORBIT():
    try:
        cwd = os.chdir(r'/Users/qa_share/Desktop/' + ID + '/Down orbit')
        count = os.listdir(r'/Users/qa_share/Desktop/' + ID + '/Down orbit')
        print('Downlook:')
        length = (len((count)))
        print(length)
        time.sleep(0.5)
    except:
        pass
DOWN_ORBIT()
DO = DOWN_ORBIT()

def CENTER():
    try:
        cwd = os.chdir(r'/Users/qa_share/Desktop/' + ID + '/Center')
        count = os.listdir(r'/Users/qa_share/Desktop/' + ID + '/Center')
        print('Center:')
        length = (len((count)))
        print(length)
        time.sleep(0.5)
    except:
        pass
CENTER()
CE = CENTER()

def UPLOOK():
    try:
        cwd = os.chdir(r'/Users/qa_share/Desktop/' + ID + '/Uplook')
        count = os.listdir(r'/Users/qa_share/Desktop/' + ID + '/Uplook')
        print('Uplook:')
        length = (len((count)))
        print(length)
        time.sleep(0.5)
    except:
        pass
UPLOOK()
UL = UPLOOK()

def UP_ORBIT():
    try:
        cwd = os.chdir(r'/Users/qa_share/Desktop/' + ID + '/Up orbit')
        count = os.listdir(r'/Users/qa_share/Desktop/' + ID + '/Up orbit')
        print('Uplook:')
        length = (len((count)))
        print(length)
        time.sleep(0.5)
    except:
        pass
UP_ORBIT()
UO = UP_ORBIT()

def TOWER_SITE_OVERVIEW():
    try:
        cwd = os.chdir(r'/Users/qa_share/Desktop/' + ID + '/Tower Site Overview')
        count = os.listdir(r'/Users/qa_share/Desktop/' + ID + '/Tower Site Overview')
        print('Tower site overview:')
        length = (len((count)))
        print(length)
        time.sleep(0.5)
    except:
        pass
TOWER_SITE_OVERVIEW()
TOWER = TOWER_SITE_OVERVIEW()

def TSO():
    try:
        cwd = os.chdir(r'/Users/qa_share/Desktop/' + ID + '/TSO')
        count = os.listdir(r'/Users/qa_share/Desktop/' + ID + '/TSO')
        print('Tower site overview:')
        length = (len((count)))
        print(length)
        time.sleep(0.5)
    except:
        pass
    
def BUILDING_SITE_OVERVIEW():
    try:
        cwd = os.chdir(r'/Users/qa_share/Desktop/' + ID + '/Building Site Overview')
        count = os.listdir(r'/Users/qa_share/Desktop/' + ID + '/Building Site Overview')
        print('BSO:')
        length = (len((count)))
        print(length)
        time.sleep(0.5)
    except:
        pass
BUILDING_SITE_OVERVIEW()
BLD_SITE = BUILDING_SITE_OVERVIEW()

def BSO():
    try:
        cwd = os.chdir(r'/Users/qa_share/Desktop/' + ID + '/BSO')
        count = os.listdir(r'/Users/qa_share/Desktop/' + ID + '/BSO')
        print('BSO:')
        length = (len((count)))
        print(length)
        time.sleep(0.5)
    except:
        pass
BSO()
BSO = BSO()

TSO()
TSO = TSO()

def CIVIL():
    try:
        cwd = os.chdir(r'/Users/qa_share/Desktop/' + ID + '/Civil')
        count = os.listdir(r'/Users/qa_share/Desktop/' + ID + '/Civil')
        print('Civil:')
        length = (len((count)))
        print(length)
        time.sleep(0.5)
    except:
        pass
CIVIL()
CIV = CIVIL()

def SECTORS():
    try:
        cwd = os.chdir(r'/Users/qa_share/Desktop/' + ID + '/Sector 1')
        count = os.listdir(r'/Users/qa_share/Desktop/' + ID + '/Sector 1')
        length = (len((count)))
        sector_1 = length
    
        cwd2 = os.chdir(r'/Users/qa_share/Desktop/' + ID + '/Sector 2')
        count2 = os.listdir(r'/Users/qa_share/Desktop/' + ID + '/Sector 2')
        length2 = (len((count2)))
        sector_2 = length2
    
        cwd3 = os.chdir(r'/Users/qa_share/Desktop/' + ID + '/Sector 3')
        count3 = os.listdir(r'/Users/qa_share/Desktop/' + ID + '/Sector 3')
        length3 = (len((count3)))
        sector_3 = length3
        total = sector_1 + sector_2 + sector_3
        print('Sectors combined:')
        print(total)
    except:
        pass
SECTORS()
SECT = SECTORS()



matterport = str(input('is there a Matterport? Y/N:  '))
print('Inputing, please wait...')
time.sleep(1.5)

#  creates QA review and enters pre req information
time.sleep(0.5)
py.doubleClick(1223, 263)
time.sleep(5)
py.click(843, 305)
time.sleep(1)
py.click(813, 343)
py.click(840, 447)
py.click(783, 518)
py.click(495, 698)
py.write(talonview_link)
py.click(525, 553)
py.scroll(-29)
py.click(467, 229)
py.click(468,280)
py.scroll(-2)

py.click(520, 262)
py.write(AR)
py.click(469, 308)
py.click(466, 357)
py.click(468, 412)

if CR:
    py.click(527, 471)
    py.write(CR)
    py.click(468, 519)
    py.click(467, 570)
    py.click(468, 621)
else:
    pass

if DL:
    py.click(526, 680)
    py.write(DL)
    py.scroll(-4)
    py.click(469,566)
    py.click(468,618)
    py.click(468, 668)
else:
    py.scroll(-4)

if CE:
    py.scroll(-11)
    py.click(552, 277)
    py.write(CE)
    py.click(472, 336)
    py.click(466, 387)
    py.click(466, 441)
else:
    py.scroll(-11)

if UL:
    py.click(532, 484)
    py.write(UL)
    py.click(468, 547)
    py.click(469, 598)
    py.click(467, 649)
else:
    pass

if TOWER:
    py.click(499, 702)
    py.write(TOWER)
    py.scroll(-4)
    py.click(468, 592)
    py.click(468, 644)
    py.click(468, 694)
elif TSO:
    py.click(499, 702)
    py.write(TSO)
    py.scroll(-4)
    py.click(468, 592)
    py.click(468, 644)
    py.click(468, 694)
else:
    py.scroll(-4)

py.scroll(-6)

if BLD_SITE:
    py.click(528, 513)
    py.write(BLD_SITE)
    py.click(468, 565)
    py.click(468, 614)
    py.click(468, 663)
elif BSO:
    py.click(528, 513)
    py.write(BSO)
    py.click(468, 565)
    py.click(468, 614)
    py.click(468, 663)
else:
    pass

py.scroll(-30)

if CIV:
    py.click(500, 362)
    py.write(CIV)
    py.click(468, 413)
    py.click(468, 464)
    py.click(468, 513)
else:
    pass

if matterport == 'Y':
    py.click(467, 564)
    py.click(467, 618)
    py.click(466,664)
else:
    pass
