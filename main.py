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
import humanfriendly

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', "--size",  help='Use size units accordingly. ex. 5MB, 200GB 1TB', required=True)
    parser.add_argument('bucket1', action="store")
    parser.add_argument('bucket2', action="store")
    args = parser.parse_args()
    return args

def main(args):
    # Make it easier to read the args passed to script. All required by argparse
    bucket1 = args.bucket1
    bucket2= args.bucket2
    
    size = num_bytes = humanfriendly.parse_size(args.size);
    print(size)

if __name__ == '__main__':
    arguments = parse_arguments()
    main(arguments)
