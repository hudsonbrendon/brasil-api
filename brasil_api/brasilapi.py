import requests


class BrasilAPI(object):
    __BASE_URL = "https://brasilapi.com.br"

    @property
    def base_url(self) -> str:
        return self.__BASE_URL
