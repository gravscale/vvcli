import json
import os
from pathlib import Path

import toml
import urllib3

import vvcli_sdk
from decouple import config


class CliConfiguration:
    host: str
    verify_ssl: bool

    def __init__(self):
        self._config_path = self._get_config_path()
        self.host = config("VVCLI_API_ENDPOINT", default="https://api.under.com.br/v1")
        self.verify_ssl = config("VVCLI_VERIFY_SSL", cast=bool, default=True)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    @classmethod
    def _get_config_path(cls):
        return os.path.join(str(Path.home()), ".vvcli/")

    def _ensure_config_directory(self):
        config_dir = os.path.dirname(self._config_path)
        os.makedirs(config_dir, exist_ok=True)

    def _load_authorization(self) -> dict:
        try:
            with open(os.path.join(self._config_path, ".auth.json"), "r") as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return {}

    def save_authorization(self, token: str):
        self._ensure_config_directory()
        with open(os.path.join(self._config_path, ".auth.json"), "w") as file:
            json.dump(
                {
                    "access_token": f"{token}",
                },
                file,
                default=str,
            )

    def load_sdk_configuration(self) -> vvcli_sdk.Configuration:
        config = {"host": self.host, "verify_ssl": self.verify_ssl}
        auth = self._load_authorization()
        if "access_token" in auth.keys():
            config["access_token"] = auth.get("access_token")
        return vvcli_sdk.Configuration(**config)

    @classmethod
    def read_user_config(cls, path_config_file: str):
        with open(path_config_file, "r") as file:
            config = toml.load(file)
        return config
