import time
import sys
sys.path.append("C:/Users/dusvl/Documents/Similarity_Analysis/src")
from similarity_analysis.sentence_bert.CosineSimilarity import calculate_cosine_similarity,print_similarity_percentage

from similarity_analysis.sentence_bert.ParseJson import extract_title_and_description, read_json_file

from similarity_analysis.sentence_bert.Embedding import SentenceEmbedding




# 시작 시간 측정
start_time = time.time()

# JSON 파일 읽기
json_data = read_json_file("src/test/test2.json")

# JSON 데이터에서 문장 추출
sentences = extract_title_and_description(json_data)

embedding_model_name = []
# 임베딩 모델을 한 번만 로드하여 문장 임베딩 계산
embedding_model = SentenceEmbedding()  # 모델은 한 번만 로드됨

embeddings = embedding_model.get_embeddings(sentences)

# 코사인 유사도 계산
similarity_score = calculate_cosine_similarity(embeddings)

# 유사도 백분율로 출력
print_similarity_percentage(similarity_score, sentences)

# 끝난 시간 측정
end_time = time.time()

# 총 실행 시간 출력
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")
