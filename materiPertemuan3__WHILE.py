def main():
    i = 1
    size = int(input("Size : "))
    while i < size:
        j = 0
        k = i
        while k < size-1:
            print(" ", end='')
            k+=2

        while j < i :
            print("-", end = '')
            j=j+1

        print('')
        i+=2



#untuk memastikan bahwa nama dari progam ini adalah __main__
if __name__ == '__main__' :
    main()