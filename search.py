from math import floor

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
        if (isinstance(List,(list,)) == False):
            return 'The first attribute should be an ordered list'

        pointerA = 0
        pointerB = len(List) - 1
        stop = -1

        while(1):
            if(List[pointerA] == target):
                return pointerA

            elif(List[pointerB] == target):
                return pointerB

            else:
                pointerC = floor((pointerA + pointerB)/2)

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


if(__name__ == '__main__'):
    s = Searcher()
    L = [9, 8, 4, 2]

    print(s.binarySearch(L, 8, ascending=False))
    
