import matplotlib.pyplot as plt


def graph(x, y, z):
    plt.scatter(y, z)
    plt.xlabel('y')
    plt.ylabel('z')
    plt.title('x = 200')
    plt.legend()

    # function to show the plot
    plt.show()


if __name__ == "__main__":
    dict = {}
    n = int(input("Enter n to the size of the board (3*n):"))
    x = int(input("Enter x:")) #the size of the third line- in the graph
    # 1 in the first line, 1 in the second and 0 in the third (the first is the lowest)
    dict[(1, 1, 0)] = 'P'
    # dict[(3, 1, 0)] = 'P' #exp2
    # dict[(2, 1, 0)] = 'P'  #exp2
    # dict[(3, 0, 0)] = 'P'  #exp2
    # dict[(1, 1, 1)] = 'P'  #exp3
    # dict[(2, 1, 1)] = 'P'  #exp3
    # dict[(2, 0, 0)] = 'P'  #exp3
    # dict[(1, 0, 0)] = 'P' #exp4
    # dict[(2, 0, 0)] = 'P'  #exp4

    # fill the first line
    for i in range(2,n+1): #exp1 = 2, exp2 = 4, exp3 = 3, exp4 = 3
        # (i,0,0) not possible
        # (i,1,0) not possible
        dict[(i, 1, 0)] = 'N' #exp1+2 = (i,1,0), exp3 = (i,1,1) exp4 = (i,0,0)

    # fill the second line
    for second in range(2, n+1): #exp1+2+3 = 2, exp4 = 1
        for first in range(second, n+1):
            if dict.get((first, second, 0)) == None: # exp1+2+4 = 0, exp3 = 1
                temp = second-1
                flag = 1
                while temp > 0 & flag: #exp1+2+3 = >, exp4 = >=
                    if dict[(first, temp, 0)] == 'P': #exp1+2+4 = 0, exp3 = 1
                        dict[(first, second, 0)] = 'N' #exp1+2+4 = 0, exp3 = 1
                        flag = 0
                    temp -= 1

                tempFir = first-1
                tempSec = second
                while tempFir > 0 & flag: #exp1 = 0, exp2 = 2, exp3+4 = 1
                    if second > tempFir:
                        tempSec = tempFir;
                    if dict[(tempFir, tempSec, 0)] == 'P': #exp1+2+4 = 0, exp3 = 1
                        dict[(first, second, 0)] = 'N' #exp1+2+4 = 0, exp3 = 1
                        flag = 0
                    tempFir -= 1
                if flag == 1:
                    dict[(first, second, 0)] = 'P' #exp1+2+4 = 0, exp3 = 1
                    # print(first, second, 0)

    y = []
    z = []

    # fill the third line
    for third in range(1, x+1): #exp1+2+4 = 1, exp3 = 2
        for second in range(third, n+1):
            for first in range(second, n+1):
                if dict.get((first, second, third)) == None: 
                    temp = third - 1
                    flag = 1
                    while temp >= 0 & flag: #exp1+2+4 = >=0, exp3 = >0
                        if dict[(first, second, temp)] == 'P':
                            dict[(first, second, third)] = 'N'
                            flag = 0
                        temp -= 1

                    tempSec = second -1
                    tempThir = third
                    while tempSec > 0 & flag: #exp1+2+3 = >, exp4 = >=
                        if third > tempSec:
                            tempThir = tempSec;
                        if dict[(first, tempSec, tempThir)] == 'P':
                            dict[(first, second, third)] = 'N'
                            flag = 0
                        tempSec -= 1

                    tempFir = first - 1
                    tempSec = second
                    tempThir = third
                    while tempFir > 0 & flag: #exp1 = 0, exp2 = 2, exp3+4 = 1
                        if second > tempFir:
                            tempSec = tempFir;
                        if third > tempFir:
                            tempThir = tempFir;
                        if dict[(tempFir, tempSec, tempThir)] == 'P':
                            dict[(first, second, third)] = 'N'
                            flag = 0
                        tempFir -= 1
                    if flag == 1:
                        dict[(first, second, third)] = 'P'
                        # print(first, second, third)
                        if third == x:
                            y.append(second - third)
                            z.append(first - second)
    graph(x, y, z)