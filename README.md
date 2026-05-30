# Water Resource AI - Hybrid RAG GIS Dashboard

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_AI-8E75B2?style=for-the-badge&logo=google&logoColor=white)

An enterprise-grade Geographic Information System (GIS) chatbot built for government water resource management. This full-stack application utilizes a **Hybrid Retrieval-Augmented Generation (RAG)** architecture to eliminate LLM hallucinations, ensuring 100% mathematical accuracy for geographical data while providing a natural, voice-enabled user interface.

## Key Features

* **Native Voice Integration:** Built-in Speech-to-Text (STT) and Text-to-Speech (TTS) using native browser Web Speech APIs. No third-party voice APIs required.
* **Hybrid RAG Architecture:** Intelligently routes queries between Semantic Vector Search, a strict Knowledge Graph, and deterministic Pandas logic.
* **Deterministic Math Fallbacks:** Bypasses the LLM for quantitative queries (e.g., "largest", "deepest") using Pandas to sort millions of square meters of lake data accurately.
* **Engineering Suitability Engine:** Hardcoded engineering constraints evaluate if a specific location's area and depth are suitable for specific structures (e.g., Anicuts, Dams).
* **Typo Tolerance:** Custom fuzzy matching logic catches and corrects misspelled geographical names before they hit the database.

## Architecture Flow

1. **User Input:** User speaks or types a query into the React frontend.
2. **Preprocessing:** FastAPI backend receives the query, runs fuzzy matching, and extracts intent (coordinates, numbers, structural types).
3. **The "Traffic Cop" Router:**
   * **Route A (Math):** Intercepts "largest/smallest" queries and uses `Pandas` to sort `FINAL_WATER_BODIES.csv` mathematically.
   * **Route B (Engineering):** Compares user specs against `features.csv` to calculate structural suitability.
   * **Route C (Semantic Search):** Queries the `FAISS` Vector Database and `Knowledge Graph` for general location and context data.
4. **Generation:** The retrieved facts are packaged into a strict context prompt and sent to Google Gemini.
5. **Output:** Gemini generates a clean, human-readable response which is sent back to React and spoken aloud.

## Core Components

### Frontend (React)
* **`App.jsx`**: The main application wrapper. Manages the chat history state and handles the Text-to-Speech (TTS) browser synthesis.
* **`ChatInput.jsx`**: The custom voice-enabled command center. Utilizes the native Web Speech API to capture user voice, detect speech pauses for auto-submission, and handle UI state (like the pulsing microphone animation).
* **`App.css`**: Contains the custom styling for the chat interface, including the dynamic `keyframes` pulse animations for the active listening state.

### Backend (FastAPI / Python)
* **`api.py`**: The central API server and routing engine. Contains the Hybrid Router logic that intercepts mathematical queries (like "largest lake") to process them with Pandas before they reach the LLM.
* **`main.py`**: The data ingestion engine. Converts raw CSV geographical data into semantic English sentences and loads them into the FAISS vector database upon startup.
* **`rag/res_llm.py`**: The LLM interaction layer. Applies strict system prompts to the Gemini model, forcing it to answer concisely based *only* on retrieved context.

## Tech Stack

**Frontend:**
* React.js (Vite)
* Native Web Speech API (STT & TTS)
* CSS Modules / Custom UI

**Backend:**
* Python 3.10+
* FastAPI & Uvicorn
* Pandas (Data manipulation)

**AI & Data Pipeline:**
* Google Gemini (LLM Generation)
* FAISS (Vector Database)
* Custom JSON Knowledge Graph
* Text Embeddings

## 🔑 Environment Variables

To run this project, you will need to set up your API keys. 

Create a `.env` file in the root of your `backend` directory and add the following:

```env
GEMINI_API_KEY="your_google_gemini_api_key_here"
```
## 🚀 Getting Started

### Prerequisites
* Python 3.9+
* Node.js 18+
* A Google Gemini API Key

### 1. Backend Setup
Navigate to the backend directory and install dependencies:

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install fastapi "uvicorn[standard]" pandas faiss-cpu python-dotenv
```
Start the FastAPI server:
```bash
uvicorn api:app --reload
```
### 2. Frontend Setup
Open a new terminal, navigate to the frontend directory:
```bash
cd client
npm install
npm run dev
```
