import json
from kgraph_generation import kgraphbuilder

builder=kgraphbuilder()
triples=builder.build("../data/water_bodies_data.csv")

with open("kgraph.json", "w") as f:
    json.dump(triples, f)

print("Knowledge graph built n saved.")