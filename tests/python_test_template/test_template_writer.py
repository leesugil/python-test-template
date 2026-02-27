
from python_test_template import template_writer

def test_compose_path():
    cases = [
                {
                'args': {
                    'module': ,
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
                    'module': ,
                    'functions': ,
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
                    'target_modules': ,
                    'target_functions': ,
                    'target_dest': ,
                    },
                'expected': ,
                },
            ]

    for case in cases:
        assert template_writer.generate_template(case['args']) == case['expected']

