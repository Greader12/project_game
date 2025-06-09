import React from "react";

function ProjectInfoPanel({ week, budget, onNextWeek }) {
  return (
    <div style={{
      backgroundColor: "#222",
      padding: "15px",
      borderRadius: "10px",
      color: "#fff",
      marginBottom: "20px"
    }}>
      <h3>📊 Project Status</h3>
      <p>📆 Week: <strong>{week}</strong></p>
      <p>💰 Budget: <strong>${budget.toLocaleString()}</strong></p>
      <button onClick={onNextWeek}>➡️ Next Week</button>
    </div>
  );
}

export default ProjectInfoPanel;
