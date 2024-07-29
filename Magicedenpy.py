import requests

class MagicEden:

    def __init__(self):
        """
        Inicializa a instância da classe com a URL base da API.
        """
        self.BASE_URL = "https://api-mainnet.magiceden.dev/v2/ord/"
        self.session = requests.Session()

    def _get(self, endpoint):
            """
            Faz uma solicitação GET para um endpoint específico da API.

            Parâmetros:
            - endpoint: O endpoint da API para acessar.

            Retorna:
            - A resposta da solicitação como um dicionário.
            """
            try:
                response = self.session.get(self.BASE_URL + endpoint)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.HTTPError as http_err:
                return f"Erro HTTP: {http_err}"
            except Exception as err:
                return f"Erro: {err}"

    def get_rune_balance(self, address):
        """
        Obtém o balanço de runes em uma carteira.

        Parâmetros:
        - address: Endereço público da chave bc1.

        Retorna:
        - A taxa de hash para o período especificado.
        """
        endpoint = f"btc/runes/wallet/balances/{address}/rune"
        return self._get(endpoint)