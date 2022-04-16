import os
import random
import shutil
import git

########################################################################################################################
rand_number = random.randint(1, 99999)
########################################################################################################################
main_dir = f"C:/Windows/Temp/The Code Base Installer - {rand_number}"
os.mkdir(main_dir)
print("Directory '% s' is built!" % main_dir)
########################################################################################################################
def version_read():
    f=open('D:/OneDrive - adithya/Programming/Python/The Code Base Installer/version.txt')
    read=f.read()
    if read=='0.0.3':
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
