from enum import Enum


class EnumObjectStoragePrintableAttributes(str, Enum):
    CLIENT_ID = "Client ID"
    EMAIL = "E-mail"
    PASSWORD = "Password"
    API_TOKEN = "Auth Token"
    ACCESS = "Access"
    DISPLAY_NAME = "Display Name"
    QUOTA = "Quota"


class EnumQuotaSize(int, Enum):
    SIZE_10GB = 10
    SIZE_25GB = 25
    SIZE_50GB = 50
    SIZE_100GB = 100
    SIZE_250GB = 250
    SIZE_500GB = 500
    SIZE_1000GB = 1000
