from rag.query_node_generation import QueryMapper

class KGRetriever:

    def __init__(self, triples):
        self.triples=triples


    def search(self, query):

        mapper=QueryMapper()
        concepts=mapper.map_query(query)

        matched_entities=set()

        for s, r, o in self.triples:

            for c in concepts:

                if c in o.lower():
                    matched_entities.add(s)

                if c in r.lower():
                    matched_entities.add(s)

        return list(matched_entities)


    def filter_by_location(self, entities, location):

        valid=set()

        for s, r, o in self.triples:

            if r == "located_in" and o.lower() == location.lower():
                if s in entities:
                    valid.add(s)

        return list(valid)