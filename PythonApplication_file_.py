try:
    _file = open('New file.txt', 'r')
    _file.readline()
    if _file.readline() == 0:
        print('File is not empty')
except Exception as e:
    print(e)
finally:    
    _file.close()
