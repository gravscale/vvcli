# import boto3
# import os
# import urllib3
# from botocore.config import Config
# from botocore.exceptions import UnknownSignatureVersionError

# # Ignore InsecureRequestWarning
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# def get_api_s3():
#     """
#     Initialize and return the S3 client.
#     """
#     host = os.getenv("OBJ_HOST", "https://obj-sp1.envvs.io")
#     access_key = os.getenv("AWS_ACCESS_KEY")
#     secret_key = os.getenv("AWS_SECRET_KEY")
#     secure = os.getenv("OBJ_SECURE", "True").lower() == "true"
#     signature_version = os.getenv("OBJ_SIGNATURE_VERSION", "s3")  # Default to s3v4
#     #signature_version = os.getenv("OBJ_SIGNATURE_VERSION", "s3v4")  # Default to s3v4


#     try:
#         # Configurações para o cliente boto3
#         config = Config(signature_version=signature_version)
#         return boto3.client(
#             "s3",
#             endpoint_url=host,
#             aws_access_key_id=access_key,
#             aws_secret_access_key=secret_key,
#             #region_name="us-east-1",
#             #region_name="default",
#             #region_name=None,
#             config=config,
#             verify=secure,
#         )
#     except UnknownSignatureVersionError:
#         raise ValueError(f"Unknown Signature Version: {signature_version}. Please use 's3' or 's3v4'.")
import boto3
import os
import urllib3
from botocore.config import Config

# Ignore InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_api_s3():
    """
    Initialize and return the S3 client with path-style addressing.
    """
    host = os.getenv("OBJ_HOST", "https://obj-sp1.envvs.io")
    access_key = os.getenv("AWS_ACCESS_KEY")
    secret_key = os.getenv("AWS_SECRET_KEY")
    secure = os.getenv("OBJ_SECURE", "False").lower() == "true"
    signature_version = os.getenv("OBJ_SIGNATURE_VERSION", "s3")  # Default to s3v4

    # Configuração do boto3 para usar path-style
    config = Config(
        signature_version=signature_version,
        s3={"addressing_style": "path"}  # Força path-style
    )
    return boto3.client(
        "s3",
        endpoint_url=host,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=config,
        verify=secure,
    )
