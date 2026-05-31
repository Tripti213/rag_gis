import { useState } from "react"
import ChatContainer from "./components/ChatContainer"
import ChatInput from "./components/ChatInput"
import Header from "./components/Header"
import Sidebar from "./components/Sidebar"
import "./App.css"

function App() {
  const [messages, setMessages] = useState([])
  const [chatSessions, setChatSessions] = useState([]) // <-- NEW: Stores past chats
  const [isMuted, setIsMuted] = useState(false)

  // --- NEW: Session Management Logic ---
  const startNewChat = () => {
    // Only save to history if the user actually typed something
    if (messages.length > 0) {
      // Find the first thing the user said to use as the title
      const firstUserMsg = messages.find(m => m.role === "user")
      let title = firstUserMsg ? firstUserMsg.content : "New Conversation"
      
      // Keep title short (like ChatGPT does)
      if (title.length > 22) title = title.substring(0, 22) + "..."
      
      // Save it to the sidebar
      setChatSessions(prev => [{ id: Date.now(), title, messages }, ...prev])
    }
    // Clear the current screen
    setMessages([])
  }

  // --- NEW: Load old chat when clicked in sidebar ---
  const loadSession = (session) => {
    setMessages(session.messages)
  }

  const toggleMute = () => {
    setIsMuted(!isMuted)
    if (!isMuted) {
      window.speechSynthesis.cancel()
    }
  }

  const sendMessage = async (text) => {
    const userMsg = { role: "user", content: text }
    const historyPayload = messages.slice(-6);
    
    setMessages((prev) => [...prev, userMsg])

    try {
      const res = await fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          question: text,
          history: historyPayload 
        }),
      })

      const data = await res.json()
      const botMsg = { role: "assistant", content: data.answer }
      setMessages((prev) => [...prev, botMsg])

      if (!isMuted) {
        const cleanText = data.answer.replace(/[*#_]/g, "")
        const utterance = new SpeechSynthesisUtterance(cleanText)
        utterance.rate = 0.85; 
        utterance.pitch = 0.8;
        window.speechSynthesis.speak(utterance)
      }

    } catch (error) {
      console.error("Error communicating with backend:", error)
    }
  }

  return (
    <div className="app-container">
      
      {/* Pass the new session data to the Sidebar */}
      <Sidebar 
        startNewChat={startNewChat} 
        chatSessions={chatSessions} 
        loadSession={loadSession}
        hasActiveMessages={messages.length > 0}
      />

      <div className="main-chat-area">
        <Header isMuted={isMuted} toggleMute={toggleMute} />
        <ChatContainer messages={messages} />
        <ChatInput sendMessage={sendMessage} />
      </div>
      
    </div>
  )
}

export default App