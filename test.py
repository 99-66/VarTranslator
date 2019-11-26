import time
from v_translator.translator import VarTranslator

word_list = [
    '제조회사',  # manufacture_company
    '등록년월',  # date_of_registration
    '2in1태블릿',  # 2in1_tablet
    '운영체제',  # operating_system
    '화면정보',  # screen_information
    '화면크기(인치)',  # screen_size_inch
    '디스플레이',  # display
    '해상도',  # resolution
    'ppi',  # ppi
    '화면비율',  # aspect_ratio
    '멀티터치',  # multi-touch
    '시스템정보',  # system_information
    'CPU제조사',  # cpu_manufacturers
    'CPU명',  # cpu_person
    '코어개수',  # cores
    '코어클럭',  # core_clock
    'RAM용량',  # ram_capacity
    '저장용량',  # storage_capacity
    '저장매체',  # storage_media
    '추가메모리슬롯',  # additional_memory_slots
    '네트워크/규격',  # network_standard
    '태블릿통신',  # tablet_communication
    'WiFi주파수',  # wifi_frequency
    'WiFi다이렉트',  # wifi_direct
    '블루투스버전',  # bluetooth_version
    '카메라성능',  # camera_performance
    '후면카메라',  # rear_camera
    '전면카메라',  # front_camera
    '카메라플래시',  # camera_flash
    '4K촬영',  # 4k_shooting
    '센서',  # sensor
    '지문인식',  # fingerprint
    '얼굴인식',  # face_recognition
    '위치정보(GPS)',  # location_gps
    '자이로센서',  # the_gyro_sensor
    '가속도센서',  # accelerometer
    '나침반센서',  # compass_sensor
    '조도센서',  # ambient_light_sensor
    '근접센서',  # proximity_sensors
    '단자/액세사리',  # terminal_accessories
    'USB충전단자',  # usb_charging_terminal
    'USB속도',  # speed_​​usb
    'USB풀사이즈',  # usb_full_size
    'HDMI지원',  # hdmi_support
    '전용터치펜',  # dedicated_touch_pen
    '전용키보드',  # dedicated_keyboard
    '크기/무게/배터리',  # dimensions_weight_battery
    '배터리용량',  # battery_capacity
    '배터리사용시간',  # battery_life
    '가로',  # horizontal
    '세로',  # vertical
    '두께',  # thickness
    '무게(g)',  # weight_g
    '인증',  # certification
    '적합성평가인증',  # conformity_assessment_certificates
    '안전확인인증',  # safety_check_certification
]
start_time = time.time()

translator = VarTranslator()
for word in word_list:
    t_word = translator.translate(word)
    print(f'\'{word}\', #{t_word:>10}')


end_time = time.time()
print(f'time taken: {end_time - start_time}')


# Test List 번역 시간: 전체 리스트 대상
# (Cache/Redis)에 모든 단어가 없는 경우 : 7 ~ 8 sec
# (Cache/Redis)에 모든 단어가 있는 경우 : 0.4 sec
