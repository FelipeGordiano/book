import requests
import config

class OrdiScan:

    def __init__(self):
        """
        Inicializa a instância da classe com a URL base da API.
        """
        self.BASE_URL = "https://api.ordiscan.com/v1/"
        self.headers_os = {"Authorization": f"Bearer {config.api_secret_os}"}
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
                response = self.session.get(self.BASE_URL + endpoint, headers=self.headers_os)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.HTTPError as http_err:
                return f"Erro HTTP: {http_err}"
            except Exception as err:
                return f"Erro: {err}"

    def get_ordinals_balance(self, address):
        """
        Obtém o balanço de ordinals em uma carteira.

        Parâmetros:
        - address: Endereço público da chave bc1.

        Retorna:
        - A taxa de hash para o período especificado.
        """
        endpoint = f'address/{address}/inscriptions'
        return self._get(endpoint)

    def get_runes_balance(self, address):
        """
        Obtém o balanço de runes em uma carteira.

        Parâmetros:
        - address: Endereço público da chave bc1.

        Retorna:
        - A taxa de hash para o período especificado.
        """
        endpoint = f'address/{address}/runes'
        return self._get(endpoint)

    def get_rune_info(self, name):
        """
        Obtém informações de mercado de uma rune.

        Parâmetros:
        - name: Endereço público da chave bc1.

        Retorna:
        - Informações de mercado para a rune especificada.
        """
        endpoint = f'rune/{name}/market'
        return self._get(endpoint)