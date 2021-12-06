
if __name__ == "__main__":
    f = open("theLibrary.txt", "w")
    f.write("test")
    f.close()
    
    l = open("theLibrary.txt", "r")
    print(l.read())