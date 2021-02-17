# In this python file, only the definations for the magic functions and the basic operations
# for the question segments are provided. There may be the need to add new functions or overload 
# existing ones as per the question requirements.

class Vector:
        
    def __init__(self, *args): 
        
        # if arg is an int(dimension)
        if isinstance(args[0], int): 
            self._coords = [0]*args[0]
        elif isinstance(args[0],list) or isinstance(args[0],tuple):
            self._coords = []
            user_iterable = args[0]
            for item in user_iterable:
                self._coords.append(item)
        else:
            raise Exception("Wrong data type passed to class constructor. Not a list or tuple ot integer.")

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
        if len(self)!=len(other):
                raise Exception("Dimension Mismatch.Two vectors being added don't have the same dimension.")

        result = Vector(len(self))   

        for index in range(len(self)):
            result[index] = (self[index]+other[index])

        return result
            
    def __eq__(self, other):
        # return True if vector has same coordinates as other
        if len(self)!=len(other):
                raise Exception("Dimension Mismatch.Two vectors being compared don't have the same dimension.")

        for index in range(len(self)):
            if self[index]!=other[index]:
                return False

        return True

    def __ne__(self, other):
        # return True if vector differs from other
        if len(self)!=len(other):
                raise Exception("Dimension Mismatch.Two vectors being compared don't have the same dimension.")

        for index in range(len(self)):
            if self[index]!=other[index]:
                return True
        return False


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
        if len(self)!=len(other):
                raise Exception("Dimension Mismatch.Two vectors being subtracted don't have the same dimension.")

        result = Vector(len(self))

        for index in range(len(self)):
            result[index] = (self[index]-other[index])

        return result
        
    def __neg__(self):
        # Soln for Qs. 3
        
        result = Vector(len(self))

        for index in range(len(self)):
            result[index] = (self[index]*(-1))

        return result

    def __rmul__(self, value):
        return (self * value) 
    
    def __mul__(self, other):
        # Soln for Qs. 4, 5 and 6
        
        if isinstance(other,int):
            result = Vector(len(self))
            for index in range(len(self)):
                result[index]=(self[index]*other)

            return result

        elif isinstance(other,Vector):
            if len(self)!=len(other):
                raise Exception("Dimension Mismatch.Two vectors being multiplied don't have the same dimension.")
            result = 0
            for index in range(len(self)):
                result += (self[index]*other[index])
            return result
        else:
            raise Exception("Invalid Operand Types found during multiplication.")


    
def main():
    # Add suitable print statements to display the results
    # of the different question segments
    v1 = Vector(5)

    print("*** TEST FOR __str__ ***")
    print("v1 = {}".format(v1))
    print()

    print("*** TEST FOR __len__ ***")
    print("v1 = {}".format(v1))
    print("Dimension of v1 = {}".format(len(v1)))
    print()

    print("*** TEST FOR __setitem__ ***")
    v1[3] = 4
    print("Set 3rd co-ordinate v1[3]=4")
    print("Now,v1 = {}".format(v1))
    print()

    print("*** TEST FOR __getitem__ ***")
    print("getting 3rd co-ordinate : {}".format(v1[3]))
    print()

    print("*** TEST FOR PASSING ITERABLE TO CONSTRUCTOR ***")
    v1 = Vector([1,2,3,4,5])
    print("v1 = Vector([1,2,3,4,5])")
    print("v1 = {}".format(v1))
    print()
    
    print("*** TEST FOR __add__ ***")
    v2 = Vector([2,2,2,2,2])
    print("v1 = {}".format(v1))
    print("v2 = {}".format(v2))
    print("v1 + v2 = {}".format(v1+v2) )
    print()

    print("*** TEST FOR __eq__ ***")
    v2 = Vector((1,2,3,4,6))
    print("v1 = {}".format(v1))
    print("v2 = {}".format(v2))
    print("v1==v2 : {}".format(v1==v2))
    print()

    print("*** TEST FOR __ne__ ***")
    print("v1 = {}".format(v1))
    print("v2 = {}".format(v2))
    print("v1!=v2 : {}".format(v1!=v2))
    print()

    print("*** TEST FOR __sub__ ***")
    v1 = Vector([1,2,3,4,5])
    v2 = Vector([1,1,1,1,1])
    print("v1 = {}".format(v1))
    print("v2 = {}".format(v2))
    print("v1-v2 = {}".format(v1-v2))
    print()

    print("*** TEST FOR __neg__ ***")
    print("v1 = {}".format(v1))
    print("-v1 = {}".format(-v1))
    print()

    print("*** TEST FOR __mul__ ***")
    print("v1 = {}".format(v1))
    print("v1*3 = {}".format(v1*3))
    print()

    print("*** TEST FOR __rmul__ ***")
    print("v1 = {}".format(v1))
    print("4*v1 = {}".format(4*v1))
    print()

    print("*** TEST FOR __mul__ ***")
    print("v1 = {}".format(v1))
    v2 = Vector([1,0,1,0,1])
    print("v2 = {}".format(v2))
    print("v1*v2 = {}".format(v1*v2))
    print()


if __name__ == '__main__':
    main()