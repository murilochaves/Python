# começando com os imports
import re
import os.path
from urllib.request import Request, urlopen
from sys import argv

# definindo o sítio em que se encontra os dados para ser captados
site_farm = 'https://meiobit.com'

# https://meiobit.com/page/2/


def site_request(site):
    """
    Esta função tem como objetivo retornar uma requisição de um site.
    """

    return Request(site, headers={'User-Agent': 'Safari/12.0.2'})


def links_collecting(site):
    """
    Esta função tem como objetivo retornar uma lista com todos os links de
    artigos da página em questão do site.
    """

    # fazendo a requisição do site em questão
    site = site_request(site)

    # coletando o conteúdo HTML e armazenando em uma variável page_content
    page_content = str(urlopen(site).read())

    # regex para capturar os links de artigos
    article_links = list(set(re.findall(r'http[s]?:\/\/meiobit\.com\/[\d]+\/[A-Za-z0-9-]+\/', page_content)))

    return article_links


def mining_article(site_farm):
    """
    Esta função tem como objetivo capturar todas as informações do artigo em questão.
    """

    article_title = ''
    article_subtitle = ''
    article_text = ''

    # mostrando sítio em console
    print('\n* gathering: {}'.format(site_farm))

    # fazer uma nova requisição do site em questão
    site = site_request(site_farm)

    # coletando o conteúdo HTML e armazenando em uma variável page_content
    page_content = str(urlopen(site).read().decode('UTF-8'))

    # NOME DO ARQUIVO
    # pegar parte do link para nome do .txt
    pattern_archive_name = re.finditer(r'\d\/(.*)\/', site_farm)

    # armazendando a informação em uma stirng com .txt ao final
    for match in pattern_archive_name:
        archive_name = match.group(1) + '.txt'

    # TÍTULO DO ARTIGO
    # encontrar o título do artigo
    pattern_title = re.finditer(r'<title>(.*) - Meio Bit</title>', page_content)

    # armazenando o título da página à uma variável
    for match in pattern_title:
        article_title = match.group(1)

    # SUBTÍTULO DO ARTIGO
    # encontrar o subtítulo do artigo
    pattern_archive_subtitle = re.finditer(r'og:description\" content=\"([A-Za-z0-9à-ú,.:-@" !-]+)', page_content)

    # armazenando o subtítulo à uma variável
    for match in pattern_archive_subtitle:
        article_subtitle = match.group(1)

    # TEXTO DO ARTIGO
    # encontrando o conteúdo do com as tags <p> até <div class=\"....">
    pattern_article_text = re.finditer(r'<[p]>(.*)<div class=\"social-mobile mobile-class\">', page_content)

    # armazenando o conteúdo do texto à uma variável
    for match in pattern_article_text:
        article_text = match.group(1)

    # fazer uma limpeza nos dados: removendo todas as tags html
    article_text = re.sub('<[^<]+?>', '', article_text)

    # criando um repositório para armazenar os artigos
    data_folder = data_folder = 'source_data/Meio Bit/'

    # verificando se já existe um arquivo txt para não ocorrer duplicidades
    if not os.path.exists(data_folder + archive_name):
        with open(data_folder + archive_name, 'w') as f:
            f.write(site_farm + '\n')
            f.write(article_title + '\n')
            f.write(article_subtitle + '\n')
            f.write(article_text + '\n')
        print('\n* create archive: {}\n'.format(archive_name))
    else:
        print('\n* do not necessary create archive.')

    # definindo uma variável para mostrar as informações no console
    devMode = False

    # se o devMode estiver ativado, mostrará todas as informações do artigo
    # em console
    if devMode:
        print('\nContent HTML: {}'.format(page_content))
        print('\nName archive:\n{}'.format(archive_name))
        print('\nLink:\n{}'.format(site_farm))
        print('\nTitle:\n{}'.format(article_title))
        print('\nSubtitle:\n{}'.format(article_subtitle))
        print('\nText:\n{}'.format(article_text))


def gathering_all_articles(site, recorrency, initial_page=2):

    if 'max' in recorrency:
        execute = True

    aux_site = site

    number_page = initial_page

    while execute:
        # mostrando no console
        print('\n\n\tNext Page: {}'.format(aux_site))
        # capturando todos os links de artigos do site
        article_links = links_collecting(aux_site)

        # pegando todos os conteúdos presentes nos links
        for links in article_links:
            mining_article(links)

        aux_site = site + '/page/' + '{0}'.format(number_page)

        print(aux_site)

        number_page += 1


if __name__ == "__main__":
    # pegando o máximo de artigos que conseguir encontrar
    gathering_all_articles(site_farm, 'max', 1000)
