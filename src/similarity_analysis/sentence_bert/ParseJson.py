import json

def parse_sentences_from_json(json_data):
    """
    JSON 데이터를 받아 문장 리스트를 추출하는 함수.
    
    :param json_data: JSON 형식의 문자열
    :return: 문장 리스트
    """
    data = json.loads(json_data)  # JSON 문자열을 파이썬 딕셔너리로 변환
    return data.get('sentences', [])  # 'sentences' 키에 해당하는 값 반환, 없으면 빈 리스트 반환


def extract_title_and_description(data):
    """
    title과 description을 결합하여 리스트로 반환하는 함수.
    
    :param data: JSON 형식의 데이터
    :return: title과 description이 결합된 문장의 리스트
    """
    result = []
    for item in data["items"]:
        title = item["title"]
        description = item["description"]
        combined_text = f"{title} {description}"
        result.append(combined_text)
    return result


def read_json_file(file_path):
    """
    주어진 경로에서 JSON 파일을 읽고 데이터를 반환하는 함수.
    
    :param file_path: JSON 파일 경로
    :return: JSON 데이터
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

