from codereview import __version__

from codereview.insert_shift_array import insert_shift_array


def test_version():
    assert __version__ == '0.1.0'


def test_list_with_even_length():
    list = [2,4,6,-8]
    insert_shift_array(list,5)
    assert list == [2,4,5,6,-8]


def test_list_with_odd_length():
    list = [42,8,15,23,42] 
    insert_shift_array(list,16)  
    assert list == [42,8,15,16,23,42]

def test_Empty_List():
    list = []
    insert_shift_array(list,10)  
    assert list ==[10]  