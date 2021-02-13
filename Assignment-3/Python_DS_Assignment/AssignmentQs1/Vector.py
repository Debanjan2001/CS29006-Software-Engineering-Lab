# In this python file, only the definations for the magic functions and the basic operations
# for the question segments are provided. There may be the need to add new functions or overload 
# existing ones as per the question requirements.

class Vector:
        
    def __init__(self, *args): 
        
        # if arg is an int(dimension)
        if isinstance(args[0], int): 
            self._coords = [0]*args[0]
        else:
            self._coords = []
            user_iterable = args[0]
            for item in user_iterable:
                self._coords.append(item)

    def __len__(self):
        # return the dimension of the vector
        return len(self._coords)

    def __getitem__(self, j):
        # return the jth coordinate of the vector
        return self._coords[j]

    def __setitem__(self, j, val):
        # set the jth coordinate of vector to val
        self._coords[j] = val

    def __add__(self, other):
        # u + v
        result = []
        for index in range(len(self)):
            result.append(self[index]+other[index])

        return result
            
    def __eq__(self, other):
        # return True if vector has same coordinates as other
        if len(self)!= len(other):
            return False
        
        for index in range(len(self)):
            if self[index]!=other[index]:
                return False

        return True

    def __ne__(self, other):
        # return True if vector differs from other
        return not self==other


    def __str__(self):
        # return the string representation of a vector within <>
        printable = "<"
        for index in range(len(self)):
            if index != len(self)-1 :
                printable += str(self[index])+", "
            else:
                printable += str(self[index])+">" 

        return printable

    def __sub__(self, other):
        # Soln for Qs. 2
        result = []
        for index in range(len(self)):
            result.append(self[index]-other[index])

        return result
        
    def __neg__(self):
        # Soln for Qs. 3
        result = []
        for index in range(len(self)):
            result.append(self[index]*(-1))

        return result

    def __rmul__(self, value):
        return (self * value) 
    
    def __mul__(self, other):
        # Soln for Qs. 4, 5 and 6
        result = []

        if isinstance(other,int):
            for index in range(len(self)):
                result.append(self[index]*other)

        else:
            for index in range(len(self)):
                result.append(self[index]*other[index])

        return result


    
def main():
    v1 = Vector(5)
    print(v1)
    # v2 = Vector (7)
    v3 = Vector([1,2,3,4,5])
    v4 = Vector([1,2,3,4,5])
    # print(v4)

    # Add suitable print statements to display the results
    # of the different question segments


if __name__ == '__main__':
    main()