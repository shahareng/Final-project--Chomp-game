import matplotlib.pyplot as plt


def graph(x, y, z):
    plt.scatter(y, z)
    plt.xlabel('y')
    plt.ylabel('z')
    plt.title('x = 300')
    plt.legend()

    # function to show the plot
    plt.show()


if __name__ == "__main__":
    dict = {}
    n = input("Enter n to the size of the board (3*n):")
    x = input("Enter x:") #the size of the third line- in the graph
    # 1 in the first line, 0 in the second and 0 in the third (the first is the lowest)
    dict[(1, 0, 0)] = 'P'

    # fill the first line
    for i in range(2,n+1):
        dict[(i, 0, 0)] = 'N'

    #fill the second line
    for second in range(1,n+1):
        for first in range(second,n+1):
            temp = second-1
            flag = 1
            while temp >= 0 & flag:
                if dict[(first, temp, 0)] == 'P':
                    dict[(first, second, 0)] = 'N'
                    flag = 0
                temp -= 1

            tempFir = first-1
            tempSec = second
            while tempFir > 0 & flag:
                if second > tempFir:
                    tempSec = tempFir;
                if dict[(tempFir, tempSec, 0)] == 'P':
                    dict[(first, second, 0)] = 'N'
                    flag = 0
                tempFir -= 1
            if flag == 1:
                dict[(first, second, 0)] = 'P'
                #print(first, second, 0)

    y = []
    z = []
    # fill the third line
    for third in range(1, x+1):
        for second in range(third,n+1):
            for first in range(second, n+1):
                temp = third - 1
                flag = 1
                while temp >= 0 & flag:
                    if dict[(first, second, temp)] == 'P':
                        dict[(first, second, third)] = 'N'
                        flag = 0
                    temp -= 1

                tempSec = second -1
                tempThir = third
                while tempSec >= 0 & flag:
                    if third > tempSec:
                        tempThir = tempSec;
                    if dict[(first, tempSec, tempThir)] == 'P':
                        dict[(first, second, third)] = 'N'
                        flag = 0
                    tempSec -= 1

                tempFir = first - 1
                tempSec = second
                tempThir = third
                while tempFir > 0 & flag:
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
                    #print(first, second, third)
                    if third == x:
                        y.append(second-third)
                        z.append(first-second)

    graph(x, y, z)