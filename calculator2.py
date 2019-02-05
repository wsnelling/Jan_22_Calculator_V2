"""
A calculator library
"""
def add(*args):
    """
    add() Returns the sum of n-parameters
    """
    answer = 0  #This iniitalizes a starting value of zero
    for value in args: #Instructs the code to iterate over each param value
        answer += value  #Adds each parameter value to the total
    return answer
    # note that there is a sum function that does this
    #built into python - we just invented our own
    #you could swap the above out (all below the def)
    #and just put in the following below it
    # sum(args)

def subtract(*args):
    """" this is the functional docstring for the subtract function """
    answer = 0
    for value in args:
        answer -= value #subtracts each parameter value to arrive at a total
    return answer

def multiply(*args):
    """" this is the functional docstring for the multiply function """
    list_args = list(args)
    count_len = len(list_args)
    count_args = int(count_len)
    if not list(args):
        answer = IndexError #if nothing in the list an error is returned
    elif count_args < 2:
        answer = IndexError #if not enough args in the list; return an error
    else:
        answer = 1
        for value in args:
            answer *= value #multiplies each parameter value to get a total
    return answer

def divide(*args):
    """ This is the doc string for the divide function"""
    list_args = list(args) #create a list of the tuple of variables
    count_len = len(list_args) #determines the number of arguments presented
    count_args = int(count_len) #turns the number of args into an integer
    if not list(args): #checks if there is anything in the list
        answer = IndexError #if nothing in the list an error is returned
    elif count_args < 2: #checks enough args were presented to do division
        answer = IndexError #if not enough args in the list; return an error
    else:
        try:
            """
            In order to perform division on a variable number of arguments
            we need to coax out the first variable as the start value for the
            list of items we will perform division of. The trick to doing
            this is to create a list from the tuple of arguments so that this
            initial value can be extracted. Upon extraction the value is squared
            and this becomes the start value for iterating through the list of
            arguments to obtain the answer. Why squared? This is done so that upon
            the first iteration of division, the squared starting number is reduced
            to it's actual initial value in the sequence.
            """
            alist = list(args)
            answer1 = alist[0] #extract the first item of variables
            answer = answer1**2 #squares up the first variableitem
            for value in args:
                answer /= value #use answer2 as the first dividend in the
                # sequence of divisions that run through the presented
                # variables. For example if the first item was 10,
                # answer2 = 100/10 to give 10, then the divisions continue
                # through any remaining variables
        except ZeroDivisionError:
            answer = ZeroDivisionError
    return answer
