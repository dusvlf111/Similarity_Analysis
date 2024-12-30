from sentence_transformers import SentenceTransformer


class SentenceEmbedding:
    _instance = None  # 클래스 변수로 인스턴스 저장

    def __new__(cls, model_name='paraphrase-MiniLM-L6-v2'):
        # 인스턴스가 이미 생성되어 있으면 기존 인스턴스를 반환
        if cls._instance is None:
            cls._instance = super(SentenceEmbedding, cls).__new__(cls)
            cls._instance.model = SentenceTransformer(model_name)
        return cls._instance
    
    def get_embeddings(self, sentences):
        """
        문장 리스트를 받아 임베딩을 생성하는 메서드.
        """
        # 문장 임베딩 생성
        return self.model.encode(sentences)

