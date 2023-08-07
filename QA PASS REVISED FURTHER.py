import os, time, pyautogui
from pathlib import Path
import webbrowser as web
import shutil
from glob import glob

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.0



ID = str(input('Type in the Site ID: '))
time.sleep(0.25)




def find_pilot_name():
    try:
        global fullpath
        fullpath = (str(glob(r'/Volumes/homes/*/' + ID +'-*')))
        global pliot_name
        Convert = list(fullpath.split('/'))
        global pilotname2
        pilotname2 = Convert[3]
        global pilotname
        pilotname = str(pilotname2)
    except:
        pass


#  this function will move the file in the server into the pass section while also renaming it
def move_to_pass():
    try:
        find_pilot_name()
        os.chdir(r'/Volumes/homes/' + pilotname)#add cwd
        for directory in Path.cwd().glob(f'{ID}*'):
            if directory.is_dir():
                file_name = (os.path.basename(directory))
                initial = input('enter initials here to pass in server: ')
                dest = r'/Volumes/homes/00 - QA Passed/Talon/' + file_name + '-' + 'QA' + initial + '-PASS'
                directory.rename(directory/dest)
                print('Moved to pass..')
            else:
                print('Unable to move to pass, please manually try it')
                pass
    except NameError:
        pass

# this function will fail the site and re-name it in the server to corrections needed
def corrections_needed():
    try:
        find_pilot_name()
        os.chdir(r'/Volumes/homes/' + pilotname)#add cwd
        for directory in Path.cwd().glob(f'{ID}*'):
            if directory.is_dir():
                file_name = (os.path.basename(directory))
                initial = input('enter initials here to fail in server: ')
                dest = r'/Volumes/homes/' + pilotname + '/' + file_name + '-' + 'QA' + initial + '-CORRECTIONS_NEEDED'
                directory.rename(directory/dest)
                print('File name changed to Corrections Needed..')
            else:
                print('Unable to fail, please manually try it')
                pass
    except NameError:
        pass


        

# this function finds full file name in the desktop based on the Site ID alone
def find_file():
    try:
        find_pilot_name()
        cwd = r'/Users/qa_share/Desktop/' + pilotname
        for x in Path.cwd().glob(f'{ID}*'):
                if x.is_dir():
                    return x
    except NameError or IndexError:
        pass



def find_file_alone():
    cwd = Path.cwd()
    for x in Path.cwd().glob(f'{ID}*'):
            if x.is_dir():
                return x




# this function simply clicks on the QR, this is where you will edit the x/y positions
def Click_Quality_Review():
    time.sleep(0.25)
    pyautogui.click(4896, 315)
    time.sleep(0.10)
    pyautogui.click(4896, 315)
    time.sleep(3)




#   this function will ignore any hidden .ds_store path
def find_hidden(directories):
    hidden = '.DS_Store'
    return True if hidden in directories else False
    hidden_count = len(hidden)



def Pass():
    print()
    talonview_link = str(input('Copy and paste the talonview link here and then press enter:  '))
    Click_Quality_Review()
    pyautogui.press('tab', presses = 2)
    time.sleep(0.6)
    pyautogui.press('down')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.press('tab', presses = 5)
    time.sleep(0.1)
    pyautogui.press('enter')
    pyautogui.press('down', presses = 2)
    time.sleep(0.1)
    pyautogui.press('enter')
    pyautogui.press('tab', presses = 4)
    pyautogui.hotkey('command', 'v')
    pyautogui.press('tab', presses = 2)
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('space')
    

    

def find_r_2():
    try:
        find_pilot_name()
        global DESKTOP
        DESKTOP = r'/Users/qa_share/Desktop/' + pilotname + '/' + ID        
        os.chdir(r'/Volumes/homes/' + pilotname)#add cwd
        for directory in Path.cwd().glob(f'{ID}*'):
            if directory.is_dir():
                R2D2 = "r'" + str(find_file())
                print('Loading files into desktop, please wait...')
                shutil.copytree(find_file(), DESKTOP)
                print('Success! The droid was found!')
                
                print('File transferred to desktop.')
            else:
                print('The droid youre looking for is not here.')
                break
    except NameError:
        pass



