import requests
import bs4
import logging
import collections

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('wb')

ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'brand_name',
        'goods_name',
        'url'
    ),
)

class Client:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 YaBrowser/20.12.2.108 Yowser/2.5 Safari/537.36',
            'Accept-Language' : 'ru'
        }
        self.result = []

    def load_page (self, page: int = None):
        url = 'https://www.wildberries.ru/catalog/dom/dosug-i-tvorchestvo/tvorchestvo-i-rukodelie/shite'
        res = self.session.get(url = url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text)
        container = soup.select('div.dtList.i-dtList.j-card-item')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        # logger.info(block)
        # logger.info('=' * 100)

        url_block = block.select_one('a.ref_goods_n_p')

        name_block = block.select_one('div.dtlist-inner-brand-name')

        brand_name = name_block.select_one('strong.brand-name')
        brand_name = brand_name.text
        brand_name = brand_name.replace('/','').strip()

        goods_name = name_block.select_one('span.goods-name')
        goods_name = goods_name.text.replace('/','').strip()

        url = 'https://www.wildberries.ru' + url_block.get('href')




        logger.info('%s, %s, %s', url, brand_name, goods_name)

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)

if __name__ == '__main__':
    parser = Client()
    parser.run()
