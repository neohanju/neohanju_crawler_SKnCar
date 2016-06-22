from crawling_utils import get_car_info_from_encar

# get_car_info_from_encar(19354224)
# info = get_car_info_from_encar(18498720)
info = get_car_info_from_encar(19260152)
if info is None:
    print('read nothing')
else:
    print('successfully read')
