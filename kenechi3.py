def show_stars(rows):
    rows = int(input("Enter the number of rows:"))
    for i in range(rows):
        print("*" *(i + 1), "" * (rows -i-1))
show_stars(5)