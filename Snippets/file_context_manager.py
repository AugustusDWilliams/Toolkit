filename = "/home/development/toolkit/example.log"


try:
    file = open(filename, "r")
except Exception as err:
    print(err)
else:
    with file:
        for line in file:
            print(line)
