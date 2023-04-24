#word = input('Enter a word: ')
#with open('New file.txt', 'r') as file:
 #   line = file.readlines()
 #   if word in line:
  #      print(line)

word = input('Enter word: ')
 
inp = iter(open('New file.txt').readlines())
 
for i in inp:
    if word in i:
        print(i)
        





