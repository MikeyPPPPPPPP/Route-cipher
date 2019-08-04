"""
hello there

hre     read in a spiral
eeh
lxt
lox

prints:
hreeehlxtlox

1 8 7
2 9 6
3 4 5


1 12 11 10
2 13 16  9
3 14 15  8
4  5  6  7


1 17 16 15 14
2 18 25 24 13
3 19 26 23 12
4 20 21 22 11
5 6 7 8 9  10

f1

f2

f3

f4

f5

function 1# get and process the lengths

function 2# if len is less then 9

function 3# if len is less then 16

function 4# if len is less then 26

function 5# gets the output for the apropreet functions and combins them
     to make a full cipher
"""

print('''
message len has to be in range 1 to 26

len 9

len 16

len 26

nothing  < then 26

''')
message = "michael mikey  p"

#message = input('message: ')




# h r e     read in a spiral
# e e h
# l   t
# l o       this should be the output


def get_process(Mes):
    Message = Mes.replace(" ", "x")

    get_len = len(Message)
    if get_len <= 9:
        a = route_9(Message)
    elif get_len <= 16:
        a = route_16(Message)
    elif get_len <= 26:
        a = route_26(Message)



"""
1 8 7
2 9 6
3 4 5

"""

def route_9(mess):
    combined_list = []
    row1 = []
    row2 = []
    row3 = []
    number = []
    number[:0] = mess



    wordlen_route9 = len(mess)
    ro1 = [0, 7, 6]
    ro2 = [1, 8, 5]
    ro3 = [2, 3, 4]
    for x in range(0, 5):#wordlen_route9):
        if x in ro1:
            if mess[x] == " ":
                print("row 1", mess[x])  # for debbuging
                row1.append("x")
            else:
                #print("row 1", mess[x])  # for debbuging
                row1.append(mess[x])
        elif x in ro2:
            if mess[x] == " ":
                print("row 2", mess[x])  # for debbuging
                row2.append("x")
            else:
                #print("row 2", mess[x])  # for debbuging
                row2.append(mess[x])
        else:
            if mess[x] == " ":
                print("row 3", mess[x])  # for debbuging
                row3.append("x")
            else:
                #print("row 3", mess[x])  # for debbuging
                row3.append(mess[x])

    for x in range(6,7):
        f = ''
        if mess[x] == 'x':
            row1.append(mess[x])
            row1.append(mess[x+1])
        else:
            row1.append(mess[x + 1])
            row1.append(mess[x])
    row2.append(mess[8])
    row2.append(mess[5])

    print(row1)
    print(row2)
    print(row3)
    for x in row1:
        combined_list.append(x)

    for x in row2:
        combined_list.append(x)

    for x in row3:
        combined_list.append(x)

    str1 = ''.join(str(e) for e in combined_list)
    print(str1)

    #return row1, row2, row3


"""
1 12 11 10
2 13 16  9
3 14 15  8
4  5  6  7
"""

def route_16(mess):
    combined_list = []
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    numsret = []
    numsret[:0] = mess



    wordlen_route16 = len(mess)
    ro1 = [0, 11, 10, 9]
    ro2 = [1, 12, 15, 8]
    ro3 = [2, 13, 14, 7]
    ro4 = [3, 4, 5, 6]

    for x in range(0, 7):#wordlen_route16):
        if x in ro1:
            if mess[x] == " ":
                print("row 1", mess[x])  # for debbuging
                row1.append("x")
            else:
                row1.append(mess[x])
        elif x in ro2:
            if mess[x] == " ":
                print("row 2", mess[x])  # for debbuging
                row2.append("x")
            else:
                row2.append(mess[x])
        elif x in ro3:
            if mess[x] == " ":
                print("row 3", mess[x])  # for debbuging
                row3.append("x")
            else:
                row3.append(mess[x])
        else:
            if mess[x] == " ":
                print("row 4", mess[x])  # for debbuging
                row4.append("x")
            else:
                row4.append(mess[x])
    row1.append(mess[11])
    row1.append(mess[10])
    row1.append(mess[9])

    row2.append(mess[12])
    row2.append(mess[15])
    row2.append(mess[8])

    row3.append(mess[13])
    row3.append(mess[14])
    row3.append(mess[7])

    print(row1)
    print(row2)
    print(row3)
    print(row4)

    for x in row1:
        combined_list.append(x)

    for x in row2:
        combined_list.append(x)

    for x in row3:
        combined_list.append(x)

    for x in row4:
        combined_list.append(x)

    str1 = ''.join(str(e) for e in combined_list)
    print(str1)
    #return row1, row2, row3, row4


"""
1 17 16 15 14
2 18 25 24 13
3 19 26 23 12
4 20 21 22 11
5 6 7 8 9  10
"""

def route_26(mess):
    combined_list = []
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    numsret = []
    numsret[:0] = mess
    wordlen_route26 = len(mess)
    ro1 = [0, 16, 15, 14, 13]
    ro2 = [1, 17, 24, 23, 12]
    ro3 = [2, 18, 25, 22, 11]
    ro4 = [3, 19, 20, 21, 10]
    ro5 = [4, 5, 6, 7, 8, 9]
    for x in range(0,wordlen_route26):
        if x in ro1:
            row1.append(mess[x])
        elif x in ro2:
            row2.append(mess[x])
        elif x in ro3:
            row3.append(mess[x])
        elif x in ro4:
            row4.append(mess[x])
        else:
            row5.append(mess[x])

    for x in row1:
        combined_list.append(x)

    for x in row2:
        combined_list.append(x)

    for x in row3:
        combined_list.append(x)

    for x in row4:
        combined_list.append(x)

    for x in row5:
        combined_list.append(x)

    str1 = ''.join(str(e) for e in combined_list)
    print(str1)

    #return row1, row2, row3, row4, row5

print(get_process(message))
