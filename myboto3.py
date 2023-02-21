import boto3

# sts example
# sts = boto3.client('sts')
# response = sts.get_caller_identity()
# user = response['UserId']
# account = response['Account']
# print(f'Hello you are logged in as user {user} to account {account}')

# s3 = boto3.client('s3')
# mybucketname = 'sena-0001'

# try:
#     response = s3.create_bucket(
#         Bucket=mybucketname,
#     )
#     location = response['Location']
#     print(f'Your bucket was created here: {location}')

# except:
#     print(f'An error occurred creating your bucket')

# s3 = boto3.client('s3')
# mybucketname = 'sena-0001'

# try:
#     response = s3.delete_bucket(
#         Bucket=mybucketname
#     )
    
# except:
#     print(f'An error occurred deleting your bucket')