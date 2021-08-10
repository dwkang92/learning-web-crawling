# Request 라이브러리를 사용해보자
# 해당 라이브러리는 해당 주소로 요청을 보내면 응답을 받도록 해주는 HTTP 클라이언트이다.
# requests 라이브러리는 매우 직관적인 API를 제공한다.
# 어떤 방식의 HTTP요청을 하느냐에따라 해당하는 이름의 함수를 사용하면 된다.
# GET 방식: requests.get()
# POST 방식: requests.post()
# PUT 방식: requests.put()
# DELETE 방식: requests.delete()


r = requests.get(
    'http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    print(gu['MSRSTE_NM'], gu['IDEX_MVL'])
