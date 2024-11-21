"""
    Naver OpenAPI를 활용한 뉴스 검색 Step 1
    - url 접속 및 json 데이터 가져오기
    뉴스 100개
"""
import urllib.request
import datetime
import json


def get_request_url(url):
    client_id = 'abOnkbtE80NEvIT3FQIH'
    client_secret = '9OCzdpovZV'

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            #print(f"[{datetime.datetime.now()}] Url Reqeust Success")
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(f"Error for URL: {url}")


def get_naver_search(node, search_text, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = f"/{node}.json"  # 'news'
    query_string = f"{urllib.parse.quote(search_text)}"

    # f"?query={query_string}&start={start}&display={display}"
    # parameters = ("?query={}&start={}&display={}".
    #               format(query_string, start, display))
    parameters = (f"?query={query_string}&start={start}&display={display}")

    url = base + node + parameters
    response = get_request_url(url)

    if response is None:
        return None
    else:
        return json.loads(response)  # json 문자열을 Python 객체로 변환


def get_post_data(post, json_result, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    '''
     strptime()
     - %a: abbreviated weekday name 
     - %A: full weekday name
     - %b" abbreviated month name
    '''
    pdate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S')
    pdate = pdate.strftime('%Y-%m-%d %H:%M:%S')

    json_result.append({'cnt': cnt, 'title': title, 'description': description,
                        'org_link': org_link, 'link': org_link, 'pdate': pdate})


def main():
    node = 'news'  # 크롤링 대상
    # search_text = input('검색어를 입력하세요: ')
    search_text = '인공지능'
    cnt = 0
    json_result = []

    json_response = get_naver_search(node, search_text, 1, 100)
    if (json_response is not None) and (json_response['display'] != 0):
        for post in json_response['items']:
            cnt += 1
            # 1단계
            print(f"[{cnt}]", end=" ")
            print(post['title'])
            print(post['description'])
            print(post['originallink'])
            print(post['link'])
            print(post['pubDate'])

            # get_post_data(post, json_result, cnt)


if __name__ == '__main__':
    main()