def QR():
    try:
        
        find_file()

         
        Site = str(DESKTOP)



        print()
        print()
        matterport = str(input('is there a Matterport? Y/N:  '))
        print()
        PF = str(input('Pass or fail? For pass, type P, if a fail, press enter to skip: '))
        if PF == 'P' or PF == 'p':
            Pass()
        else:
            pass




        
        if PF == 'P' or PF == 'p':
            pass
        else:
            print()
            talonview_link = str(input('Copy and paste the talonview link here and then press enter:  '))
            Click_Quality_Review()
            pyautogui.press('tab', presses = 2)
            time.sleep(0.6)
            pyautogui.press('down')
            time.sleep(0.2)
            pyautogui.press('enter')
            time.sleep(0.1)
            pyautogui.press('tab', presses = 5)
            time.sleep(0.1)
            pyautogui.press('enter')
            pyautogui.press('down', presses = 3)
            time.sleep(0.1)
            pyautogui.press('enter')
            pyautogui.press('tab', presses = 4)
            pyautogui.hotkey('command', 'v')
            pyautogui.press('tab', presses = 2)
            pyautogui.press('space')
            pyautogui.press('tab')
            pyautogui.press('space')
        print()
        print()
        print('**REMINDER; if you delete any photos on Talonview, this list will not be accurate**')
        print('-----')
        print('Site ID:')
        print(ID)
        print('-----')
        print('Processing, please wait...')
        print('-----')


        #   below will collect the photo count within each category and input results into salesforce:





        #   Access road
        try:
            os.chdir(Site + '/Access Road')
            if  os.getcwd() == Site + '/Access Road':
                os.chdir(Site + '/Access Road') 
                count = os.listdir(Site + '/Access Road')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print()
                print('Access Road:')
                AR = (len(count))
                if find_hidden(count) == True:
                    AR -= 1
                else:
                    pass
                print(AR)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(AR))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pass
        except:
            if  os.getcwd() == Site + '/Access Road' or os.getcwd() == Site + '/ACCESS ROAD':
                pass
            else:
                print('Access Road:')
                print('N/A:')
                print()
                pyautogui.press('tab', presses = 4)









        #  Cable run
        try:
            os.chdir(Site + '/Cable Run')

            if  os.getcwd() == Site + '/Cable Run':
                os.chdir(Site + '/Cable Run')
                count = os.listdir(Site + '/Cable Run')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print('Cable Run:')
                CR = (len(count))
                if find_hidden(count) == True:
                    CR -= 1
                else:
                    pass
                print(CR)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(CR))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')

            else:
                pyautogui.press('tab', presses = 4)
        except:
            if  os.getcwd() == Site + '/Cable run' or os.getcwd() == Site + '/CABLE RUN':
                pass
            else:
                print('Cable Run:')
                print('N/A:')
                print()
                pyautogui.press('tab', presses = 4)




        #  Downlook
        try:
            os.chdir(Site + '/Downlook')
            if  os.getcwd() == Site + '/Downlook':
                os.chdir(Site + '/Downlook')
                count = os.listdir(Site + '/Downlook')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                DL = (len(count))
                print('Downlook:')
                if find_hidden(count) == True:
                    DL -= 1
                else:
                    pass
                print(DL)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(DL))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pass
        except:
            pass




            #  Donwlook split
            try:
                os.chdir(Site + '/Downlook - Sector 1')
                if  os.getcwd() == Site + '/Downlook - Sector 1':
                    os.chdir(Site + '/Downlook - Sector 1')
                    count = os.listdir(Site + '/Downlook - Sector 1')
                    hidden_list = sorted(str((count)))
                    find_hidden(count)
                    length = (len(count))
                    if find_hidden(count) == True:
                        length -= 1
                    else:
                        pass
                    DOWN1 = length

                    os.chdir(Site + '/Downlook - Sector 2')
                    count2 = os.listdir(Site + '/Downlook - Sector 2')
                    hidden_list = sorted(str((count)))
                    find_hidden(count)
                    length2 = (len(count2))
                    if find_hidden(count) == True:
                        length -= 1
                    else:
                        pass
                    DOWN2 = length2

                    os.chdir(Site + '/Downlook - Sector 3')
                    count3 = os.listdir(Site + '/Downlook - Sector 3')
                    hidden_list = sorted(str((count)))
                    find_hidden(count)
                    length3 = (len(count3))
                    if find_hidden(count) == True:
                        length -= 1
                    else:
                        pass
                    DOWN3 = length3
                    DOWNS = DOWN1 + DOWN2 + DOWN3
                    print('Downlook:')
                    print(DOWNS)
                    print()
                    pyautogui.press('tab')
                    pyautogui.write(str(DOWNS))
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
                else:
                    pyautogui.press('tab', presses = 4)
            except:
                pass



            #  Donwlook split V2.0
            try:
                os.chdir(Site + '/Downlook 1')
                if  os.getcwd() == Site + '/Downlook 1':
                    os.chdir(Site + '/Downlook 1')
                    count = os.listdir(Site + '/Downlook 1')
                    hidden_list = sorted(str((count)))
                    find_hidden(count)
                    length = (len(count))
                    if find_hidden(count) == True:
                        length -= 1
                    else:
                        pass
                    DOWN1 = length

                    os.chdir(Site + '/Downlook 2')
                    count2 = os.listdir(Site + '/Downlook 2')
                    hidden_list = sorted(str((count)))
                    find_hidden(count)
                    length2 = (len(count2))
                    if find_hidden(count) == True:
                        length -= 1
                    else:
                        pass
                    DOWN2 = length2

                    os.chdir(Site + '/Downlook 3')
                    count3 = os.listdir(Site + '/Downlook 3')
                    hidden_list = sorted(str((count)))
                    find_hidden(count)
                    length3 = (len(count3))
                    if find_hidden(count) == True:
                        length -= 1
                    else:
                        pass
                    DOWN3 = length3
                    DOWNS = DOWN1 + DOWN2 + DOWN3
                    print('Downlook:')
                    print(DOWNS)
                    print()
                    pyautogui.press('tab')
                    pyautogui.write(str(DOWNS))
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
                else:
                    pyautogui.press('tab', presses = 4)
            except:
                pass




            #  Donwlook split only two sectors
            try:
                os.chdir(Site + '/Downlook - Sector 1')
                if  os.getcwd() == Site + '/Downlook - Sector 1':
                    os.chdir(Site + '/Downlook - Sector 1')
                    count = os.listdir(Site + '/Downlook - Sector 1')
                    hidden_list = sorted(str((count)))
                    find_hidden(count)
                    length = (len(count))
                    if find_hidden(count) == True:
                        length -= 1
                    else:
                        pass
                    DOWN1point2 = length

                    os.chdir(Site + '/Downlook - Sector 2')
                    count2 = os.listdir(Site + '/Downlook - Sector 2')
                    hidden_list = sorted(str((count)))
                    find_hidden(count)
                    length2 = (len(count2))
                    if find_hidden(count) == True:
                        length -= 1
                    else:
                        pass
                    DOWN2point2 = length2
                    DOWNSS = DOWN1point2 + DOWN2point2
                    print('Downlook:')
                    print(DOWNSS)
                    print()
                    pyautogui.press('tab')
                    pyautogui.write(str(DOWNSS))
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
                else:
                    pyautogui.press('tab', presses = 4)
            except:
                pass






            #  Donwlook split only two sectors V2.0
            try:
                os.chdir(Site + '/Downlook 1')
                if  os.getcwd() == Site + '/Downlook 1':
                    os.chdir(Site + '/Downlook 1')
                    count = os.listdir(Site + '/Downlook 1')
                    hidden_list = sorted(str((count)))
                    find_hidden(count)
                    length = (len(count))
                    if find_hidden(count) == True:
                        length -= 1
                    else:
                        pass
                    DOWN1point2 = length

                    os.chdir(Site + '/Downlook 2')
                    count2 = os.listdir(Site + '/Downlook 2')
                    hidden_list = sorted(str((count)))
                    find_hidden(count)
                    length2 = (len(count2))
                    if find_hidden(count) == True:
                        length -= 1
                    else:
                        pass
                    DOWN2point2 = length2
                    DOWNSS = DOWN1point2 + DOWN2point2
                    print('Downlook:')
                    print(DOWNSS)
                    print()
                    pyautogui.press('tab')
                    pyautogui.write(str(DOWNSS))
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
                else:
                    pyautogui.press('tab', presses = 4)
            except:
                pass








        #  Down orbit
        try:
            os.chdir(Site + '/Down Orbit')
            if  os.getcwd() == Site + '/Down Orbit':
                    os.chdir(Site + '/Down Orbit')
                    count = os.listdir(Site + '/Down Orbit')
                    hidden_list = sorted(str((count)))
                    find_hidden(count)
                    DO = (len(count))
                    print('Downlook:')
                    if find_hidden(count) == True:
                        DO -= 1
                    else:
                        pass
                    print(DO)
                    print()
                    pyautogui.press('tab')
                    pyautogui.write(str(DO))
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
            else:
                pyautogui.press('tab', presses = 4)
        except:
            if  os.getcwd() == Site + '/Downlook' or os.getcwd() == Site + '/Down Orbit' or os.getcwd() == Site + '/DOWNLOOK' or os.getcwd() == Site + '/Downlook - Sector 3' or os.getcwd() == Site + '/Downlook 3' or os.getcwd() == Site + '/Downlook - Sector 2' or os.getcwd() == Site + '/Downlook 2':
                pass
            else:
                print('Downlook:')
                print('N/A:')
                print()
                pyautogui.press('tab', presses = 4)






        #  Center
        try:
            os.chdir(Site + '/Center')
            if  os.getcwd() == Site + '/Center':
                os.chdir(Site + '/Center')
                count = os.listdir(Site + '/Center')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print('Center:')
                CE = (len(count))
                if find_hidden(count) == True:
                    CE -= 1
                else:
                    pass
                print(CE)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(CE))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pass
        except:
            pass









        #   Center Out
        try:
            os.chdir(Site + '/Center Out')
            if  os.getcwd() == Site + '/Center Out':
                os.chdir(Site + '/Center Out')
                count = os.listdir(Site + '/Center Out')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print('Center:')
                CO = (len(count))
                if find_hidden(count) == True:
                    CO -= 1
                else:
                    pass
                print(CO)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(CO))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pass
        except:
            pass







        #   Center Facing Away
        try:
            os.chdir(Site + '/Center Facing Away')
            if  os.getcwd() == Site + '/Center Facing Away':
                os.chdir(Site + '/Center Facing Away')
                count = os.listdir(Site + '/Center Facing Away')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print('Center:')
                CA = (len(count))
                if find_hidden(count) == True:
                    CA -= 1
                else:
                    pass
                print(CA)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(CA))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pass
        except:
            pass

        

            #   Center Orbit Facing Away
            try:
                os.chdir(Site + '/Center Orbit Facing Away')
                if  os.getcwd() == Site + '/Center Orbit Facing Away':
                    os.chdir(Site + '/Center Orbit Facing Away')
                    count = os.listdir(Site + '/Center Orbit Facing Away')
                    hidden_list = sorted(str((count)))
                    find_hidden(count)
                    print('Center:')
                    CA = (len(count))
                    if find_hidden(count) == True:
                        CA -= 1
                    else:
                        pass
                    print(CA)
                    print()
                    pyautogui.press('tab')
                    pyautogui.write(str(CA))
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
                else:
                    pass
            except:
                pass

            #   Center Orbit Facing Out
            try:
                os.chdir(Site + '/Center Orbit Facing Out')
                if  os.getcwd() == Site + '/Center Orbit Facing Out':
                    os.chdir(Site + '/Center Orbit Facing Out')
                    count = os.listdir(Site + '/Center Orbit Facing Out')
                    hidden_list = sorted(str((count)))
                    find_hidden(count)
                    print('Center:')
                    CA = (len(count))
                    if find_hidden(count) == True:
                        CA -= 1
                    else:
                        pass
                    print(CA)
                    print()
                    pyautogui.press('tab')
                    pyautogui.write(str(CA))
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
                else:
                    pass
            except:
                pass


            #   Center Away
            try:
                os.chdir(Site + '/Center Away')
                if  os.getcwd() == Site + '/Center Away':
                    os.chdir(Site + '/Center Away')
                    count = os.listdir(Site + '/Center Away')
                    hidden_list = sorted(str((count)))
                    find_hidden(count)
                    print('Center:')
                    CA = (len(count))
                    if find_hidden(count) == True:
                        CA -= 1
                    else:
                        pass
                    print(CA)
                    print()
                    pyautogui.press('tab')
                    pyautogui.write(str(CA))
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
                    pyautogui.press('tab')
                    pyautogui.press('space')
                else:
                    pass
            except:
                pass



        #   Center Facing Out
        try:
            os.chdir(Site + '/Center Facing Out')
            if  os.getcwd() == Site + '/Center Facing Out':
                os.chdir(Site + '/Center Facing Out')
                count = os.listdir(Site + '/Center Facing Out')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print('Center:')
                CFO = (len(count))
                if find_hidden(count) == True:
                    CFO -= 1
                else:
                    pass
                print(CFO)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(CFO))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pass
        except:
            pass








        #   Center Orbit
        try:
            os.chdir(Site + '/Center Orbit')
            if  os.getcwd() == Site + '/Center Orbit':
                os.chdir(Site + '/Center Orbit')
                count = os.listdir(Site + '/Center Orbit')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print('Center:')
                CA = (len(count))
                if find_hidden(count) == True:
                    CA -= 1
                else:
                    pass
                print(CA)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(CA))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pass
        except:
            if  os.getcwd() == Site + '/Center' or os.getcwd() == Site + '/Center Out' or os.getcwd() == Site + '/Center Facing Away' or os.getcwd() == Site + '/Center Facing Out' or os.getcwd() == Site + '/Center Orbit' or os.getcwd() == Site + '/Center Orbit Facing Away' or os.getcwd() == Site + '/Center Orbit Facing Out' or os.getcwd() == Site + '/Center Away':
                pass
            else:
                print('Center:')
                print('N/A:')
                print()
                pyautogui.press('tab', presses = 4)








        #  Uplook
        try:
            os.chdir(Site + '/Uplook')
            if  os.getcwd() == Site + '/Uplook':
                os.chdir(Site + '/Uplook')
                count = os.listdir(Site + '/Uplook')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print('Uplook:')
                UL = (len(count))
                if find_hidden(count) == True:
                    UL -= 1
                else:
                    pass
                print(UL)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(UL))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pass
        except:
            pass






        #  Up orbit
        try:
            os.chdir(Site + '/Up Orbit')
            if  os.getcwd() == Site + '/Up Orbit':
                os.chdir(Site + '/Up Orbit')
                count = os.listdir(Site + '/Up Orbit')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print('Uplook:')
                UO = (len(count))
                if find_hidden(count) == True:
                    UO -= 1
                else:
                    pass        
                print(UO)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(UO))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pyautogui.press('tab', presses = 4)
        except:
            if  os.getcwd() == Site + '/Uplook' or os.getcwd() == Site + '/Up Orbit' or os.getcwd() == Site + '/UPLOOK':
                pass
            else:
                print('Uplook:')
                print('N/A:')
                print()
                pyautogui.press('tab', presses = 4)







        #  Tower Site Overview
        try:
            os.chdir(Site + '/Tower Site Overview')
            if  os.getcwd() == Site + '/Tower Site Overview':
                os.chdir(Site + '/Tower Site Overview')
                count = os.listdir(Site + '/Tower Site Overview')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print('Tower Site Overview:')
                Tower = (len(count))
                if find_hidden(count) == True:
                    Tower -= 1
                else:
                    pass
                print(Tower)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(Tower))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pass
        except:
            pass


        #  Tower Site overview (Specifically for kevin who doesnt capitalize the O in overview)
        try:
            os.chdir(Site + '/Tower Site overview')
            if  os.getcwd() == Site + '/Tower Site overview':
                os.chdir(Site + '/Tower Site overview')
                count = os.listdir(Site + '/Tower Site overview')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print('Tower Site Overview:')
                Tower = (len(count))
                if find_hidden(count) == True:
                    Tower -= 1
                else:
                    pass
                print(Tower)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(Tower))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pass
        except:
            pass

        




        #  TSO
        try:
            os.chdir(Site + '/TSO')
            if  os.getcwd() ==  Site + '/TSO':
                os.chdir(Site + '/TSO')
                count = os.listdir(Site + '/TSO')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print('Tower Site Overview:')
                TSO = (len(count))
                if find_hidden(count) == True:
                    TSO -= 1
                else:
                    pass
                print(TSO)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(TSO))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pyautogui.press('tab', presses = 4)
        except:
            if  os.getcwd() == Site + '/Tower Site Overview' or os.getcwd() == Site + '/TSO' or os.getcwd() == Site + '/TOWER SITE OVERVIEW' or os.getcwd() == Site + '/Tower Site overview':
                pass
            else:
                print('Tower Site Overview:')
                print('N/A:')
                print()
                pyautogui.press('tab', presses = 4)







        #     Building Site Overview
        try:
            os.chdir(Site + '/Building Site Overview')
            if  os.getcwd() == Site + '/Building Site Overview':
                os.chdir(Site + '/Building Site Overview')
                count = os.listdir(Site + '/Building Site Overview')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print('Building Site Overview:')
                Building = (len(count))
                if find_hidden(count) == True:
                    Building -= 1
                else:
                    pass
                print(Building)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(Building))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pass
        except:
            pass








        #     Building Site overview
        try:
            os.chdir(Site + '/Building Site overview')
            if  os.getcwd() == Site + '/Building Site overview':
                os.chdir(Site + '/Building Site overview')
                count = os.listdir(Site + '/Building Site overview')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print('Building Site Overview:')
                Building = (len(count))
                if find_hidden(count) == True:
                    Building -= 1
                else:
                    pass
                print(Building)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(Building))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pass
        except:
            pass




        #     BSO
        try:
            os.chdir(Site + '/BSO')
            if  os.getcwd() == Site + '/BSO':
                os.chdir(Site + '/BSO')
                count = os.listdir(Site + '/BSO')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print('Building Site Overview:')
                BSO = (len(count))
                if find_hidden(count) == True:
                    BSO -= 1
                else:
                    pass
                print(BSO)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(BSO))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pyautogui.press('tab', presses = 4)
        except:
            if  os.getcwd() == Site + '/Building Site Overview' or os.getcwd() == Site + '/BSO' or os.getcwd() == Site + '/BUILDING SITE OVERVIEW' or os.getcwd() == Site + '/Building Site overview':
                pass
            else:
                print('Building Site Overview:')
                print('N/A:')
                print()
                pyautogui.press('tab', presses = 4)






        #  Sectors
        try:
            os.chdir(Site + '/Sector 1')
            if  os.getcwd() == Site + '/Sector 1':
                os.chdir(Site + '/Sector 1')
                count = os.listdir(Site + '/Sector 1')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                length = (len(count))
                if find_hidden(count) == True:
                    length -= 1
                else:
                    pass
                SEC1 = length

                os.chdir(Site + '/Sector 2')
                count2 = os.listdir(Site + '/Sector 2')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                length2 = (len(count2))
                if find_hidden(count) == True:
                    length -= 1
                else:
                    pass
                SEC2 = length2

                os.chdir(Site + '/Sector 3')
                count3 = os.listdir(Site + '/Sector 3')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                length3 = (len(count3))
                if find_hidden(count) == True:
                    length -= 1
                else:
                    pass
                SEC3 = length3
                SECS = SEC1 + SEC2 + SEC3
                print('Sectors combined:')
                print(SECS)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(SECS))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
            else:
                pyautogui.press('tab', presses = 4)
        except:
            if  os.getcwd() == Site + '/Sector 1':
                pass
            else:
                print('Arrays:')
                print('N/A:')
                print()
                pyautogui.press('tab', presses = 4)










        #  Civil
        try:
            os.chdir(Site + '/Civil')
            if  os.getcwd() == Site + '/Civil':
                os.chdir(Site + '/Civil')
                count = os.listdir(Site + '/Civil')
                hidden_list = sorted(str((count)))
                find_hidden(count)
                print('Civil:')
                CIV = (len(count))
                if find_hidden(count) == True:
                    CIV -= 1
                else:
                    pass
                print(CIV)
                print()
                pyautogui.press('tab')
                pyautogui.write(str(CIV))
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('space')
        except:
            if  os.getcwd() == Site + '/Civil' or os.getcwd() == Site + '/CIVIL':
                pass
            else:
                print('Civil:')
                print('N/A:')
                print()
                pyautogui.press('tab', presses = 4)



        if matterport == 'Y' or matterport == 'y':
            pyautogui.press('tab')
            pyautogui.press('space')
            pyautogui.press('tab')
            pyautogui.press('space')
            pyautogui.press('tab')
            pyautogui.press('space')
        else:
            pass

        if PF == 'P' or PF == 'p':
            move_to_pass()
        else:
            corrections_needed()
    except NameError or IndexError:
        print('ERROR: The droid youre looking for is not here. Check if the site was already uploaded into Talonview')


find_r_2()
QR()
