from enum import Enum


class EnumObjectStoragePrintableAttributes(str, Enum):
    CLIENT_ID = "Client ID"
    EMAIL = "E-mail"
    PASSWORD = "Password"
    API_TOKEN = "Auth Token"
    ACCESS = "Access"
    DISPLAY_NAME = "Nome de exibição"
    QUOTA = "Quota"


class EnumQuotaSize(int, Enum):
    SIZE_100GB = 100
    SIZE_200GB = 200
    SIZE_300GB = 300
    SIZE_500GB = 500
    SIZE_600GB = 600
    SIZE_700GB = 700
    SIZE_800GB = 800
    SIZE_900GB = 900
    SIZE_1000GB = 1000

