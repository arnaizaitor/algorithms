from math import floor
from math import sqrt

class Searcher:
    def __init__(self):
        pass

    ########################################################################################################################################################
    # Function Name: binarySearch
    # Attributes: + self: Searcher instance
    #             + List: (ascending by default) ordered list where we want to search (can contain any type of object)
    #             + target: object we want to see whether it is in List or not
    #             + ascending: boolean that tells us if the list is ascending ordered or descending ordered
    #
    # Return:     + int: -1 if the target doesn't appear in List, the index of target if it does appear in List
    ########################################################################################################################################################
    def binarySearch(self, List, target, ascending = True):
        if (isinstance(List,(list,tuple,)) == False):
            print('The first attribute should be an ordered list')
            return -1

        if(len(List) <= 0):
            print('The list must not be empty')
            return -1

        pointerA = 0
        pointerB = len(List) - 1
        stop = -1

        while(1):
            if(List[pointerA] == target):
                return pointerA

            elif(List[pointerB] == target):
                return pointerB

            else:
                pointerC = int(floor((pointerA + pointerB)/2))

                #Stop condition
                if (stop == pointerC):
                    return -1

                stop = pointerC
                #End of stop condition

                if(List[pointerC] == target):
                    return pointerC

                #If the list is ascending ordered
                if(ascending == True):
                    if(List[pointerC] < target):
                        pointerA = pointerC

                    else:
                        pointerB = pointerC

                #If the list is in descending order, we do the opposite of what we do when it's ascening-sorted
                else:
                    if(List[pointerC] < target):
                        pointerB = pointerC

                    else:
                        pointerA = pointer

    ########################################################################################################################################################
    # Function Name: linearSearch
    # Attributes: + self: Searcher instance
    #             + List: unordered list where we want to search (can contain any type of object)
    #             + target: object we want to see whether it is in List or not
    #
    # Return:     + int: -1 if the target doesn't appear in List, the index of the first appearance of the target if it does appear in List
    ########################################################################################################################################################
    def linearSearch(self, List, target):
        if (isinstance(List,(list,tuple,)) == False):
            print('The first attribute should be an ordered list')
            return -1

        if(len(List) <= 0):
            print('The list must not be empty')
            return -1

        for i in range(len(List)):
            if(List[i] == target):
                return i

        return -1


    ########################################################################################################################################################
    # Function Name: orderedLinearSearch
    # Attributes: + self: Searcher instance
    #             + List: ordered list where we want to search (can contain any type of object)
    #             + target: object we want to see whether it is in List or not
    #             + ascending: boolean that tells us if the list is ascending ordered or descending ordered
    #
    # Return:     + int: -1 if the target doesn't appear in List, the index of the first appearance of the target if it does appear in List
    ########################################################################################################################################################
    def orderedLinearSearch(self, List, target, ascending = True):
        if (isinstance(List,(list,tuple,)) == False):
            print('The first attribute should be an ordered list')
            return -1

        if(len(List) <= 0):
            print('The list must not be empty')
            return -1

        for i in range(len(List)):
            #if the list is ascending sorted
            if(ascending == True):
                if(List[i] > target):
                    return -1

                if(List[i] == target):
                    return i
            #If the list is descending sorted
            else:
                if(List[i] < target):
                    return -1

                if(List[i] == target):
                    return i

        return -1


    ########################################################################################################################################################
    # Function Name: jumpSearch (generalized binary to n-ary search; proven sqrt(n) as best size steps)
    # Attributes: + self: Searcher instance
    #             + List: (ascending by default) ordered list where we want to search (can contain any type of object)
    #             + target: object we want to see whether it is in List or not
    #             + jumpSize: size of each jump; it is proven that the most optimal is the default given
    #
    # Return:     + int: -1 if the target doesn't appear in List, the index of target if it does appear in List
    ########################################################################################################################################################
    def jumpSearch(self, List, target, jumpSize = -1):
        if (isinstance(List,(list,tuple,)) == False):
            print('The first attribute should be an ordered list')
            return -1

        if(len(List) <= 0):
            print('The list must not be empty')
            return -1

        if(jumpSize == -1):
            jumpSize = int(floor(sqrt(len(List))))

        #If unsert, we set jumpSize to its most optimal value
        size = len(List)
        if(jumpSize > size):
            jumpSize = size - 1

        #number of intervals previously checked
        count = 0

        searcher = Searcher()

        pointerA = 0
        pointerB = jumpSize

        if((target < List[pointerA]) or (target > List[size-1])):
            return -1

        while(1):
            if((target >= List[pointerA]) and (target <= List[pointerB])):
                ret = searcher.linearSearch(List[pointerA:pointerB+1], target)
                if(ret == -1):
                    return ret
                else:
                    return jumpSize * count + ret
            else:
                count += 1
                pointerA = pointerB
                pointerB = min(pointerB + jumpSize, size-1)


    ########################################################################################################################################################
    # Function Name: interpolationSearch
    # Attributes: + self: Searcher instance
    #             + List: (ascending by default) ordered list where we want to search (can contain any type of object)
    #             + target: object we want to see whether it is in List or not
    #
    # Return:     + int: -1 if the target doesn't appear in List, the index of target if it does appear in List
    ########################################################################################################################################################
    def interpolationSearch(self, List, target):
        if (isinstance(List,(list,tuple,)) == False):
            print('The first attribute should be an ordered list')
            return -1

        if(len(List) <= 0):
            print('The list must not be empty')
            return -1

        pointerA = 0
        pointerB = len(List) - 1

        while(pointerA <= pointerB and target >= List[pointerA] and target <= List[pointerB]):
            if(pointerA == pointerB):
                if(List[pointerA] == target):
                    if(pointerA < 0):
                        return len(List) + pointerA
                    return pointerA
                else:
                    return -1

            else:
                pos = pointerA + int((((float(pointerB - pointerA) / List[pointerB] - List[pointerA])) * (target - List[pointerA])))

                if(List[pos] == target):
                    if(pos < 0):
                        return len(List) + pos
                    return pos

                if(List[pos] < target):
                    pointerA = pos + 1

        return -1

    ########################################################################################################################################################
    # Function Name: exponentialSearch
    # Attributes: + self: Searcher instance
    #             + List: (ascending by default) ordered list where we want to search (can contain any type of object)
    #             + target: object we want to see whether it is in List or not
    #
    # Return:     + int: -1 if the target doesn't appear in List, the index of target if it does appear in List
    ########################################################################################################################################################
    def exponentialSearch(self, List, target):
        if (isinstance(List,(list,tuple,)) == False):
            print('The first attribute should be an ordered list')
            return -1

        if(len(List) <= 0):
            print('The list must not be empty')
            return -1

        s = Searcher()

        if(List[0] == target):
            return target

        #So we can duplicate it, due to that we check index 0 independently
        pointer = 1

        #if element at index pointer is greater than our target, if the target is in the list,
        #it must be in the sublist List[0:pointer] (list considered in ascending order)
        while(pointer < len(List) and List[pointer] <= target):
            pointer = pointer * 2

        #binary search in the found interval
        return s.binarySearch(List[:pointer], target)





if(__name__ == '__main__'):
    s = Searcher()
    L = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610)

    T = []

    print(s.exponentialSearch(T, 6100))
