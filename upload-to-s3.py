import boto3

bucket_name = 'cloud-data-lab-34 '
s3 = boto3.client('s3')

s3.upload_file('nbu_2025.csv', bucket_name, 'nbu_2025.csv')
print("Файл успішно вивантажено на S3")