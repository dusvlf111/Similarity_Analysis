import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(embeddings):
    """
    두 임베딩 벡터 간의 코사인 유사도를 계산하는 함수.
    
    :param embeddings: 첫 번째 문장 기준으로 끝까지 비교 
    :return: 코사인 유사도
    """
    cosine_sim = cosine_similarity([embeddings[0]], embeddings[1:])
    return cosine_sim[0]

def print_similarity_percentage(cosine_sim, sentences):
    """
    첫 번째 문장과 나머지 문장들 간 유사도를 백분율로 출력하는 함수.
    
    :param cosine_sim: 첫 번째 문장과 다른 문장들 간 유사도 (1D numpy array)
    :param sentences: 비교한 문장들
    """
    print(f"Similarity for the first sentence '{sentences[0]}':")
    for i in range(len(cosine_sim)):
        print(f"  Compared to Sentence {i + 2}: {cosine_sim[i] * 100:.2f}%")
    print()
