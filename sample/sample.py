'''
    Workbook class holds any and all operations on a workbook that may affect calculated cell
'''

# Standard imports
from typing import List, Dict, Optional, Tuple, Any, TextIO
import json

# Local package imports
from .other import Other

# If you are unfamiliar with Python 3 type annotations, see the Python standard
# library documentation for the typing module here:
#
#     https://docs.python.org/3/library/typing.html

class Sample:
    '''
    Sample class for doing stuff
    '''

    def __init__(self):
        '''
        Initialize new workbook
        '''
        self.other_object = Other()
        self.dummy_value = ['dummy', 'value']


    def get_dummy_value(self) -> List[str]:
        '''
        Return dummy value
        '''
        return self.dummy_value
    
    def get_odds_and_evens(self) -> Tuple[List[int], List[int]]:
        '''
        Gets list of odds and events
        '''
        y = []
        x = []
        for i in range(1000000):
            if i % 2 == 0:
                x.append(i)
            else:
                y.append(i)
        return (x,y)
