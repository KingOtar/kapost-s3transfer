FROM python
COPY . /kapost-s3transfer
CMD pip install humanreadable boto3

ENTRYPOINT ["/kapost-s3transfer/main.py"]
