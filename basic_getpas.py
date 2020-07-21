import getpass

try:
    pwd = getpass.getpass()
except Exception as ex:
    print('Error Occured : ', ex)
else:
    print('Entered secret :', pwd)