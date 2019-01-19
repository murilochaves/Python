# começando com os imports
from urllib.request import Request, urlopen
import re

# definindo o sítio em que se encontra os dados para ser captados
site_farm = "https://meiobit.com"


def site_request(site_farm):
    """
    Função com objetivo de fazer a requisição em um site.
    """
    return Request(site_farm, headers={'User-Agent': 'Safari/12.0.2'})


if __name__ == "__main__":
    site_farm = site_request(site_farm)

    page_content = str(urlopen(site_farm).read())

    # regex para captar os links
    articles_links = list(set(re.findall(r'https?:\/\/meiobit\.com\/[0-9]+\/[a-zA-Z0-9\-]+\/', page_content)))

    print(type(articles_links))
    print(len(articles_links))
    print(articles_links)

    teste = re.search(r'(\"og:title\" content=\")(*[\w\d\s]+)', page_content)
    print('\n\n\n\n', teste)
