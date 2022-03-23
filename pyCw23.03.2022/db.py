def save(filename, number):
    try:
        with open(str(filename),'a', encoding="UTF-8") as f:
            f.write(str(number))
            f.write("\n")
            #print(number, file=f)
    except IOError as e:
        print(e)

def load(filename):
    storage = []
    try:
        with open(str(filename), "r", encoding="UTF-8") as f:
            for line in f.readlines():
                try:
                    number = int(line)
                    storage.append(number)
                except(ValueError, TypeError) as _: #прочерк вместо имени переменной исключения
                    pass

    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)

    return storage




if __name__ == '__main__':


    save("numbers", 10)
    save("numbers", -7)
    save("numbers", 9)
    s = load("numbers")

    numbres = load("numbers.txt")
    print(s)
    print(numbres)