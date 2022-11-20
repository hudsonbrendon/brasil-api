from brasil_api.brasilapi import BrasilAPI


class TestBrasilAPI:
    def test_brasil_api(self, brasil_api: BrasilAPI):
        assert isinstance(brasil_api, BrasilAPI)

    def test_base_url(self, brasil_api: BrasilAPI):
        assert brasil_api.base_url == "https://brasilapi.com.br"
