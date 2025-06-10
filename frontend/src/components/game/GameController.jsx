// src/components/game/GameController.jsx
import React from "react";
import { useGame } from "../../context/GameContext";
import { useTranslation } from "react-i18next";

function GameController({ onTriggerEvent }) {
  const { week, nextWeek } = useGame();
  const { t } = useTranslation();


  const handleNextWeek = () => {
    // Пример простого рандомного события
    if (Math.random() < 0.2) {
      const event = {
        title: "🚨 Unexpected Event!",
        description: "One of your staff members took a sudden leave.",
        impact: "-1 staff efficiency"
      };
      onTriggerEvent(event);
    }
    nextWeek();
  };

  return (
    <div style={{
      marginBottom: "20px",
      textAlign: "center"
    }}>
      <h3>🕓 Simulation Control</h3>
      <p>Current Week: <strong>{week}</strong></p>
      <button onClick={handleNextWeek} style={{
        padding: "10px 20px",
        backgroundColor: "#6b46c1",
        color: "#fff",
        border: "none",
        borderRadius: "5px",
        cursor: "pointer"
      }}>
        Advance to Next Week ➡️
      </button>
    </div>
  );
}

export default GameController;
