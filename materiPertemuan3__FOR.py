def main():
    x = int(input("Panjang Looping"))
    j = 0

    arr = [0,1,2,3,4,5,6]

    for i in range(0, x):
        for j in range(0, i+1):
            print("*", end = '')
        print('')
    # for i in range(0, 5) :
    #     print(i)


#untuk memastikan bahwa nama dari progam ini adalah __main__
if __name__ == '__main__' :
    main()