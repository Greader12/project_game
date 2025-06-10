import React from "react";
import { useGame } from "../../context/GameContext";

function ProjectInfoPanel() {
  const { week, budget, nextWeek } = useGame();

  return (
    <div style={{
      backgroundColor: "#222",
      padding: "20px",
      marginBottom: "20px",
      borderRadius: "10px",
      color: "#fff",
      display: "flex",
      justifyContent: "space-between",
      alignItems: "center"
    }}>
      <div>
        <h3>📊 Project Info</h3>
        <p>📅 Week: <strong>{week}</strong></p>
        <p>💰 Budget: <strong>${budget.toLocaleString()}</strong></p>
      </div>
      <div>
        <button onClick={nextWeek} style={{
          padding: "10px 20px",
          backgroundColor: "#6b46c1",
          color: "#fff",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer"
        }}>
          ➡️ Next Week
        </button>
      </div>
    </div>
  );
}

export default ProjectInfoPanel;
