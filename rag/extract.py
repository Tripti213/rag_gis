import pandas as pd

def extract_csv(csv_path:str):
    df=pd.read_csv(csv_path)
    df=df.fillna("unknown")

    extracted_texts=[]

    for _, row in df.iterrows():
        ex=(
            f"{row['name']} is a {row['type']} in {row['district']} "
            f"at coordinates ({row['latitude']}, {row['longitude']}). "
            f"Capacity of the Water Body: {row['capacity']}. "
            f"{row['description']}"
        )
        extracted_texts.append(ex)
    
    return extracted_texts
    
    