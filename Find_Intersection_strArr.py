def FindIntersection(strArr):
    """ Function:
        1. Splits 2 arrays into separate data (numbers separated by ", ")
        2. Creates a string to return
        3. Loops through the data of array 1
        4. Compares for the presence of the same data between array 1 and array 2
        5. Writes to "2" found in "4"
        6. Returns "2" (excluding the last comma) """
    # print(strArr[0])
    # if strArr[0] not in strArr[1]:
    #   return False
    # else:
    #   print('There are Intersections')

    """ Splits Arr into separate data """
    list_0 = strArr[0].split(", ")
    # print(list_0)
    """ Splits Arr into separate data """
    list_1 = strArr[1].split(", ")
    # print(list_1)

    """ Here we collect data for return """
    intersections_list = ''

    """ Looping through list_0 data """
    for i in list_0:
        # print(i)
        """ Select data from list_0 that is present in list_1 """
        if i in list_1:
            # print(str(i) + '   # There are Intersections')
            intersections_list += i + ','

    # print('Output: '+ intersections_list)
    """ Returns Intersections (excluding the last comma) """
    return intersections_list[0:-1]


# keep this function call here
print(FindIntersection(input()))