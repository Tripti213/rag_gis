class retriever:
    def __init__(self, vectordb, embedder):
        self.vectordb=vectordb
        self.embedder=embedder
    def retrieve(self, ques, k=20):
        ques_embed=self.embedder.embedtext([ques])
        return self.vectordb.search(ques_embed,k)    