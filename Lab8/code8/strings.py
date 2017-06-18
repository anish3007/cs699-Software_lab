def locate (substr, str):
    # returns index where the substring occurs first, if not found, return -1
    return str.find(substr)
def count (substr, str):
    # passreturns how many times the substring occurs in str
    return str.count(substr)
def remove (substr, str):
    # removes the first occurance of the substring from the string, if it is present
    return str.replace(substr,"",1)
def replace (substr, newsubstr, str): 
    # replaces the first occurance of the substring with the new substring inside the given string
    return str.replace(substr,newsubstr,1)
def removeAll (substr, str):
    # removes all occurences of the substring one by one. Use function 3 above.
    # return str.replace(substr,"")
    for i in range(count(substr, str)):
        str=remove(substr, str)
    return str
def replaceAll (substr, newsubstr, str):
    # replaces all occurences one by one. Use function 5 above
    #return str.replace(substr,newsubstr)
    for i in range(count(substr, str)):
        str=replace(substr, newsubstr, str)
    return str
