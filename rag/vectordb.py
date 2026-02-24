import numpy as np
import faiss

class vectordatabase:
    def __init__(self, dimension:int):
        self.index=faiss.IndexFlatL2(dimension)
        self.texts=[]
    
    def add(self, embeddings, texts):
        embeddings=np.array(embeddings).astype("float32")
        self.index.add(embeddings)
        self.texts.extend(texts)

    def search(self, ques_embedding, k=4):
        ques_embedding=np.array(ques_embedding).astype("float32")
        dist, indexes=self.index.search(ques_embedding,k)

        return [self.texts[x] for x in indexes[0]]
    