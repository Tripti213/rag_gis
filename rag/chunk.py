#used overlap based chunking currently, since took data directly from csv
def extract_csv(path):

    import csv
    texts=[]

    with open(path,'r',encoding='utf-8') as f:
        reader=csv.DictReader(f)

        for row in reader:

            chunk=f"""
                    Water Body: {row['name']}
                    Type: {row['type']}
                    District: {row['district']}
                    Coordinates: {row['latitude']}, {row['longitude']}
                    Capacity: {row['capacity']}
                    Purpose: {row['description']}
                """

            texts.append(chunk.strip())

    return texts