
with open('file.txt', 'r') as f:
    sorted_line = sorted([line.strip() for line in f.readlines()])
    print(sorted_line)
    
    