import os
import random
import shutil
import git
from datetime import datetime
from datetime import date

current_version='0.0.4'

########################################################################################################################
rand_number = random.randint(1, 99999)
########################################################################################################################
now = datetime.now()
current_time = now.strftime("%H_%M_%S")
time_now = (current_time)
today = date.today()
########################################################################################################################
main_path = 'D:/OneDrive - adithya/Programming/Python/The Code Base Installer/log'
is_main_path = os.path.isdir(main_path)
if is_main_path == True:
    path = f'D:/OneDrive - adithya/Programming/Python/The Code Base Installer/log/Log--{today}'
    isFile = os.path.isdir(path)
    if isFile == True:
        f = open(f'D:/OneDrive - adithya/Programming/Python/The Code Base Installer/log/Log--{today}/Log--{time_now}--{rand_number}.txt', 'w+')
        f.write(f'{time_now}--Creating Log Folders...!\n')
        f.write(f'{time_now}--Success!!\n')
    else:
        os.mkdir(f'D:/OneDrive - adithya/Programming/Python/The Code Base Installer/log/Log--{today}')
        f = open(f'log/Log--{today}/Log--{time_now}--{rand_number}.txt', 'w+')
        f.write(f'{time_now}--Creating Log Folders...!\n')
        f.write(f'{time_now}--Success!!\n')
else:
    os.mkdir('D:/OneDrive - adithya/Programming/Python/The Code Base Installer/log')
    os.mkdir(f'D:/OneDrive - adithya/Programming/Python/The Code Base Installer/log/Log--{today}')
    f = open(f'D:/OneDrive - adithya/Programming/Python/The Code Base Installer/log/Log--{today}/Log--{time_now}--{rand_number}.txt', 'w+')
    f.write(f'{time_now}--Creating Log Folders...!\n')
    f.write(f'{time_now}--Success!!\n')
########################################################################################################################
main_dir = f"C:/Windows/Temp/The Code Base Installer - {rand_number}"
os.mkdir(main_dir)
print("Directory '% s' is built!" % main_dir)
########################################################################################################################
def version_read():
    f=open('D:/OneDrive - adithya/Programming/Python/The Code Base Installer/version.txt')
    read=f.read()
    if read>=current_version:
        print('you are uptodate!')
    else:
        print('pls update to the latest version!')
########################################################################################################################
git.Git(main_dir).clone("https://gist.github.com/7554ffa2272a586e0dff328166dac075.git")
print("Cloning GIT Repo...")
is_file_alv='D:/OneDrive - adithya/Programming/Python/The Code Base Installer/version.txt'
version_file=os.path.isfile(is_file_alv)
if version_file==True:
    os.remove('D:/OneDrive - adithya/Programming/Python/The Code Base Installer/version.txt')
    shutil.move(f"C:/Windows/Temp/The Code Base Installer - {rand_number}/7554ffa2272a586e0dff328166dac075/version.txt", "D:\OneDrive - adithya\Programming\Python\The Code Base Installer")
    version_read()
else:
    shutil.move(f"C:/Windows/Temp/The Code Base Installer - {rand_number}/7554ffa2272a586e0dff328166dac075/version.txt","D:\OneDrive - adithya\Programming\Python\The Code Base Installer")
    version_read()
########################################################################################################################
