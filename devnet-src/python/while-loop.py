while True:
    x=input("Enter a number to count to or 'q' to quit: ")
    if x == 'q' or x == 'quit':
        break
    x = int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
