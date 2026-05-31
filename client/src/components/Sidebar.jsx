import React from "react";
import "./Sidebar.css";

const Sidebar = ({ startNewChat, chatSessions, loadSession, hasActiveMessages }) => {
  return (
    <div className="sidebar">
      
      <button className="new-chat-btn" onClick={startNewChat}>
        <span className="plus-icon">+</span> New Chat
      </button>

      <div className="history-container">
        <p className="history-title">Recent Conversations</p>
        
        {/* Show a 'Current Session' indicator if they are typing */}
        {hasActiveMessages && (
          <div className="history-item active">
            Current Session...
          </div>
        )}

        {/* Loop through the saved history array and display them */}
        {chatSessions.map((session) => (
          <div 
            key={session.id} 
            className="history-item"
            onClick={() => loadSession(session)}
            title={session.title} /* Shows full text on hover */
          >
            💬 {session.title}
          </div>
        ))}

        {/* Show this if history is completely empty */}
        {!hasActiveMessages && chatSessions.length === 0 && (
          <div style={{ color: '#475569', fontSize: '0.85rem', paddingLeft: '8px', marginTop: '10px' }}>
            No recent history.
          </div>
        )}
        
      </div>
    </div>
  );
};

export default Sidebar;