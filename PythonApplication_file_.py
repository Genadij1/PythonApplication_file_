
word = input('Enter word: ')
inp = iter(open('New file.txt').readlines())
for i in inp:
    if word in i:
        print(i)
        





