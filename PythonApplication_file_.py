
try:
    with open('New file.txt', 'r') as f:
        line_number = int(input('Enter line number: ')) 
        current_line_number = 1
        for line in f:
            if current_line_number == line_number:
                print(line)
                break
        else:
            print(f"Рядок з номером {line_number} не знайдено")
except Exception as e:
    print(e)


