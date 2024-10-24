while True:
    x = input("Enter number or 'stop' to finish: ")
    if x == "stop":
        break
    elif not x.isnumeric():
        print("Podaj liczbe albo 'stop'!")
        continue
    else: 
        x = float(x)
        print(f"x: {x}, x^3: {pow(x, 3)}")
