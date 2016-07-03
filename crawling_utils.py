from bs4 import BeautifulSoup
from urllib import parse
from urllib.request import Request, urlopen
from selenium import webdriver
from crawling_defines import CarInfo, CarSpecification, remove_legacy_characters, list_target_makers
import time
import json


def get_car_list_from_list_page(page_number):

    # scrape the page with selenium
    url = 'http://www.encar.com/fc/fc_carsearchlist.do?carType=for&searchType=model&wtClick_index=251#!%7B%22action' \
          '%22%3A%22%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22' \
          'page%22%3A{0}%2C%22limit%22%3A20%7D'.format(page_number)
    phantomjs_path = r'D:\Workspace\[LIBRARY]\[WEB]\phantomjs-2.1.1-windows\bin\phantomjs.exe'
    try:
        # driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT.copy())
        driver = webdriver.PhantomJS(phantomjs_path)
    except (ValueError, KeyError) as e:
        print('Driver error with Chrome browser')
        return None
    else:
        try:
            driver.get(url)
        except (ValueError, KeyError) as e:
            print('URL open error with car page')
            return None
    list_page = driver.page_source
    try:
        # because of bugs in the 'service', pass for quit method is demanded
        driver.quit()
    except AttributeError:
        pass
    soup = BeautifulSoup(list_page, 'lxml')

    # validate the page
    no_car_message = soup('p', {'class': 'message', 'title': '등록차량이 없습니다. 다른 조건으로 검색하세요.'})
    if 0 < len(no_car_message):
        print('there is no car list')
        return None

    # get gar list table
    car_list = soup.body('tbody', {'id': 'sr_normal'})
    if 0 == len(car_list):
        return None

    # get URLs of each car page and parse each page into 'result_car' instance
    result_car_list = []
    for tr in car_list[0]('td', {'class': 'inf'}):
        page_url = 'http://www.encar.com' + tr.a.get("href")
        result_car = get_car_info_from_car_detail_page(page_url)
        if result_car is not None:
            result_car_list.append(result_car)

    return result_car_list


