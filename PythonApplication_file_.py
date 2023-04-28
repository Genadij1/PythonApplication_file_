
try:
    with open('file.txt', 'r') as file:
        text = file.readlines()
        start = int(input('Enter the line with start: '))
        for line in text:
            if start <= 0:
                print('Enter the correct line!')
            else:
                print(' '.join(text[start-1:]))
                break
except ValueError as e: 
    print(f'error: {e}')
      