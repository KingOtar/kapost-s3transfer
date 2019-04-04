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
import os
import boto3

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
    
    size_limit = humanfriendly.parse_size(args.size);

    conn = boto3.client('s3')

    #loop through bucket objects
    for obj in conn.list_objects(Bucket=bucket1)['Contents']:
        key = obj['Key']
        size = obj['Size']

        # check size and if larger than provided size, copy to bucket2
        if size > size_limit:
            copy_source = {
                'Bucket': bucket1,
                'Key': key
            }
            conn.copy(copy_source, bucket2, key)
    

if __name__ == '__main__':
    arguments = parse_arguments()
    main(arguments)
