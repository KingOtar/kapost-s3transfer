FROM python
COPY . /kapost-s3transfer
RUN ["pip","install","humanfriendly", "boto3"]

ENTRYPOINT ["/kapost-s3transfer/main.py"]

