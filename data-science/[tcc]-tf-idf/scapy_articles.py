# começando com os imports
from urllib.request import Request, urlopen

# definindo variáveis globais
sites_farm = 'https://meiobit.com'

# definindo a quantidade de artigos que deseja realizar o scaping
# number_articles = 1

articles_links = []


def capture_links():
    request_site = Request(sites_farm, headers={'User-Agent': 'Safari/12.0.2'})

    set_articles = []

    with urlopen(request_site) as response:
        page_content = response.read().decode('utf-8')

    # capturando a primeira lista de artigos do site (page_content_first_list)
    if '<div class="col-articles-list f-left" data-mh="col-articles-1">' in page_content:
        scaping_init = '<div class="col-articles-list f-left" data-mh="col-articles-1">'
        slice_init = int(page_content.index(scaping_init) + len(scaping_init))

        scaping_quit = '<div class="sidebar-banner f-right pc">'
        slice_quit = int(page_content.index(scaping_quit))

        set_articles.append(page_content[slice_init:slice_quit])

    #print(set_articles)
    #print(len(set_articles))

    # capturando a segunda lista de artigos do site (page_content_second_list)
    if '<div class="col-articles-list f-left" id="loadmore-home">' in page_content:
        scaping_init = '<div class="col-articles-list f-left" id="loadmore-home">'
        slice_init = int(page_content.index(scaping_init) + len(scaping_init))

        scaping_quit = '<div class="elm-wrapper">'
        slice_quit = int(page_content.index(scaping_quit))

        set_articles.append(page_content[slice_init:slice_quit])

    return set_articles


def extract_links(set_articles):
    global articles_links

    for element in set_articles:
        #print(element)

        page_content = element

        for link in range(element.count('<a href="')):

            scaping_init = '<a href="'
            scaping_quit = '" class=\'list-post-link\'>'

            slice_init = int(page_content.index(scaping_init) + len(scaping_init))

            page_content = page_content[slice_init:]

            slice_quit = int(page_content.index(scaping_quit))

            articles_links.append(page_content[:slice_quit])

            page_content = page_content[slice_quit:]


def save_article():

    aux = articles_links[:1]
    #print(aux)

    for link in aux:
        #print(link)
        request_site = Request(link, headers={'User-Agent': 'Safari/12.0.2'})

        with urlopen(request_site) as response:
            page_content = response.read().decode('utf-8')

        scaping_init = link + '">'
        scaping_quit = '</a></h1>'

        slice_title_init = int(page_content.index(scaping_init) + len(scaping_init))
        slice_title_quit = int(page_content.index(scaping_quit))

        article_title = page_content[slice_title_init:slice_title_quit]
        print(article_title)

        scaping_init = '<h2 class="olho">'
        scaping_quit = '</h2>'

        slice_subtitle_init = int(page_content.index(scaping_init) + len(scaping_init))
        slice_subtitle_quit = int(page_content.index(scaping_quit))

        article_subtitle = page_content[slice_subtitle_init:slice_subtitle_quit]

        #print(page_content[slice_subtitle_quit:])
        print(page_content)

        with open('{}.txt'.format(article_title), 'w') as archive:
            archive.write(article_title + '\n')
            archive.write(article_subtitle + '\n')


def scapy_articles():
    set_articles = capture_links()

    extract_links(set_articles)

    save_article()


if __name__ == "__main__":
    scapy_articles()
