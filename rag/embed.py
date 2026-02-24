from sentence_transformers  import SentenceTransformer

class embedder:
    def __init__(self, model="all-MiniLM-L6-v2"):
        self.model=SentenceTransformer(model)

    def embedtext(self,texts):
        return self.model.encode(texts, show_progress_bar=True)
