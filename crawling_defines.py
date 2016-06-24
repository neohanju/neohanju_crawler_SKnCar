def remove_legacy_characters(str_input):
    str_input = str_input.replace('\n', '')
    str_input = str_input.replace('\r', '')
    str_input = str_input.replace('\t', '')
    return str_input


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
    bExist_ = False                                 # 성능 점검 기록의 유무
    strYear_ = '1985'                               # 연식
    strFirstRegistrationDate_ = '1985년 3월 25일'    # 최초등록일
    nMileage_ = '0'                                 # 주행거리 및 계기상태
    strMotorType_ = 'unknown'                       # 원동기형식
    bIllegalRemodeling_ = False                     # 불법구조변경
    strVIN_ = 'unknown'                             # 차대번호 (Vehicle Identification Number)
    strVINMatching_ = 'unknown'                     # 동일성확인(차대번호 표기)라고 하나 명확히 무엇인지 모름
    bDamaged_ = False                               # 사고 유무
    bSubmerged_ = False                             # 사고 유무
    strWarrantyType_ = 'unknown'                    # 보증유형
    strTermOfValidity_ = 'unknown'                  # 검사유효기간
    # 자동차 상태 표시
    listExteriorRepairs_ = []                       # 외판
    listStructureRepairs_ = []                      # 주요 골격
    # 원동기
    strEngineOperation_ = 'unknown'                 # 작동상태
    strEngineOilLeakCylinderHead_ = 'unknown'       # 오일누유 (실린더 헤드)
    strEngineOilLeakCylinderBlock_ = 'unknown'      # 오일누유 (실린더 블럭)
    strEngineOilCondition_ = 'unknown'              # 오일 유량 및 오염
    strEngineCoolantLeakCylinderBlock_ = 'unknown'  # 냉각수누수 (실린더 블럭)
    strEngineCoolantLeakCylinderHead_ = 'unknown'   # 냉각수누수 (실린더 헤드)
    strEngineCoolantLeakWaterPump_ = 'unknown'      # 냉각수누수 (워터펌프)
    strEngineCoolantLeakCooler_ = 'unknown'         # 냉각수누수 (냉각쿨러)
    strEngineCoolantCondition_ = 'unknown'          # 냉각수량 및 오염
    strEngineCommonRail_ = 'unknown'                # 고압펌프(커먼레일)
    # 변속기 (변속기 종류마다 항목이 달라짐: 자동, 수동, 세미오토, CVT, 기타)
    strATGearboxOilLeak_ = 'unknown'                # 자동 변속기 오일누유
    strATGearboxOilCondition_ = 'unknown'           # 자동 변속기 오일유량 및 상태
    strATGearboxCondition_ = 'unknown'              # 자동 변속기 작동상태(공회전)
    strATGearboxStallTestForward_ = 'unknown'       # 자동 변속기 스톨시험(전진)
    strATGearboxStallTestBackward_ = 'unknown'      # 자동 변속기 스톨시험(후진)
    strMTGearboxOilLeak_ = 'unknown'                # 수동 변속기 오일누유
    strMTGearboxOilCondition_ = 'unknown'           # 수동 변속기 오일유량 및 상태
    strMTGearboxCondition_ = 'unknown'              # 수동 변속기 작동상태(공회전)
    strMTGearboxClutch_ = 'unknown'                 # 수동 변속기 기어변속장치
    # 동력전달
    strClutchAssembler_ = 'unknown'                 # 클러치 어셈블러
    strConstantVelocityJoint_ = 'unknown'           # 등속죠인트
    strThrustShaft_ = 'unknown'                     # 추친축 및 베어링
    # 조향
    strSteeringOilCondition_ = 'unknown'            # 동력조향 작동 오일 누유
    strSteeringGear_ = 'unknown'                    # 스티어링 기어
    strSteeringPump_ = 'unknown'                    # 스티어링 펌프
    strTieRodEndBall_ = 'unknown'                   # 스티어링 타이로엔드 및 볼 죠인트
    # 제동
    strBreakOilCondition_ = 'unknown'               # 브레이크 오일 유량상태
    strBreakOilLeak_ = 'unknown'                    # 브레이크 오일 누유
    strBreakBoosterCondition_ = 'unknown'           # 배력장치 상태
    # 전기
    strGeneratorPower_ = 'unknown'                  # 발전기 출력
    strStartingMotor_ = 'unknown'                   # 시동 모터
    strWiperMotor_ = 'unknown'                      # 와이퍼 모터 기능
    strAirConditionMotor_ = 'unknown'               # 실내송풍 모터
    strRadiatorFanMotor_ = 'unknown'                # 라디에이터 팬 모터
    # 기타
    strGasLeakage_ = 'unknown'                      # 연료누출 (LP가스포함)
    strWindowMotor_ = 'unknown'                     # 윈도우 모터 작동
    # 배출가스
    strEmissions_ = 'unknown'                       # 배출가스
    # 자가진단 사항
    strSelfInspection_ = 'unknown'                  # 자기진단 사항
    # 득기사항, 점검자 의견
    strInspectorOpinion_ = 'unknown'                # 특기사항, 점검자 의견


