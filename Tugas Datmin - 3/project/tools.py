def listToString(array):
    msg="[ "
    for x in array:
        msg=msg+str(x)+", "
    msg=msg+" ]"
    return msg