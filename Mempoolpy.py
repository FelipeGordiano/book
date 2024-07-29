import requests

class MempoolAPI:

    def __init__(self):
        """
        Inicializa a instância da classe com a URL base da API.
        """
        self.BASE_URL = "https://mempool.space/api/"
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

    def get_hashrate(self, period):
        """
        Obtém a taxa de hash de mineração para um período específico.

        Parâmetros:
        - period: O período para o qual obter a taxa de hash (por exemplo, "3d" para 3 dias).

        Retorna:
        - A taxa de hash para o período especificado.
        """
        endpoint = f"v1/mining/hashrate/{period}"
        return self._get(endpoint)

    def get_mempool_status(self):
        """
        Obtém o status atual do mempool.

        Retorna:
        - O status do mempool.
        """
        endpoint = "mempool"
        return self._get(endpoint)

    def get_recent_transactions(self):
        """
        Obtém as últimas transações.

        Retorna:
        - As últimas transações.
        """
        endpoint = "transactions"
        return self._get(endpoint)

    def get_historical_price(self, timestamp):
        """
        Obtém o preço histórico do Bitcoin em dólares para um dado timestamp.

        Parâmetros:
        - timestamp: O timestamp para o qual obter o preço.

        Retorna:
        - O preço do Bitcoin em dólares no timestamp especificado.
        """
        endpoint = f"v1/historical-price?currency=USD&timestamp={timestamp}"
        response = self._get(endpoint)
        if isinstance(response, str):  # Verifica se a resposta é um erro.
            return response
        return response.get("prices", [{}])[0].get("USD", "Preço não disponível")

    def get_average_rewards_by_block(self, period):
        """
        Obtém as médias de recompensas por bloco para um período específico.

        Parâmetros:
        - period: O período para o qual obter as médias de recompensas por bloco (por exemplo, "1d" para 1 dia).

        Retorna:
        - Uma lista de dicionários, onde cada dicionário contém informações sobre a altura média dos blocos,
        o timestamp e as recompensas médias de bloco nesse período.
        """
        endpoint = f"v1/mining/blocks/rewards/{period}"
        return self._get(endpoint)


    def get_address_info(self, address):
        """
        Obtém informações detalhadas sobre um endereço específico.

        Parâmetros:
        - address: O endereço para o qual obter as informações.

        Retorna:
        - Um dicionário contendo as informações sobre o endereço especificado.
        """
        endpoint = f"address/{address}"
        return self._get(endpoint)