from rag.res_llm import get_resp

# 1. Added history=[] to the parameters
def ai(context, q="", history=[]):
    try:
        # 2. Passed history into the get_resp function
        return get_resp([context], q, history)
    except:
        return context