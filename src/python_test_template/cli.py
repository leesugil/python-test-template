#!/usr/bin/env python3
import argparse

from . import parse_paths
from . import template_writer

def main():
    # Define possible arguments
    parser = argparse.ArgumentParser(description="Writing functions are fun, writing test files for those functions are boring. This helps that.")
    parser.add_argument("destination_subfolder", default='tests', help="Destination subfolder where test_*.py files will be stored. Default is 'tests'.")
    parser.add_argument("--src", type=str, default='src', help="src path.")
    parser.add_argument("--package", type=str, default='*', help="To isolate the process to a specific package name.")
    parser.add_argument("--module", type=str, default='*', help="To isolate the process to a specific module name.")
    #parser.add_argument("--class", type=str, default='*', help="To isolate the process to a specific class name.")
    parser.add_argument("--function", action='append', type=str, default='*', help="To isolate the process to a specific function name.")
    # Debug
    parser.add_argument("--debug", action="store_true", help="DEBUG MODE")

    args = parser.parse_args()

    target_modules = parse_paths.get_target_modules(src=args.src, package=args.package, module=args.module)
    template_writer.generate_template(target_modules=target_modules, target_functions=args.function)


if __name__ == "__main__":
    main()
