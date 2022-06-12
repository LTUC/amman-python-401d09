
def compare(lis1, lis2):
    """
    Input: 2 lists
    It will compare the two lists and find the common values between them
    :return: list with common values
    """
    # solution 1
    # output = [] # O(1)
    # for i in lis1: # O(n)
    #     for j in lis2: # O(m)
    #         if i == j: # O(1)
    #             output.append(i) # O(1)
    #
    #
    #
    # return output

    # solution 2
    # O(n^2)
    # output = [] # O(1)
    # for i in lis1: # O(n)
    #     if i in lis2: # O(n)
    #         output.append(i) # O(1)
    # return(output)

    # solution 3
    # O(n)
    # output = [] # O(1)
    # print(list(zip(lis1, lis2)))
    # return [i for i,j in zip(lis1, lis2) if i == j]

    # Solution 4
    # O(n)
    # i = 0 # O(1)
    # j = 0 # O(1)
    # outlist = [] # O(1)
    # while i < len(list1): # O(n)
    #     if list1[i] == list2[j]: # O(1)
    #         outlist.append(list1[i]) # O(1)
    #     j += 1 # O(1)
    #     if j >= len(list2): # O(1)
    #         i += 1 # O(1)
    #         j = 0 # O(1)
    #
    # return outlist

    # Solution 5
    # O(n)
    # set1 = set(lis1) # O(n)
    # output = [] # O(1)
    # for i in lis2: # O(n)
    #     if i in set1: # O(1)
    #         output.append(i) # O(1)

    # Solution 5
    # O(n)
    output = [] # O(1)
    obj = {} # O(1)
    for i in list1: # O(n)
        obj[i] = 0 # O(1)


    for j in list2: # O(n)
        x = obj.get(j, None) # O(1)
        if x != None: # O(1)
            output.append(j) # O(1)

    print(obj)
    return output



if __name__ == "__main__":
    list1 = [ 5, True, False, "Yousef", "Ahmad", "Lila", "Mohammad"]
    list2 = [ 5, True, None, "Yousef", "Mouyad", "Malak"]

    output = compare(list1, list2)

    print(output)
    # print(1 == True)
