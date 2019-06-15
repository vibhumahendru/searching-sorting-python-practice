testAr = [3,2,1,7,5]

# for val in range(0,len(a)-1):
#     print("sup")
#     for value in range(0, len(a)- val -1):
#             print(a[value], a[value+1])
#             if a[value+1] < a[value]:
#                 a[value + 1], a[value] = a[value], a[value + 1]
#
# print("answer is ", a)


def mySortFunction(a):
    for val in range(0,len(a)-1):
        # print("sup")
        for value in range(0, len(a)- val -1):
                # print(a[value], a[value+1])
                if a[value+1] < a[value]:
                    a[value + 1], a[value] = a[value], a[value + 1]

    # print("answer is ", a)
    return a


# mySortFunction(testAr)

# inputAr = int(input())

# print("this is your input ", inputAr)

def binarySearch(array, findNum):
    sortedAr = mySortFunction(array)
    # print(sortedAr)

    beg = 0
    end = len(sortedAr)-1
    while beg<=end:
        mid = (beg+end)//2
        if findNum == sortedAr[mid]:
            return mid
        elif findNum > sortedAr[mid]:
            beg = mid+1
        else:
            end = mid-1
    return 0



# found = binarySearch(testAr, 5)
#
# if found == 0:
#     print("Not Found")
# else:
#     print("FOUND at = ", found)

sortedAr = [1,2,3,8,9]
#
# def insert(array, num):
#     if array[6]:
#         print("yeeeee")
#
#
#
#
#
#
# insert(sortedAr, 5)
# array1 = [100]
# array1 = [1,2,3,4,5]
# array1.append(8)
# print(array1[6])

def insert(array, num):
    answerIndex = len(array)
    for index in range(0, len(array)):
        if num < array[index]:
            # print("test", index)
            answerIndex = index
            break
    array.append(0)
    print(array,  answerIndex)

    for value in range(len(array)-1, answerIndex, -1):
        array[value], array[value-1] = array[value-1], array[value]


    array[answerIndex] = num
    print(array,  answerIndex)

insert(sortedAr, 2)







###
