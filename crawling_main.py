from crawling_utils import get_car_info_from_encar, get_car_list_from_encar

# info = get_car_info_from_encar(19202670)   # 보험이력, 성능점검 둘 다 없지만, form은 있는 것
# info = get_car_info_from_encar(19263032)  # 보험이력, 성능점검 둘 다 있고, 성능기록부사진 버튼까지 있음
# info = get_car_info_from_encar(18690055)  # 보험처리 이력 있는 차
# info = get_car_info_from_encar(18934713)  # 성능점검 있는 차 (수동)
# info = get_car_info_from_encar(19296824)
# info = get_car_info_from_encar(18334408)  # CVT 차량
# info = get_car_info_from_encar(18602966)  # 세미오토 차량
# info = get_car_info_from_encar(19018207)  # 리스 차량
# info = get_car_info_from_encar(19267048)  # 기타 분류 차량. 구체적으로 뭘까?


def main_crawling():
    car_lists = []
    for page_number in range(500):
        cur_car_list = get_car_list_from_encar(page_number)
        if cur_car_list is None:
            break
        car_lists.append(cur_car_list)

