file = open('file.txt', 'r')
for line in file:
    for word in line.split():
        if word.isdigit():
            print(word)
file.close()



