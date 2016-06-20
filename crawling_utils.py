from bs4 import BeautifulSoup
from urllib.request import Request,urlopen

def get_car_info(car_id):
    # http://www.encar.com/dc/dc_cardetailview.do?carid=18498720
    url = 'http://www.encar.com/dc/dc_cardetailview.do?carid={0}'.format(str(car_id))
    url_request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    car_page = urlopen(url_request).read()
    soup_data = BeautifulSoup(car_page, 'lxml')

    # page validation
    find_mytr = soup_data.find_all("div", attrs={'class': "section view none"})


    print(soup_data.prettify())