def get_car_info_from_car_detail_page(page_url):

    # 자동차 페이지
    url_request = Request(page_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        connection = urlopen(url_request)
    except (ValueError, KeyError) as e:
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
    # 기본적인 차량 정보 받아오기
    # ================================================================
    find_iter = soup.head.find_all('meta', {'name': 'WT.z_CarId'})
    if 0 == len(find_iter):
        return None
    car_id = int(find_iter[0].attrs.get('content'))

    current_car = CarInfo(car_id)
    # current_car.dealer_ = 'unknown'
    # for i in range(len(find_iter)):
    #     attribute_name = find_iter[i].attrs.get('name')
    #     if attribute_name is None:
    #         continue
    #     # class 순서상 빈 것: 딜러
    #     if 'WT.z_state' == attribute_name:  # 차량 위치
    #         current_car.state_ = find_iter[i].attrs.get('content')
    #     # class 순서상 빈 것: 차량번호
    #     elif 'WT.z_price' == attribute_name:  # 총 구매비용
    #         current_car.price_ = find_iter[i].attrs.get('content')
    #     # class 순서상 빈 것: 제조사보증 유무
    #     elif 'WT.z_make' == attribute_name:  # 제조사
    #         current_car.set_maker(find_iter[i].attrs.get('content'))
    #     # class 순서상 빈 것: 차종
    #     # class 순서상 빈 것: 차량코드
    #     # class 순서상 빈 것: 모델
    #     # class 순서상 빈 것: 트림
    #     elif 'WT.trns' == attribute_name:  # 변속기
    #         current_car.transmission_ = find_iter[i].attrs.get('content')
    #     elif 'WT.whatfuel' == attribute_name:  # 연료
    #         current_car.fuel_ = find_iter[i].attrs.get('content')
    #     elif'WT.z_cat' == attribute_name:  # 분류
    #         current_car.category_ = find_iter[i].attrs.get('content')
    #     elif 'WT.z_year' == attribute_name:  # 연식
    #         current_car.year_ = find_iter[i].attrs.get('content')
    #     elif 'WT.z_month' == attribute_name:  # 출시월
    #         current_car.month_ = find_iter[i].attrs.get('content')
    #     elif 'WT.mileage' == attribute_name:  # 주행거리
    #         current_car.mileage_ = find_iter[i].attrs.get('content')
    #     elif 'WT.z_vehcat' == attribute_name:  # 상태
    #         current_car.condition_ = find_iter[i].attrs.get('content')
    #     elif 'WT.color' == attribute_name:  # 색상
    #         current_car.color_ = find_iter[i].attrs.get('content')
    #     # class 순서상 빈 것: 부품교환이력

    # current_car.type_ = soup.body('span', class_='cls')[0].em.string
    # current_car.model_ = soup.body('span', class_='dtl')[0]('strong')[-1].text
    # current_car.modelCode_ = soup.body('span', class_='dtl')[0].em.string

    # 페이지 마지막 디테일 정보에서 대충 긁어오기
    for input_field in soup.body('form', {'name': 'carDetail'})[0]('input'):
        if not input_field.has_attr('id'):
            continue
        current_car.set_info(input_field.attrs.get('id'), input_field.attrs.get('value'))

    # 페이지 중단에서 정보받아오기. 특히, 제조사 보증 유무를 위해
    stat_detail = soup.body('ul', class_='stat_detail')[0]('li')
    for stat in stat_detail:
        if '차량번호' == stat.span.string:
            current_car.plateNumber_ = stat.text.split()[1]
        elif '배기량:' == stat.span.string:
            current_car.displacement_ = stat.text.split(':')[1]
        elif '연비:' == stat.span.string:
            current_car.fuelEfficiency_ = stat.text.split(':')[1]
        elif '수입형태:' == stat.span.string:    # 제조사 보증 유무
            if 'X' in stat.text:
                current_car.warranty_ = False
            else:
                current_car.warranty_ = True

    # 리스 정보가 있을 경우, 리스 정보 읽기
    for lease_table in soup.body('ul', class_='brd_price'):
        for dl in lease_table('dl'):
            if '인수비용' == dl.dt.text:
                current_car.leaseCost_ = dl.dd.text
            elif '월리스료' == dl.dt.text:
                current_car.leaseMonthlyPay_ = dl.dd.text
            elif '잔여개월' == dl.dt.text:
                months = dl.dd.text.split('/')
                current_car.leaseLeftMonths_ = months[0]
                current_car.leaseTotalMonths_ = months[1].replace('개월', '')
            else:
                print('unknown information for lease')

    # ================================================================
    # 딜러 및 상사 정보 받아오기
    # ================================================================
    # 상사 정보를 불러오기 위해서는 아래 링크를 띄워서 크롤링 해야함
    url = 'http://www.encar.com/dc/dc_carsearchpop.do?method=companyInfoPop&carTypeCd=1&carid={0}'.format(str(car_id))
    url_request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        connection = urlopen(url_request)
    except (ValueError, KeyError) as e:
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
    # 성능 점검 기록 받아오기
    # ================================================================
    # 성능 점검 기록이 등록되어있다면 아래의 페이지가 제대로 접속될 것임
    url = 'http://www.encar.com/md/sl/mdsl_regcar.do?method=inspectionView&carid={0}'.format(str(car_id))
    url_request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        connection = urlopen(url_request)
    except (ValueError, KeyError) as e:
        current_car.inspection_.bExist_ = False
    else:
        current_car.inspection_.bExist_ = True
        inspection_page = connection.read()
        connection.close()
        inspection_soup = BeautifulSoup(inspection_page, 'lxml')
        table_body = inspection_soup.body('table', class_='ckst')[0].tbody
        table_field_names = table_body('th')
        table_field_values = table_body('td')
        # 차종에 따라, 사고와 침수가 함께 표시되고, 원동기 형식이 표기되지 않는 테이블들이 있음
        for i in range(len(table_field_names)):
            if '연식' in table_field_names[i].text:
                current_car.inspection_.strYear_ = table_field_values[i].text
            elif '차대번호' == table_field_names[i].text: # 동일성 확인 부분과 겹치므로, == 로 검사
                current_car.inspection_.strVIN_ = table_field_values[i].text
            elif '최초등록일' in table_field_names[i].text:
                current_car.inspection_.strFirstRegistrationDate_ = table_field_values[i].text
            elif '동일성확인' in table_field_names[i].text:
                current_car.inspection_.strVINMatching_ = remove_legacy_characters(table_field_values[i].text)
            elif '주행거리' in table_field_names[i].text:
                current_car.inspection_.nMileage_ = int(table_field_values[i].text.split()[0].replace(',', ''))
            elif '변속기종류' in table_field_names[i].text:
                current_car.inspection_.strVIN_ = remove_legacy_characters(table_field_values[i].text)
            elif '사고유무' == table_field_names[i].text:
                if '무' not in table_field_values[i].text:
                    current_car.inspection_.bDamaged_ = True
            elif '침수유무' == table_field_names[i].text:
                if '무' not in table_field_values[i].text:
                    current_car.inspection_.bSubmerged_ = True
            elif '사고/침수유무' == table_field_names[i].text:
                if '무' not in table_field_values[i].text:
                    print('유사고 표기방법: ' + table_field_values[i].text)  # 이런 경우가 거의 없어서, 크롤링 중 발견하면 report하도록
            elif '원동기형식' in table_field_names[i].text:
                current_car.inspection_.strMotorType_ = table_field_values[i].text
            elif '보증유형' in table_field_names[i].text:
                current_car.inspection_.strWarrantyType_ = table_field_values[i].text
            elif '불법구조변경' in table_field_names[i].text:
                if '없음' not in table_field_values[i].text:
                    current_car.inspection_.bIllegalRemodeling_ = True
            elif '검사유효기간' in table_field_names[i].text:
                current_car.inspection_.strTermOfValidity_ = table_field_values[i].text

        # 부품 교환 이력이 있는 것들 찾기
        repair_inspections = inspection_soup.body('dl', class_='section_cktxt')[0]('dd')
        if 1 < len(repair_inspections):
            structure_repair_list = repair_inspections[1]('span', {'class': 'on'})
            for repair_inst in structure_repair_list:
                current_car.inspection_.listStructureRepairs_.append(repair_inst.text)
        if 0 < len(repair_inspections):
            exterior_repair_list = repair_inspections[0]('span', {'class':'on'})
            for repair_inst in exterior_repair_list:
                current_car.inspection_.listExteriorRepairs_.append(repair_inst.text)

        # 개정된 성능 기록표
        status_name_list = []
        status_value_list = []
        new_inspection_tables = inspection_soup.body('table', class_='ckstl ckdata')[0]('tbody')
        for table in new_inspection_tables:
            cur_section_name = table.th.text + '_'
            cur_mid_section_name = ''
            for tr in table('tr'):
                for td in tr('td'):
                    if td.has_attr('rowspan'):        # 중간 섹션
                        cur_mid_section_name = td.text + '_'
                    else:
                        if td.has_attr('colspan'):    # 검사 항목 (중간 섹션 없는 경우)
                            if 3 == int(td.attrs.get('colspan')):  # 배기 가스 등, 여러 줄에 걸친 검사 결과
                                status_name_list.append(cur_section_name[:-1])  # 마지막에 언더라인 지우기
                                status_value_list.append(td.text)
                            else:
                                status_name_list.append(cur_section_name + td.text)
                                cur_mid_section_name = ''  # rowspan이 끝났음을 표현
                        else:
                            cur_status = td('span', {'class': 'on'})
                            if 0 < len(cur_status):   # 검사 결과
                                status_value_list.append(cur_status[0].text)
                            else:                     # 검사 항목
                                status_name_list.append(cur_section_name + cur_mid_section_name + td.text)

        # 항목별로 정리해서 집어 넣기
        for i in range(len(status_name_list)):
            current_car.inspection_.set_item(status_name_list[i], status_value_list[i])

    # ================================================================
    # 보험 기록 가져오기
    # ================================================================
    # 보험 기록이 등록되어있다면 아래의 페이지가 제대로 접속된 후, 테이블이 읽힐 것
    # 페이지 자체는 모두 존재함을 확인 함
    url = 'http://www.encar.com/dc/dc_cardetailview.do?method=kidiFirstPop&carid={0}'.format(str(car_id))
    url_request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    current_car.insurance_.bExist_ = False
    try:
        connection = urlopen(url_request)
    except (ValueError, KeyError) as e:
        print('no insurance page')
    else:
        insurance_page = connection.read()
        connection.close()
        insurance_soup = BeautifulSoup(insurance_page, 'lxml')
        smlist = insurance_soup.body('div', class_='smlist')
        if 0 < len(smlist):
            current_car.insurance_.bExist_ = True
            tr_list = smlist[0]('tr')
            for tr in tr_list:
                image_src = tr.img.get('src')
                if '/images/es/car_num2_2.gif' == image_src:  # 자동차 용도 이력
                    current_car.insurance_.set_change_purpose(tr('td')[1].text.split()[0])
                elif '/images/es/car_num2_3.gif' == image_src:  # 번호판 / 차주 변경 이력
                    input_numbers = tr('td')[1].text.split('/ ')
                    current_car.insurance_.set_change_plate_number(input_numbers[0].replace('회', ''))
                    current_car.insurance_.set_change_owner(input_numbers[1].replace('회', ''))
                elif '/images/es/car_num2_4.gif' == image_src:  # 파손 이력
                    current_car.insurance_.set_damages(tr('td')[1].text)
                elif '/images/es/car_num2_5.gif' == image_src:
                    current_car.insurance_.set_compensation_self(tr('td')[1].text)
                elif '/images/es/car_num2_6.gif' == image_src:
                    current_car.insurance_.set_compensation_others(tr('td')[1].text)

    # ================================================================
    # 차량 설명 받아오기
    # ================================================================
    current_car.description_ = soup.body('div', {'class', 'wrp_car_info'})[0]('div')[0].pre.string

    return current_car


def extract_list(soup_list, str_object_name):
    result_list = []
    for object in soup_list:
        number = object.get('value')
        if '' == number:
            continue
        name = object.text
        result_list.append({str_object_name: name, 'no': number})
    return result_list


def handling_dash(str_input):
    if '-' in str_input:
        return ''
    else:
        return str_input


def get_car_specification(start_year, end_year):
    base_url = 'http://www.bobaedream.co.kr/mycar/popup/popCatalogSpec.php'
    url_request = Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        connection = urlopen(url_request)
    except (ValueError, KeyError) as e:
        print('URL open error with car specification page')
        return None
    default_page = connection.read()
    connection.close()
    soup = BeautifulSoup(default_page, 'lxml')

    # 제조사 리스트 parsing
    maker_dics_candidate = extract_list(soup('select', {'name': 'maker_no'})[0]('option'), 'maker')

    # 관심 제조사만 추리기
    maker_dics = []
    for maker_dic in maker_dics_candidate:
        if maker_dic.get('maker') in list_target_makers:
            maker_dics.append(maker_dic)

    # 모델 받아오기
    for maker_dic in maker_dics:
        print('now get the car infos of {0}'.format(maker_dic.get('maker')))
        maker_page_url = base_url + '?maker_no={0}'.format(maker_dic.get('no'))
        try:
            connection = urlopen(maker_page_url)
        except (ValueError, KeyError) as e:
            print('URL open error with maker page')
            return None
        maker_page = connection.read()
        connection.close()
        maker_soup = BeautifulSoup(maker_page, 'lxml')
        model_dics = extract_list(maker_soup('select', {'name': 'model_no'})[0]('option'), 'model')

        # 등급 받아오기
        for model_dic in model_dics:
            print('\tget the car levels of {0}'.format(model_dic.get('model')))
            model_page_url = maker_page_url + '&model_no={0}'.format(model_dic.get('no'))
            try:
                connection = urlopen(model_page_url)
            except (ValueError, KeyError) as e:
                print('URL open error with maker page')
                return None
            model_page = connection.read()
            connection.close()
            model_soup = BeautifulSoup(model_page, 'lxml')
            level_dics = extract_list(model_soup('select', {'name': 'level_no'})[0]('option'), 'level')

            # 세부 등급 받아오기
            for level_dic in level_dics:
                level_page_url = model_page_url + '&level_no={0}'.format(level_dic.get('no'))
                try:
                    connection = urlopen(level_page_url)
                except (ValueError, KeyError) as e:
                    print('URL open error with maker page')
                    return None
                level_page = connection.read()
                connection.close()
                level_soup = BeautifulSoup(level_page, 'lxml')
                level_dic['level2'] = extract_list(level_soup('select', {'name': 'level2_no'})[0]('option'), 'level2')

            model_dic['levels'] = level_dics
        maker_dic['models'] = model_dics
        time.sleep(3)

    # 변속기는 자동/수동, 연도는 start_year ~ end_year까지
    str_transmission = [parse.quote('자동'), parse.quote('수동')]
    car_specifications = []
    for maker in maker_dics:
        for model in maker['models']:
            for level in model['levels']:
                for level2 in level['level2']:
                    for transmission in str_transmission:
                        for year in range(start_year, end_year):
                            test_page_url = base_url + '?maker_no={0}&model_no={1}&level_no={2}&level2_no={3}&' \
                                                       'method={4}&year={5}'.format(maker.get('no'), model.get('no'),
                                                                                    level.get('no'), level2.get('no'),
                                                                                    transmission, str(year))
                            try:
                                connection = urlopen(test_page_url)
                            except (ValueError, KeyError) as e:
                                print('URL open error with maker page')
                                return None
                            spec_page = connection.read()
                            connection.close()
                            spec_soup = BeautifulSoup(spec_page, 'lxml')
                            car_title = spec_soup('div', {'class': 'carlogo'})[0].text
                            if maker.get('maker') not in car_title:
                                continue

                            # 차량 기본 정보
                            cur_car_specification = CarSpecification()
                            cur_car_specification.maker = maker.get('maker')
                            cur_car_specification.model = model.get('model')
                            cur_car_specification.variant = level.get('level')
                            cur_car_specification.trim = handling_dash(level2.get('level2'))
                            cur_car_specification.year = year
                            # 본격적으로 제원 긁어오기
                            tables = spec_soup('div', {'class': 'popTableDv'})[0]('table')
                            # 물리적 치수는 테이블 2에
                            size_table_cells = tables[2]('td')
                            cur_car_specification.length = handling_dash(size_table_cells[0].text)
                            cur_car_specification.width = handling_dash(size_table_cells[2].text)
                            cur_car_specification.height = handling_dash(size_table_cells[4].text)
                            cur_car_specification.wheelbase = handling_dash(size_table_cells[6].text)
                            # 연료 및 성능은 테이블 3에
                            performance_table_cells = tables[3]('td')
                            cur_car_specification.displacement = handling_dash(performance_table_cells[4].text)
                            cur_car_specification.fuelType = handling_dash(performance_table_cells[0].text)
                            cur_car_specification.fuelConsumption = handling_dash(performance_table_cells[14].text)
                            # 변속기는 테이블 4에
                            cur_car_specification.transmission = handling_dash(tables[4]('td')[0].text)

                            car_specifications.append(cur_car_specification)

    with open('car_specs.txt', 'w') as outfile:
        json.dump([car_spec_class.__dict__ for car_spec_class in car_specifications], outfile)

    # 모델을 크롤링


# ()()
# ('') HAANJU.YOO

