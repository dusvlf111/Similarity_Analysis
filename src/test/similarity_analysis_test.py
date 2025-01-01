
from similarity_analysis.sentence_bert.CosineSimilarity import calculate_cosine_similarity
from sentence_bert.ParseJson import parse_sentences_from_json
from sentence_bert.Embedding import SentenceEmbedding

def SimilarityAnalysis(json_data):
    # JSON 데이터에서 문장 추출
    sentences = parse_sentences_from_json(json_data)

    if len(sentences) >= 2:
        # 임베딩 생성
        embedding_model = SentenceEmbedding()  # 모델은 한 번만 로드됨
        embeddings = embedding_model.get_embeddings(sentences)
        
        # 임베딩 결과 출력
        print("Embeddings:")
        for idx, embedding in enumerate(embeddings):
            print(f"Sentence {idx+1} Embedding: {embedding[:10]}...")  # 앞부분만 출력 (길이가 길어짐)

        # 코사인 유사도 계산
        similarity_score = calculate_cosine_similarity(embeddings[0], embeddings[1])
        print("----------------------------------------------------------------------")
        print(f"Cosine Similarity between the sentences: {similarity_score:.4f}")
        print("----------------------------------------------------------------------")

    else:
        print("Insufficient sentences in the JSON data.")

if __name__ == "__main__":
    # JSON 형식의 데이터 (예시)
    json_data = '''
    {
        "sentences": [
            "[속보]참사 하루 만에 제주항공 동일 기종서 또 랜딩기어 이상에 회항전남 무안국제공항에서 발생한 제주항공 여객기 참사 하루 만에 제주항공의 같은 기종이 사고 원인으로 지목된 부품과 동일한 이상으로 정상적으로 운항하지 못하는 일이 벌어졌다. 30일 항공업계에 따르면 이날 오전",
            "[속보] '김포발 제주행' 제주항공 동일 기종서 또 랜딩기어 이상으로 회항 30일 오전 6시 37분 '김포발 제주행' 제주항공 참사 여객기 동일 기종서 또 랜딩기어 이상 161명 승객에게 랜딩기어 문제에 따른 기체 결함을 안내한 뒤 회항"
        ]
    }
    '''
    json_data2 = '''
    {
        "sentences": [
            "[속보] 공수처, 윤 대통령 체포 영장소환 불응에 강제 수사 고위공직자범죄수사처가 윤석열 대통령에 대한 체포 영장을 전격 청구했습니다. 공수처는 내란과 직권 남용 등의 혐의로 윤석열 대통령에 대한 체포 영장을 서울서부지방법원에 청구했다고 밝혔습니다. 법원에서 체포 ",
            "[속보] 측, 공수처 체포영장에 즉각 대응 서부지법에 의견서 낼 것측 변호사 변호인 선임계도 제출 윤석열 대통령 측 윤갑근 변호사는 30일 고위공직자범죄수사처가 청구한 체포영장에 대한 의견서를 이날 오후 서울서부지법에 제출할 예정이라고 밝혔다. 윤 변호사는 이와 함께 "
        ]
    }
    '''
    
    SimilarityAnalysis(json_data)
    SimilarityAnalysis(json_data2)

    
