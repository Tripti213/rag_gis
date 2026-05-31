import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 1. Added history=[] to the arguments
def get_resp(context_chunks, ques, history=[]):

    if not context_chunks:
        return "No matching data found."

    contexts="\n".join(context_chunks)

    # 2. Format the history into a readable text block
    history_text = ""
    if history:
        history_text = "--- CONVERSATION HISTORY ---\n"
        for msg in history:
            # Safely extract data whether it's a Pydantic model or dictionary
            role = msg.role if hasattr(msg, 'role') else msg.get('role', 'user')
            content = msg.content if hasattr(msg, 'content') else msg.get('content', '')
            
            speaker = "User" if role == "user" else "Assistant"
            history_text += f"{speaker}: {content}\n"
        history_text += "----------------------------\n"

    # 3. Injected the history_text into your prompt
    prompt=f"""
You are a GIS decision-support assistant.

IMPORTANT:
- If the query asks "where built", interpret it as CONDITIONS (area, depth, slope).
- If the query asks "where located", interpret it as LOCATIONS (villages, coordinates).

STRICT RULES:
- Use ONLY the provided context AND the conversation history.
- Do NOT add any external information.
- Do NOT guess or hallucinate missing values.
- If data is missing, ignore it.
- Be concise and clear.

{history_text}

DATA FORMAT:
Each entry contains:
Village, Panchayat, Coordinates, Area (m²), Depth (m)

CONTEXT:
{contexts}

USER QUERY:
{ques}

OUTPUT FORMAT:
- 1–2 line explanation
- Then list key results in short form

ANSWER:
"""

    response=client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
    )

    return response.text.strip()