class CarInsurance:
    bExist_ = False                # 보험 기록 유무
    bChangePurpose_ = False        # 용도변경 이력
    nChangePlateNumber_ = 0         # 번호판 변경 횟수
    nChangeOwner_ = 0               # 소유자 변경 횟수
    strDamages_ = ''                # 파손 이력
    nWrecked_ = 0                   # 전손 횟수
    nStolen_ = 0                    # 도난 횟수
    nSubmerged_ = 0                 # 침수 횟수
    nFullySubmerged_ = 0            # 완전 침수 횟수
    nPartiallySubmerged_ = 0        # 부분 침수 횟수
    nAmountCompensationSelf_ = 0    # 자차 보상금
    nNumCompensationSelf_ = 0       # 자차 보상 횟수
    nAmountCompensationOthers_ = 0  # 타차 가해 보상금
    nNumCompensationOthers_ = 0     # 타차 가해 보상 횟수

    def set_change_purpose(self, str_change_purpose):
        if '없음' not in str_change_purpose:
            self.bChangePurpose_ = True

    def set_change_plate_number(self, str_change_plate_number):
        if str_change_plate_number.isdigit():
            self.nChangePlateNumber_ = int(float(str_change_plate_number))

    def set_change_owner(self, str_change_owner):
        if str_change_owner.isdigit():
            self.nChangeOwner_ = int(float(str_change_owner))

    def set_damages(self, str_damage):
        self.strDamages_ = remove_legacy_characters(str_damage)
        array_damages = self.strDamages_.split(', ')
        for cur_string in array_damages:
            if '전손' in cur_string:
                self.nWrecked_ = int(float(cur_string.split(' : ')[1]))
            elif '도난' in cur_string:
                self.nStolen_ = int(float(cur_string.split(' : ')[1]))
            elif '침수' in cur_string:
                self.nFullySubmerged_ = int(float(cur_string.split(' : ')[1]))
            elif '분손' in cur_string:
                self.nPartiallySubmerged_ = int(float(cur_string.split(' : ')[1].replace(')', '')))
            else:
                print('Unable to parse the string describing damages')

    def set_compensation_self(self, str_compensation_self):
        if '없음' not in str_compensation_self:
            str_compensation_self = remove_legacy_characters(str_compensation_self)
            array_string = str_compensation_self.split(', ')
            self.nNumCompensationSelf_ = int(float(array_string[0].replace('회', '')))
            self.nAmountCompensationSelf_ = int(float(array_string[1].replace('원', '').replace(',', '')))

    def set_compensation_others(self, str_compensation_others):
        if '없음' not in str_compensation_others:
            str_compensation_others = remove_legacy_characters(str_compensation_others)
            array_string = str_compensation_others.split(', ')
            self.nNumCompensationOthers_ = int(float(array_string[0].replace('회', '')))
            self.nAmountCompensationOthers_ = int(float(array_string[1].replace('원', '').replace(',', '')))


class CarInfo:
    # 판매 관련
    dealer_ = 'Mr.Dealer'               # 소유딜러(상사명)
    state_ = 'Kyung-gi'                 # 차량위치
    plateNumber_ = '02너3020'           # 차량번호
    price_ = '1250'                     # 총 구매비용 (만원단위)
    warranty_ = False                   # 제조사보증 유무
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


# ()()
# ('') HAANJU.YOO

