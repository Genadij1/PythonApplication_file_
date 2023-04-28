
with open('file.txt', 'r') as f:
    content = f.readlines()
    if len(content) == len(set(content)):
        print('Повторів рядків немає')
    else:
        print('Повтори є')
