from crawling_utils import get_car_info_from_encar

# info = get_car_info_from_encar(19202670)   # 보험이력, 성능점검 둘 다 없지만, form은 있는 것
info = get_car_info_from_encar(19263032)  # 보험이력, 성능점검 둘 다 있고, 성능기록부사진 버튼까지 있음
# info = get_car_info_from_encar(18210804)
# info = get_car_info_from_encar(19296824)
if info is None:
    print('read nothing')
else:
    print('successfully read')
