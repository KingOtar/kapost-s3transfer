#!/usr/bin/env python3
"""
Project for kapost s3 file transfer challange
Refer to README for usage.
"""

__author__ = "Samuel Lightsey"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', "--size",  help='Use parsable size units according to "man units"')
    parser.add_argument('bucket1', action="store")
    parser.add_argument('bucket2', action="store")
    args = parser.parse_args()
    return args

def main():
    print("hello world")

if __name__ == '__main__':
    arguments = parse_arguments()
    main(*arguments)
