
from python_test_template import template_writer

def test_compose_path():
    cases = [
                {
                'args': {
                    #module: dict
                    },
                'expected': ,
                },
            ]

    for case in cases:
        assert template_writer.compose_path(case['args']) == case['expected']

def test_case_and_test_statement():
    cases = [
                {
                'args': {
                    #function, module
                    },
                'expected': ,
                },
            ]

    for case in cases:
        assert template_writer.case_and_test_statement(case['args']) == case['expected']

def test_case_list():
    cases = [
                {
                'args': {
                    #args
                    },
                'expected': ,
                },
            ]

    for case in cases:
        assert template_writer.case_list(case['args']) == case['expected']

def test_compose_template():
    cases = [
                {
                'args': {
                    #module: str, functions: list[dict]
                    },
                'expected': ,
                },
            ]

    for case in cases:
        assert template_writer.compose_template(case['args']) == case['expected']

def test_generate_template():
    cases = [
                {
                'args': {
                    #target_modules: list[str], target_functions: list[str], target_dest: str='.', debug=False
                    },
                'expected': ,
                },
            ]

    for case in cases:
        assert template_writer.generate_template(case['args']) == case['expected']

