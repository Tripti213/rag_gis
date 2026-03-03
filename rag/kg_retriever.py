class KGRetriever:

    def __init__(self, triples):
        self.triples=triples

        #for forward adjacency
        self.graph={}

        #for rev adjacency
        self.reverse_graph={}

        for s,r,o in triples:

            self.graph.setdefault(s.lower(),[]).append((r,o.lower()))
            self.reverse_graph.setdefault(o.lower(),[]).append((r,s.lower()))