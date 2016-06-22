from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, HTTPError, URLError
from crawling_defines import CarInfo


def get_car_info_from_encar(car_id):
    # http://www.encar.com/dc/dc_cardetailview.do?carid=18498720
    url = 'http://www.encar.com/dc/dc_cardetailview.do?carid={0}'.format(str(car_id))
    url_request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        connection = urlopen(url_request)
    except:
        print('URL open error with car page')
        return None
    car_page = connection.read()
    connection.close()
    soup = BeautifulSoup(car_page, 'lxml')

    # page validation
    find_iter = soup.find_all('div', attrs={'class': 'car_info'})
    if 0 == len(find_iter):
        return None

    # ================================================================
    # head로부터 기본적인 차량 정보 받아오기
    # ================================================================
    find_iter = soup.head.find_all('meta')
    if 0 == len(find_iter):
        return None

    current_car = CarInfo(car_id)
    current_car.dealer_ = 'unknown'
    for i in range(len(find_iter)):
        attribute_name = find_iter[i].attrs.get('name');
        if attribute_name is None:
            continue
        # class 순서상 빈 것: 딜러
        if 'WT.z_state' == attribute_name:  # 차량 위치
            current_car.state_ = find_iter[i].attrs.get('content')
        # class 순서상 빈 것: 차량번호
        elif 'WT.z_price' == attribute_name:  # 총 구매비용
            current_car.price_ = find_iter[i].attrs.get('content')
        # class 순서상 빈 것: 제조사보증 유무
        elif 'WT.z_make' == attribute_name:  # 제조사
            current_car.set_maker(find_iter[i].attrs.get('content'))
        # class 순서상 빈 것: 차종
        # class 순서상 빈 것: 차량코드
        # class 순서상 빈 것: 모델
        # class 순서상 빈 것: 트림
        elif 'WT.trns' == attribute_name:  # 변속기
            current_car.transmission_ = find_iter[i].attrs.get('content')
        elif 'WT.whatfuel' == attribute_name:  # 연료
            current_car.fuel_ = find_iter[i].attrs.get('content')
        elif'WT.z_cat' == attribute_name:  # 분류
            current_car.category_ = find_iter[i].attrs.get('content')
        elif 'WT.z_year' == attribute_name:  # 연식
            current_car.year_ = find_iter[i].attrs.get('content')
        elif 'WT.z_month' == attribute_name:  # 출시월
            current_car.month_ = find_iter[i].attrs.get('content')
        elif 'WT.mileage' == attribute_name:  # 주행거리
            current_car.mileage_ = find_iter[i].attrs.get('content')
        elif 'WT.z_vehcat' == attribute_name:  # 상태
            current_car.condition_ = find_iter[i].attrs.get('content')
        elif 'WT.color' == attribute_name:  # 색상
            current_car.color_ = find_iter[i].attrs.get('content')
        # class 순서상 빈 것: 부품교환이력

    current_car.type_ = soup.body('span', class_='cls')[0].em.string
    current_car.model_ = soup.body('span', class_='dtl')[0]('strong')[-1].text
    current_car.modelCode_ = soup.body('span', class_='dtl')[0].em.string

    stat_detail = soup.body('ul', class_='stat_detail')[0]('li')
    for stat in stat_detail:
        if '차량번호' == stat.span.string:
            current_car.plateNumber_ = stat.text.split()[1]
        elif '배기량' == stat.span.string:
            current_car.displacement_ = stat.text.split()[1]
        elif '연비' == stat.span.string:
            current_car.fuelEfficiency_ = stat.text.split()[1]
        elif '수입형태' == stat.span.string:    # 제조사 보증 유무
           if 'X' in stat.text:
                current_car.warranty_ = False
           else:
               current_car.warranty_ = True

    # ================================================================
    # 딜러 및 상사 정보 받아오기
    # ================================================================
    # 상사 정보를 불러오기 위해서는 아래 링크를 띄워서 크롤링 해야함
    url = 'http://www.encar.com/dc/dc_carsearchpop.do?method=companyInfoPop&carTypeCd=1&carid={0}'.format(str(car_id))
    # url = 'http://www.encar.com/dc/dc_carsearchpop.do?method=companyInfoPop&carTypeCd=1&carid=0'
    url_request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        connection = urlopen(url_request)
    except:
        print('URL open error with dealer page')
        return None
    dealer_page = connection.read()
    connection.close()
    dealer_soup = BeautifulSoup(dealer_page, 'lxml')
    dealer_company = dealer_soup.body('table', {'class', 'viewinfo'})[0].find_all('td')[0].string

    # 딜러 본인의 이름 받아오기
    dealer_name = soup.body('div', {'class', 'dealer'})[0]('div', {'class', 'info'})[0].strong.string
    current_car.dealer_ = '{0}({1})'.format(dealer_name, dealer_company)

    # ================================================================
    # 옵션 정보 받아오기
    # ================================================================
    options = soup.body('div', {'class', 'box_opt'})
    options_basic = options[0]('dd', {'class', 'on'})
    for i in range(len(options_basic)):
        current_car.option_.set_option(options_basic[i].a.string)

    # 기타 옵션
    if 1 < len(options):
        options_etc = options[1]('dd')
        for i in range(len(options_etc)):
            current_car.option_.set_option(options_etc[i].string)

    # 추가 입력 옵션 (사용자가 추가로 요청 할 수 있는 옵션들인듯)
    if 2 < len(options):
        current_car.option_.additionalOptions_ = options[2].p.string

    # ================================================================
    # 부품 교환 이력 받아오기
    # ================================================================
    inspection_info = soup.body('div', class_='part inspection')[0]
    replacements = inspection_info('div', {'class', 'iconarea'})
    if 0 < len(replacements):
        replacement_list = replacements[0].find_all('span')
        for span in replacement_list:
            current_car.inspection_.repair_.append(span.string)

    # ================================================================
    # 차량 설명 받아오기
    # ================================================================
    current_car.description_ = soup.body('div', {'class', 'wrp_car_info'})[0]('div')[0].pre.string


    return current_car

#()()
#('')HAANJU.YOO
