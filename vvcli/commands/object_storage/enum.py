from enum import Enum


class EnumObjectStoragePrintableAttributes(str, Enum):
    CLIENT_ID = "Client ID"
    EMAIL = "E-mail"
    PASSWORD = "Password"
    API_TOKEN = "Auth Token"
