
from python_test_template import dummy

def test_dummy_function():
    cases = [
                {
                'args': {
                    #arg1: str='example', arg2: str='ex,.:', arg3: str="don't do this", arg4=False
                    },
                #list[dict]
                'expected': ,
                },
            ]

    for case in cases:
        assert dummy.dummy_function(case['args']) == case['expected']

