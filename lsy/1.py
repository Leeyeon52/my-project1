import requests
import xmltodict

# 1. API 키 설정
API_KEY = 'trcnbljnjkgvgctyvcgfhve546d7cdi78fcdr6ddc7869707fx577scy8bubbvtc5exw4z6567g0h9ji0kimub7y'  # 자신의 인증키
API_KEY_decode = requests.utils.unquote(API_KEY)  # URL 인코딩 해제

# 2. 우체국 도로명 주소 조회 API URL (정확한 최신 URL 확인 필요)
url = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getMsrstnList'

# 3. 검색 조건 설정
search_Se = "road"  # 검색 유형 (road: 도로명 주소, dong: 동 주소)
srch_wrd = "둔산대로 135"  # 검색어 (도로명 주소 입력)

# 4. 한글 주소를 URL 인코딩하여 API 요청이 정상적으로 수행되도록 처리
encoded_srch_wrd = requests.utils.quote(srch_wrd)

params = {
    "ServiceKey": API_KEY_decode,
    "searchSe": search_Se,
    "srchwrd": encoded_srch_wrd,
}

# 5. API 요청
response = requests.get(url, params=params)
print("응답 코드:", response.status_code)  # 응답 코드 확인 (200이어야 정상)

# 6. 응답 데이터 확인
if response.status_code == 200:
    xml_data = response.text
    dict_data = xmltodict.parse(xml_data)  # XML → Dict 변환

    # 7. 응답 데이터 구조 확인 (디버깅용)
    print("응답 데이터 구조:", dict_data.keys())
    print("전체 응답 데이터:", dict_data)

    # 8. 주소 데이터 추출
    try:
        if 'NewAddressListResponse' in dict_data and 'newAddressListAreaCd' in dict_data['NewAddressListResponse']:
            address_list = dict_data['NewAddressListResponse']['newAddressListAreaCd']
            
            # 여러 개의 결과가 반환될 수 있으므로 리스트 처리
            if isinstance(address_list, list):
                address_list = address_list[0]  # 첫 번째 결과 선택

            print("[입력한 도로명 주소]", srch_wrd)
            print("[응답 데이터에서 추출한 결과]")
            print("- 우편번호:", address_list.get('zipNo', '데이터 없음'))
            print("- 도로명주소:", address_list.get('lnmAdres', '데이터 없음'))
            print("- 지번주소:", address_list.get('rnAdres', '데이터 없음'))
        
        else:
            print("❌ 주소 데이터를 찾을 수 없습니다. API 응답 구조를 확인하세요.")

    except KeyError as e:
        print(f"❌ KeyError 발생: {e}. API 응답 구조를 확인하세요.")

else:
    print("❌ API 요청 실패. 응답 코드:", response.status_code)
