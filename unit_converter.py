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
        print(f'{num}ft in inches = {in_output}in')
    else:
        ft_output = num/12
        print(f'{num}inches in feet = {ft_output}feet')


def Kilogram_gram(num ,g):
    
    '''
    This is a method that converts from kilograms to Grams and otherwise
    
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
        print(f'{num} in minutes = {m_output}m')


def metres_miles(num ,mi):
    
    '''
    This is a method that converts from metres to miles and otherwise
    
    arg::
        num: float
        m: bool
    '''
    
    assert type(num) == float or type(num) == int, f"{num} is not a floating point argument"
    assert type(mi) == bool, f"{mi} is not a boolean object"
    
    if mi:
        mi_output = num*0.000621371
        print(f'{num} in miles = {mi_output}mi')
    else:
        m_output = num/0.000621371
        print(f'{num} in metres = {m_output}m')


def metres_yard(num ,yd):
    
    '''
    This is a method that converts from metres to yards and otherwise
    
    arg::
        num: float
        yd: bool
    '''
    
    assert type(num) == float or type(num) == int, f"{num} is not a floating point argument"
    assert type(yd) == bool, f"{yd} is not a boolean object"
    
    if yd:
        yd_output = num*1.09361
        print(f'{num} in yards = {yd_output}yd')
    else:
        m_output = num/1.09361
        print(f'{num} in metres = {m_output}m')


def metres_feet(num ,ft):
    
    '''
    This is a method that converts from metres to feet and otherwise
    
    arg::
        num: float
        ft: bool
    '''
    
    assert type(num) == float or type(num) == int, f"{num} is not a floating point argument"
    assert type(ft) == bool, f"{ft} is not a boolean object"
    
    if ft:
        ft_output = num*3.28084
        print(f'{num} in feet = {ft_output}ft')
    else:
        m_output = num/3.28084
        print(f'{num} in metres = {m_output}m')


def gram_ounce(num ,ounce):
    
    '''
    This is a method that converts from grams to ounces and otherwise
    
    arg::
        num: float
        ounce: bool
    '''
    
    assert type(num) == float or type(num) == int, f"{num} is not a floating point argument"
    assert type(ounce) == bool, f"{ounce} is not a boolean object"
    
    if ounce:
        ounce_output = num*0.035274
        print(f'{num} in ounces = {ounce_output}ounces')
    else:
        g_output = num/0.035274
        print(f'{num} in grams = {g_output}g')


def Kilogram_pound(num ,pd):
    
    '''
    This is a method that converts from kilograms to pounds and otherwise
    
    arg::
        num: float
        pd: bool
    '''
    
    assert type(num) == float or type(num) == int, f"{num} is not a floating point argument"
    assert type(pd) == bool, f"{pd} is not a boolean object"
    
    if pd:
        pd_output = num*2.20462
        print(f'{num} in pounds = {pd_output}pd')
    else:
        kg_output = num/2.20462
        print(f'{num} in kilograms = {kg_output}kg')