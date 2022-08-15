def metres_centimetres(num ,cm):
    
    '''
    This is a method that converts from metres to centimetres and otherwise
    
    arg::
        num: float
        cm: bool
    '''
    
    assert type(num) == float or type(num) == int, f"{num} is not a floating point argument"
    assert type(cm) == bool, f"{cm} is not a boolean object"
    
    if cm:
        cm_output = num*100
        print(f'{num} in centimetres = {cm_output}cm')
    else:
        m_output = num/100
        print(f'{num} in metres = {m_output}')

def feet_inches(num ,_in):
    
    '''
    This is a method that converts from feet to inches and otherwise
    
    arg::
        num: float
        in: bool
    '''
    
    assert type(num) == float or type(num) == int, f"{num} is not a floating point argument"
    assert type(_in) == bool, f"{_in} is not a boolean object"
    
    if _in:
        in_output = num*12
        print(f'{num} in inches = {in_output}_in')
    else:
        ft_output = num/12
        print(f'{num} in feet = {ft_output}')


def Kilogram_gram(num ,g):
    
    '''
    This is a method that converts from Grams to Kilograms and otherwise
    
    arg::
        num: float
        g: bool
    '''
    
    assert type(num) == float or type(num) == int, f"{num} is not a floating point argument"
    assert type(g) == bool, f"{g} is not a boolean object"
    
    if g:
        g_output = num*1000
        print(f'{num} in grams = {g_output}g')
    else:
        kg_output = num/1000
        print(f'{num} in Kilograms = {kg_output}kg')


def Litres_millilitres(num ,ml):
    
    '''
    This is a method that converts from Litres to Millilitres and otherwise
    
    arg::
        num: float
        ml: bool
    '''
    
    assert type(num) == float or type(num) == int, f"{num} is not a floating point argument"
    assert type(ml) == bool, f"{ml} is not a boolean object"
    
    if ml:
        ml_output = num*1000
        print(f'{num} in millilitres = {ml_output}ml')
    else:
        L_output = num/1000
        print(f'{num} in Litres = {L_output}L')


def Minutes_seconds(num ,s):
    
    '''
    This is a method that converts from Minutes to seconds and otherwise
    
    arg::
        num: float
        s: bool
    '''
    
    assert type(num) == float or type(num) == int, f"{num} is not a floating point argument"
    assert type(s) == bool, f"{s} is not a boolean object"
    
    if s:
        s_output = num*60
        print(f'{num} in seconds = {s_output}s')
    else:
        m_output = num/60
        print(f'{num} in feet = {m_output}m')