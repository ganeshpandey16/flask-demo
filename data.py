for i in range(10):
    f = open("data.txt", "a")
    f.write('my name is ganesh')
    f.write(str([1,2,3,4,5,6]))
    f.close()
    f = open("data.txt", "r")
    f.close()
