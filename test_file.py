from recursion import string_reverse
import pytest



def test_string_reverse():
    # rvrsdStr = recursion.string_reverse(str('reversal'))
    # print(rvrsdStr,'print')
    assert string_reverse(str('helvin')) == str('nivleh')
    

