from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class CarInfo:
    maker_ = 'Vorkswagen'
    modelName_ = 'Vorkswagen Phaeton'
    modelTrim_ = 'V8 4.2 NWB VW611'
    transmitter_ = 'auto'
    condition_ = 'used'
    fuel_ = 'gas'
    state_ = 'Kyung-gi'
    category_ = 'full-size'
    color_ = 'black'
    mileage_ = 0
    price_ = 1250
    year_ = 2006
    month_ = 5
    carID_ = 18498720
    def __init__(self, carID):
        self.carID_ = carID
    def __del__(self):
        return None

def GetCarInfo(carID):
    # http://www.encar.com/dc/dc_cardetailview.do?carid=18498720
    url = 'http://www.encar.com/dc/dc_cardetailview.do?carid={0}'.format(str(carID))
    urlRequest = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    carPage = urlopen(urlRequest).read()
    soup = BeautifulSoup(carPage, 'lxml')

    # page validation
    findIter = soup.find_all("div", attrs={'class': "car_info"})

    if 0 == len(findIter):
        return None

    # extract car ID
    findIter = soup.head.find_all("meta")
    if 0 == len(findIter):
        return None

    currentCar = CarInfo(carID)
    print(findIter[0].attrs)
    for i in findIter:
        attributeName = findIter[i].attrs.get('name');
        if None == attributeName:
            continue
        if 'WT.z_model_name' == attributeName:
            car_model_name = head_contents[i].attrs.get('content')
            continue
        if 'WT.z_model_trim' == attributeName:
            car_model_trim = head_contents[i].attrs.get('content')
            continue



    print(soup_data.prettify())
