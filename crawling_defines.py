class CarOption:
    # 옵션 정보는 다음의 링크 참고: http://www.encar.com/dc/dc_carsearchpop.do?method=optionDic&optncd=029&carTypeCd=1
    # 외관
    HID_ = False                  # HID 헤드램프
    powerMirror_ = False          # 전동접이식미러
    sunroof_ = False              # 선루프
    roofRack_ = False             # 루프랙
    alloyWheels_ = False          # 알루미늄휠
    # 내장
    steeringWheelRC_ = False      # 스티어링 휠 리모컨 (핸들에 버튼 달렸는지 여부)
    powerSteeringWheel_ = False   # 파워 스티어링
    ECM_ = False                  # ECM (야간 주행을 위한 룸미러 반사율 자동 조절)
    leatherSeats_ = False         # 가죽 시트
    powerDriverSeat_ = False      # 전동 시트 (운전석)
    powerAssistantSeat_ = False   # 전동 시트 (조수석)
    heatedSeatFront_ = False      # 열선 시트 (앞좌석)
    heatedSeatRear_ = False       # 열선 시트 (뒷좌석)
    memorySeat_ = False           # 메모리 시트
    ventilationSeat_ = False      # 통풍 시트
    # 안전
    airbagDriver_ = False         # 에어백 (운전석)
    airbagAssistant_ = False      # 에어백 (조수석)
    airbagSide_ = False           # 에어백 (사이드)
    airbagCurtain_ = False        # 에어백 (커튼)
    rearOccupantSensing_ = False  # 후방감지센서
    rearCamera_ = False           # 후방카메라
    ABS_ = False                  # ABS
    TCS_ = False                  # 미끄럼방지
    VDC_ = False                  # 차체자세 제어 장치
    ECS_ = False                  # 전자제어 서스펜션
    TPMS_ = False                 # 타이어 공기압감지
    powerDoorLock_ = False        # 파워 도어록 (운전석에 차량 잠금/해제 가능 여부)
    # 편의
    autoAirconditioner_ = False   # 자동 에어컨
    remoteDoorLock_ = False       # 무선 도어 잠금 장치
    smartKey_ = False             # 스마트키
    powerTrunk_ = False           # 파워 트렁크
    powerWindow_ = False          # 파워 윈도우
    cruiseControl_ = False        # 크루즈 컨트롤
    navigation_ = False           # 네비게이션
    handsFreeExt_ = False         # 핸즈프리
    hipass_ = False               # 내장 하이패스
    # 멀티미디어
    CDPlayer_ = False             # CD 플레이어
    CDChanger_ = False            # CD 체인저
    AVSystem_ = False             # AV 시스템
    rearSeatTV_ = False           # 뒷좌석 TV
    AUX_ = False                  # AUX 단자
    USB_ = False                  # USB 단자
    iPod_ = False                 # iPod 단자
    # 기타 옵션
    ETC_ = []                      # 기타 옵션
    # 추가입력 옵션
    additionalOptions_ = ''        # 추가 입력 옵션

    def __del__(self):
        return None

    def set_option(self, str_option_name, flag=True):
        if 'HID' in str_option_name:
            self.HID_ = flag
        elif '전동접이 사이드미러' in str_option_name:
            self.powerMirror_ = flag
        elif '선루프' in str_option_name:
            self.sunroof_ = flag
        elif '루프랙' in str_option_name:
            self.roofRack_ = flag
        elif '알루미늄휠' in str_option_name:
            self.alloyWheels_ = flag
        elif '스티어링 휠 리모컨' in str_option_name:
            self.steeringWheelRC_ = flag
        elif '파워 스티어링' in str_option_name:
            self.powerSteeringWheel_ = flag
        elif 'ECM' in str_option_name:
            self.ECM_ = flag
        elif '가죽' in str_option_name:
            self.leatherSeats_ = flag
        elif '전동 시트(운전석)' in str_option_name:
            self.powerDriverSeat_ = flag
        elif '전동 시트(동승석)' in str_option_name:
            self.powerAssistantSeat_ = flag
        elif '열선 시트(앞좌석)' in str_option_name:
            self.heatedSeatFront_ = flag
        elif '열선 시트(뒷좌석)' in str_option_name:
            self.heatedSeatRear_ = flag
        elif '메모리 시트' in str_option_name:
            self.memorySeat_ = flag
        elif '통풍 시트(앞좌석)' in str_option_name:
            self.ventilationSeat_ = flag
        elif '에어백(운전석)' in str_option_name:
            self.airbagDriver_ = flag
        elif '에어백(동승석)' in str_option_name:
            self.airbagAssistant_ = flag
        elif '에어백(사이드)' in str_option_name:
            self.airbagSide_ = flag
        elif '커튼 에어백' in str_option_name:
            self.airbagCurtain_ = flag
        elif '후방 감지센서' in str_option_name:
            self.rearOccupantSensing_ = flag
        elif '후방 카메라' in str_option_name:
            self.rearCamera_ = flag
        elif 'ABS' in str_option_name:
            self.ABS_ = flag
        elif 'TCS' in str_option_name:
            self.TCS_ = flag
        elif '차체자세' in str_option_name:
            self.VDC_ = flag
        elif 'ECS' in str_option_name:
            self.ECS_ = flag
        elif 'TPMS' in str_option_name:
            self.TPMS_ = flag
        elif '파워 도어록' in str_option_name:
            self.powerDoorLock_ = flag
        elif '자동 에어컨' in str_option_name:
            self.autoAirconditioner_ = flag
        elif '무선 도어잠금장치' in str_option_name:
            self.remoteDoorLock_ = flag
        elif '스마트 키' in str_option_name:
            self.smartKey_ = flag
        elif '파워 트렁크' in str_option_name:
            self.powerTrunk_ = flag
        elif '파워 윈도우' in str_option_name:
            self.powerWindow_ = flag
        elif '크루즈 컨트롤' in str_option_name:
            self.cruiseControl_ = flag
        elif '네비게이션' in str_option_name:
            self.navigation_ = flag
        elif '핸즈프리' in str_option_name:
            self.handsFreeExt_ = flag
        elif '하이패스' in str_option_name:
            self.hipass_ = flag
        elif 'CD 플레이어' in str_option_name:
            self.CDPlayer_ = flag
        elif 'CD 체인저' in str_option_name:
            self.CDChanger_ = flag
        elif 'AV 시스템' in str_option_name:
            self.AVSystem_ = flag
        elif '뒷좌석 TV' in str_option_name:
            self.rearSeatTV_ = flag
        elif 'AUX' in str_option_name:
            self.AUX_ = flag
        elif 'USB' in str_option_name:
            self.USB_ = flag
        elif 'iPod' in str_option_name:
            self.iPod_ = flag
        else:
            print('unknown option')
            self.ETC_.append(str_option_name)


