# kapost-s3transfer
kapost S3transfer Challenge


## Usage
- Since the container isn't hosted in docker hub ( I can do that if needed) you will need to build the container.
1. `git clone https://github.com/KingOtar/kapost-s3transfer.git`
2. `cd kapost-s3transfer`
3. `docker build . -t s3transfer`

- To run the container, you must either use Iam roles to authenticate into AWS to use the buckets or you can provide credentials by passing in environment variables.

 Iamrole: `docker run s3transfer source-bucket destination-bucket --size 5MB`
 
 Env Vars: `docker run -e AWS_ACCESS_KEY_ID=[Key here] -e AWS_SECRET_ACCESS_KEY=[Secret here] s3transfer --size 5MB source-bucket  destination-bucket`


## Thank You
Thank you so much for giving me this opportunity to take this challenge. Please let me know if you have any questions or concerns and I will do my best to assist.


