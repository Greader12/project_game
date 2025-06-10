// src/components/layout/GameSavePanel.jsx
import React from "react";
import { useGame } from "../../context/GameContext";

function GameSavePanel() {
  const { saveGame, loadGame } = useGame();

  return (
    <div style={{ margin: "20px 0", textAlign: "center" }}>
      <button
        onClick={saveGame}
        style={{
          marginRight: "10px",
          padding: "10px 20px",
          backgroundColor: "#38a169",
          color: "#fff",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer"
        }}
      >
        💾 Save Progress
      </button>
      <button
        onClick={loadGame}
        style={{
          padding: "10px 20px",
          backgroundColor: "#3182ce",
          color: "#fff",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer"
        }}
      >
        📤 Load Progress
      </button>
    </div>
  );
}

export default GameSavePanel;
