#!/usr/bin/python

# def defines a function
# function header ends with colon
def right_justify(strInput, intRtMargin):
    '''This is a docstring\n
    Right justifies a string 'strInput to a right margin at intRtMargin.'''
    strLen = len(strInput)                     # strLen here is a local variable to the function
                                            # len() is a function to get the length of a string
    # print 70 minus the length of strInput and then concatenate inStr to it
    print(" " * ( intRtMargin - strLen )  + strInput)
    # end of a function is indicated by untabbing back to previous level
# <-- over here

intMargin = 80

right_justify("Do or do not,", intMargin)
right_justify("There is no try", intMargin)
right_justify("-- Yoda", intMargin)



