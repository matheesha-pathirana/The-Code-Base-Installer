import wget
url = "https://raw.githubusercontent.com/matheesha-pathirana/The-Code-Base-Installer/master/version?token=GHSAT0AAAAAABRGIOISZLPRA4MJQI7HG55AYSZM6VA"
wget.download(url, 'version.txt')
f=open('version.txt')
read=f.read()
if read=='0.0.2':
    print('You are uptodate!')

else:
    print('Please update to the latest version!')