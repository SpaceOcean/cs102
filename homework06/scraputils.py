import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    news_list_subtext = []
    news = {}
    tbl_list_title = parser.table.findAll('a', attrs={"class": "storylink"})
    for link in tbl_list_title:
        news = dict(title=link.get_text(), url=link.get('href'))
        news_list.append(news)
    tbl_list_subtext = parser.table.findAll('td', attrs={"class": "subtext"})
    for link in tbl_list_subtext:
        news = dict(author=link.find('a', attrs={"class": "hnuser"}).get_text(),
                comments=link.findAll('a')[-1].get_text(),
                points=link.find('span', attrs={"class": "score"}).get_text()[:-6])
        news_list_subtext.append(news)
    for news in news_list_subtext:
        if news['comments'] == 'discuss':
            news['comments'] = '0'
        else:
            news['comments'] = news['comments'][:-9]
        if news['points'][-1] == ' ':
            news['points'] = news['points'][:-1]
    for news in range(len(news_list)):
        news_list[news].update(news_list_subtext[news])

    return news_list


def extract_next_page(parser):
    """ Extract next page URL """
    return parser.table.find('a', attrs={"class": "morelink"}).get('href')


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news

if __name__ == '__main__':
    news_list = get_news("https://news.ycombinator.com/newest", n_pages=2)
    print(news_list)
