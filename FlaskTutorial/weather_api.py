import requests

url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
service_key = "RY86xHRwOGsZ8K3FWKxwqE6zjJxf7cW0/MILj2JgqZFmG2AB9K45mP1RiyePy23jhtmXL6us4GtOXUFb0RIIzg=="

# 웹 요청시 같이 전달될 데이터 = 요청 메시지
params = {
    'serviceKey' : service_key,
    'numOfRows' : 30,
    'pageNo' : 1,
    'dataType' : 'JSON',
    'base_date' : '20200611', # 오늘 날짜
    'base_time' : '1400', # 요청 가능 발표 시간
    'nx' : 18, # 샘플 지역
    'ny' : 1 # 샘플 지역
}

res = requests.get(url=url , params=params)
print(res.status_code, type(res.text), res.url)
print()
print(res.text)