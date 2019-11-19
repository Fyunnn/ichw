# currency.py
# Fu Jin Yu (pkuid: 1900011813)
# November 19, 2019

# 作者老老实实按照Cornell大学的作业指导，从而出现了很多无用的函数，比如 get_from 

"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange. Bseides, this file
contants several tests for testing the primary module."""

def before_space(s):
    """Returns: Substring of s; up to, but not including, the first space 
    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    return s.split(" ", 1)[0]

def after_space(s):
    """Returns: Substring of s after the first space 
    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    return s.rsplit(" ", 1)[1]

def first_inside_double_quotes(s):
    """Returns: The first substring of s between two (double) quote characters 
    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote 
    characters inside"""
    a=s.split('"', 1)[1]
    return a.split('"', 1)[0]

def get_from(json):
    """Returns: The FROM value in the response to a currency query
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    a=json.split('"src"', 1)[1]
    return first_inside_double_quotes(a)

def get_to(json):
    """Returns: The TO value in the response to a currency query
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    a=json.split('"dst"', 1)[1]
    return first_inside_double_quotes(a)

def has_error(json):
    """Returns: True if the query has an error; False otherwise
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    return json.find("true")==-1

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    url="http://cs1110.cs.cornell.edu/2018fa/a1server.php?from="+currency_from+"&to="+currency_to+"&amt="+str(amount_from)
    from urllib.request import urlopen
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return float(before_space(get_to(jstr)))

def iscurrency(currency):
    """Returns: True if currency is a valid (3 letter code for a) currency. 
    It returns False otherwise.
    Parameter currency: the currency code to verify
    Precondition: currency is a string."""
    url="http://cs1110.cs.cornell.edu/2018fa/a1server.php?from="+currency+"&to="+"USD"+"&amt="+"1"
    from urllib.request import urlopen
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return not has_error(jstr)





"""Test module for the module for currency exchange

When run as a script, this module invokes several procedures that 
test the various functions in the module above."""

def test_before_space():
    """test before_space function"""
    assert(before_space("hello world") == "hello")
    
def test_after_space():
    """test after_space function"""
    assert(after_space("hello world") == "world")

def test_first_inside_double_quotes():
    """test first_inside_double_quotes function"""
    assert(first_inside_double_quotes('''A B "C" D "E" F G''')=="C")

def test_get_from():
    """test get_from function"""
    assert(get_from('this "src" is far "beyond" ours')=="beyond")
    
def test_get_to():
    """test get_to function"""
    assert(get_to('this "dst" is far "beyond" ours')=="beyond")

def test_has_error():
    """test has_error function"""
    assert(has_error('''{ "src" : "", "dst" : "", "valid" : false, "error" : 
        "Exchange currency code is invalid." }''')==True)
    assert(has_error('''{ "src" : "2.5 United States Dollars", "dst" : 
        "2.2160175 Euros", "valid" : true, "error" : "" }''')==False)

def test_exchange():
    """test exchange function"""
    assert(exchange("USD" , "EUR" , 2.5)==2.2160175)
    
def test_iscurrency():    
    """test iscurrency function"""
    assert(iscurrency("USD")==True)
    assert(iscurrency("US")==False)

def testAll():
    """test all cases"""
    test_before_space()
    test_after_space()
    test_first_inside_double_quotes()
    test_get_from()
    test_get_to()
    test_has_error()
    test_exchange()
    test_iscurrency()
    print("All tests passed")
    
    

def main():
    """main module"""
    testAll()

if __name__ == '__main__':
    main()
