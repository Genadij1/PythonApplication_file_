
file = open('file.txt', 'r')
line = file.readlines()
print(line)
line_change = int(input('Enter the line you want to change: ')) 
text = input('Enter the text you want to change: ')
for el in line:
        if el == line[line_change - 1]:
            line[line_change - 1] = text + '\n'
            print(' '.join(line))
file.close()
