
from python_test_template import parse_code

def test_parse_args():
    cases = [
                {
                'args': {
                    'args': ,
                    },
                'expected': ,
                },
            ]

    for case in cases:
        assert parse_code.parse_args(case['args']) == case['expected']

def test_parse_return():
    cases = [
                {
                'args': {
                    'return_obj': ,
                    },
                'expected': ,
                },
            ]

    for case in cases:
        assert parse_code.parse_return(case['args']) == case['expected']

def test_parse_functions():
    cases = [
                {
                'args': {
                    'filepath': ,
                    'target_functions': ,
                    },
                'expected': ,
                },
            ]

    for case in cases:
        assert parse_code.parse_functions(case['args']) == case['expected']

