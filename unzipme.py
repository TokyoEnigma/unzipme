import sys, pyzipper

listPath = sys.argv[1]
zipPath = sys.argv[2]

with open(listPath, 'r') as f:
    global items
    passWord = f.read()
    f.close()
    passWord = passWord.splitlines()
    
for i in passWord:
    with pyzipper.AESZipFile(zipPath, 'r') as zip:
        try:
            zip.extractall(pwd = bytes(i, 'utf-8'))
            print('Success. Files extracted. Password: ' + i)
            sys.exit()
        except RuntimeError:
            print('Failed. Tried pass: ' + i)
