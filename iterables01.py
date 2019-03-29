def steady(value=1):
    '''Returns an iterator that produces value indefinitely.
    HISTORY: 2018--5-14: changed sentinel from None to NoMore;
    2018-04-11: was generator that yielded x indefinitely.'''
    return iter(constant(value), NoMore)