class CarInspection:
    exist_ = False     # 성능 점검 기록의 유무
    repair_ = []        # 수리 이력
    replacement_ = ''   # 교체
    welding_ = ''       # 용접
    erosion_ = ''       # 부식
    accident_ = False  # 사고유무


class CarInsurance:
    exist_ = False          # 보험 기록 유무
    changePurpose_ = ''      # 용도변경 이력
    changePlateNumber_ = ''  # 번호판 변경 횟수
    changeOwner_ = ''        # 소유자 변경 횟수
    damages_ = ''            # 파손 이력
    compensationSelf_ = ''   # 자차 보상
    compensationOther_ = ''  # 타차 가해


class CarInfo:
    # 판매 관련
    dealer_ = 'Mr.Dealer'               # 소유딜러(상사명)
    state_ = 'Kyung-gi'                 # 차량위치
    plateNumber_ = '02너3020'           # 차량번호
    price_ = '1250'                     # 총 구매비용 (만원단위)
    warranty_ = False                  # 제조사보증 유무
    # 차량모델
    maker_ = 'Volkswagen'               # 제조사
    type_ = 'Volkswagen Phaeton'        # 차종
    modelCode_ = 'PT'                   # 차량코드
    model_ = 'V8 4.2'                   # 모델
    trim_ = 'V8 4.2 NWB VW611'          # 트림
    transmission_ = 'auto'              # 변속기
    fuel_ = 'gas'                       # 연료
    category_ = 'full_size'             # 분류
    displacement_ = '4000'              # 배기량
    fuelEfficiency_ = '9.0'             # 연비
    # 등록정보
    year_ = '2006'                      # 연식
    month_ = '05'                       # 출시월
    # 차량 상태
    mileage_ = '0'                      # 주행거리
    condition_ = 'used'                 # 상태
    color_ = 'black'                    # 색상
    option_ = CarOption()               # 차량 옵션
    inspection_ = CarInspection()       # 차량 검사 결과
    insurance_ = CarInsurance()         # 차량 보험 기록
    # 기타 encar 관련
    description_ = ''                   # 차량 소개글
    carID_ = 18498720                   # DB 등록 번호

    def __init__(self, car_id):
        self.carID_ = car_id

    def __del__(self):
        return None

    # def set_category(self, korean_string):
    #     if '대형차' == korean_string:
    #         self.category_ = 'full_size'
    #     elif '중형차' == korean_string:
    #         self.category_ = 'medium_size'
    #     elif '소형차' == korean_string:
    #         self.category_ = 'compact_car'
    #     else:
    #         self.category_ = 'unknown'

    def set_maker(self, skencar_maker_string):
        if '폭스바겐' == skencar_maker_string:
            self.maker_ = 'Volkswagen'
        elif '벤츠' == skencar_maker_string:
            self.maker_ = 'Mercedes Benz'
        else:
            self.maker_ = skencar_maker_string


#()()
#('')HAANJU.YOO

