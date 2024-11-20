def main():
    
    size = int(input("Size : "))
    for i in range(1, size+1, 2) :
        for k in range(i, size-1, 2) :
            print(' ', end='')

        for j in range(0, i, 1) :
            if j == 0 or j == i-1 :
                print('*', end = '')
            else :
                 print(" ", end='')
        print('')
    
    for i in range(1, size+1, 2):
        for j in range(0, i, 2):
            print("-", end="")
        for j in range(size-1, i):
            print("*", end="")
            # if j==1 or j==i-1:
            #     print("*", end="")
            # else:
            #     print(" ", end="")
                
            
            
        print('')



#untuk memastikan bahwa nama dari progam ini adalah __main__
if __name__ == '__main__' :
    main()