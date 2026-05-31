# 1. Added history=[] to the arguments
def handle(action, state, kg, matcher, ai, q, history=[]):

    if action=="CHITCHAT":
        # 2. Passed history to ai()
        return ai("Respond naturally to the user greeting or casual message.", q, history)

    if action=="EXPLORE":
        # 2. Passed history to ai()
        return ai("Ask what the user wants to build and their goal", q, history)

    if action=="REFINE":
        if state.area and state.depth:
            return "Proceeding with available data..."
        
        prompt = f"""
User wants recommendation.

Known:
type:{state.type}
area:{state.area}
depth:{state.depth}
slope:{state.slope}

Ask ONE specific question to improve accuracy.
"""
        # 2. Passed history to ai()
        return ai(prompt, q, history)

    if action=="RECOMMEND":

        site={"area":state.area,"depth":state.depth}

        if state.type:
            result=matcher.check_suitability(site,state.type)
            return str(result)

        # 2. Passed history to ai()
        return ai("Suggest suitable structures based on data", q, history)

    if action=="KG":
        nodes=kg.dynamic_search(q)
        return str(nodes[:5])

    return ai(f"The user asked: '{q}'. Please use the conversation history to answer this follow-up.", q, history)