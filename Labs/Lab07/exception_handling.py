from typing import List
import sys

class CustomException(Exception):
    def __init__(self, number1, number2):
        # compare number 1 and 2, raise an exception if number1 is less than number2
        super().__init__("Exception: number1 is smaller than number2. Can not continue")

def calculate_sqrt(input_num: int):
    # use a try catch block to catch the exception
    # output: "pow() can not be applied to a string"

    x = 0
    try:
        x = input_num**2
    except TypeError as e:
        return "TypeError: pow() can not be applied to a string"
    return x

def divide_numbers(x:int, y:int):
    #use a try catch block here

    try:
        ret_val = x/y
    except ZeroDivisionError:
        return "ZeroDivisionError: cannot divide a number by 0"
    return x / y


def custom_multiplication(x:int, y:int):
    #if x < 0 return a message "(LogicalError: first parameter cannot be a negative number)"
    #raise a ValueError when y < 0 and return the ValueError with the message: (LogicalError: "can not multiply by a negative number")
    try:
        if x < 0:
            return "LogicalError: first parameter cannot be a negative number"
        elif y < 0:
            raise ValueError
    except ValueError:
        print(x*y)
        raise ValueError("LogicalError: second parameter cannot be a negative number")
    return x*y

def return_element(l:List, i:int):
    #if index is out of range, return "IndexError: index is out of range, returning the last element {}.
    #return the last element
    
    try:
        ele = l[i]
    except IndexError:
        print("IndexError: index is out of range, returning the last element {val}.".format(val=l[len(l)-1]))
        return l[len(l)-1]
    return ele

def check_key(mydict:dict, key:int):
    try:
        ret_value = mydict[key]
    except KeyError:
        return "KeyNotFoundError"
    return ret_value

def subtract_numbers(x:int, y:int):
    try:
        if x < y:
            raise CustomException(x, y)
    except CustomException:
        raise CustomException(x, y)
    else:
        return x -y

if __name__=='__main__':
    print("===Exception 1===")
    print(calculate_sqrt(4)) #should print 16
    print(calculate_sqrt('a'))  #should print "TypeError: pow() can not be applied to a string"

    print("===Exception 2===")
    print(divide_numbers(2, 1)) #should print 1
    print(divide_numbers(2,0)) #this should print "ZeroDivisionError: cannot divide a number by 0"

    print("===Exception 3===")
    print(custom_multiplication(2,5)) #should print 10
    print(custom_multiplication(-2, 1)) #should print "CustomError: cannot multiply by negative number"
    try:
       custom_multiplication(2,-1)
    except ValueError as ex:
        if ex.__str__() == "LogicalError: second parameter cannot be a negative number":
            print("We received an expected logical Error")
        else:
            sys.exit(1)

    print("===Exception 4===")
    print(return_element([2,10,3,4], 3)) #should print 4
    print(return_element([2,10,2,4], 4)) #should print "IndexError: index is out of range"

    print("===Exception 5===")
    print(check_key({1:"one", 2:"two", 3:"three"}, 2)) #should print "two"
    print(check_key({1:"one", 2:"two:", 3:"three"}, 4)) #should print "KeyNotFoundError"

    print("===Exception 6===")
    print("Subtracting two values. Result = {}".format(subtract_numbers(4,2)))
    try:
       x = subtract_numbers(2,4)
    except CustomException as ex:
        if ex.__str__() == "Exception: number1 is smaller than number2. Can not continue":
            print("Successfully raised a custom exception")
        else:
            sys.exit(1)