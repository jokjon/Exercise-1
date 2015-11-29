# Copyright (c) 2015,Vienna University of Technology,
# Department of Geodesy and Geoinformation
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Vienna University of Technology,
#      Department of Geodesy and Geoinformation nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL VIENNA UNIVERSITY OF TECHNOLOGY,
# DEPARTMENT OF GEODESY AND GEOINFORMATION BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
In this module you will define several functions.

Please document your functions according to
https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
'''

# Example so that you can see a passing test


def f():
    """Returns the string 'success'
    """
    return "success"

##############################
# Basic function definitions #
##############################

# Define a function named add that takes two numbers and returns the sum.
def add(x, y):
    '''
    :param x: term 1
    :param y: term 2
    :return: the value of the terms x+y
    '''
    return x+y


# Define a function named to_tuple that takes three arguments and returns a
# tuple of these three arguments.
def to_tuple(x, y, z):
    '''
    :param x: argument 1
    :param y: argument 2
    :param z: argument 3
    :return: a tuple of with three arguments.
    '''
    return x, y, z


# Define a function named check5 that checks if a number is greater than 5 and
# returns True or False.
def check5(x):
    '''
    :param x: number to check
    :return: check number if it greater than 5
    '''
    return x > 5


# Define a function named check_n that check is a number is greater than n. The
# number should be the first argument and n the second
def check_n(x, n):
    '''
    :param x: number to check
    :param n: comparing number
    :return: check number if it greater than n
    '''
    return x > n

#########
# LISTS #
#########

# Define a function named check_list that takes two arguments. The first
# argument is a list of numbers and the second argument is the number n to
# compare against. The function should return a list with equal length as the
# input list containing for each number in the original list either True or
# False if the number was greater than or equal to n.
def check_list(l, n):
    '''
    :param l: list of numbers
    :param n: comparing number
    :return: check each number of l if it greater than n
    '''
    r = []
    for e in l:
        r.append(e >= n)
    return r


# Define a function named check_list_nth that does the same as check_list but
# uses every nth element of the input list (including the first one). You will
# need a third input argument.
def check_list_nth(l, n, i):
    '''
    :param l: list of number
    :param n: comparing number
    :param i: step size
    :return: check each number of l with the step size if it greater than n
    '''
    r = []
    for e in l[::i]:
        r.append(e >= n)
    return r


# Define a function named add_new_list that takes two inputs. A list l and a
# second variable x to add to the list. Return a new list containing x as the
# last element without modifying the original list.
def add_new_list(l, x):
    '''
    :param l: list with objects
    :param x: object to add on the end of the list
    :return: a copy of the list with param x added on the end
    '''
    r = l.copy()
    r.append(x)
    return r

# Define a function named remove_nth that takes a list and removes every nth
# element (including the first one). Use a keyword named nth to set the default
# value for nth to 2.
def remove_nth(l, nth = 2):
    '''
    :param l: list with objects
    :param nth: step size
    :return: a copy of the list without the first and the nth elements
    '''
    r = l.copy()
    del r[::nth]
    return r


# Define a function named search_n that takes a list and a variable x and
# searches for x in the list. If the variable is found return the index of the
# variable in the list and the variable. Otherwise use None for both return
# values
def search_n(l, x):
    '''
    :param l: list with objects
    :param x: searched object
    :return: the index of the variable in the list and the variable
    '''
    for idx, val in enumerate(l):
        if val == x:
            return idx, val
    return None, None


################
# Dictionaries #
################

# Define a function named args_to_dict that takes three arguments and returns a
# dictionary with the position of the argument as the key (starting at 0) and
# the argument as the value.
def args_to_dict(x, y, z):
    '''
    :param x: object 1
    :param y: object 2
    :param z: object 3
    :return: dictionary with the params
    '''
    return {0: x, 1: y, 2: z}


# BONUS: Write a function named args_to_dict_general that does the same for any
# number of arguments
def args_to_dict_general(*l):
    '''
    :param l: list of objects
    :return: dictionary with the params and index as id
    '''
    r = {}
    i = 0
    for e in l:
        r[i] = e
        i += 1
    return r


# Define a function named lists_to_dict that takes two lists of equal lenght
# named keys and values and builds a dictionary out of them.
def lists_to_dict(ln, lv):
    '''
    :param ln: list with keys
    :param lv: list with values
    :return: merge key and value lists
    '''
    return dict(zip(ln, lv))


# Define a function named search_list that takes two lists a and b. The
# function searches for all elements of b in list a. The return value should be
# a dictionary containing the index of the found element of b in list a and the
# value of the found element. If nothing was found then return an empty
# dictionary.
def search_list(a, b):
    '''
    :param a: list
    :param b: list with searched objects
    :return: dictionary with index of a as key and the found object as value
    '''
    r = {}
    for i, e in enumerate(a):
        if e in b:
            r[i] = e
    return r


# Define a function named dict_to_string that takes a dictionary and a
# separator string. The function should only take elements out of the
# dictionary whose value is a string and then return a single string containing
# the strings stored in the dictionary seperated by the separator string.
# Return an empty string if there are no strings in the dictionary.
def dict_to_string(d, s):
    '''
    :param d: dictionary
    :param s: separator
    :return: string with the dictionary value (if the value a string) separated by the separator
    '''
    r = '';
    for v in d.values():
        if isinstance(v, str):
            r += v + s
    return r[:-1]


# Define a function named classify_by_type which takes a list l and returns a
# dictionary d. The d must have the keys 'int' and 'str' which contain the
# elements out of l that have this type. Elements that do not fit one of these
# two types should be stored in a list under the key 'others'
def classify_by_type(l):
    '''
    :param l: list with objects
    :return: dictionary with the keys :"str", "int", and "others" and as the value the sorted object
    '''
    s = []
    i = []
    o = []
    for e in l:
        if isinstance(e, int):
            i.append(e)
        elif isinstance(e, str):
            s.append(e)
        else:
            o.append(e)
    return {'str': s, 'int': i, 'others': o}
