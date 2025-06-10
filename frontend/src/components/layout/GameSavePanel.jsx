// src/components/layout/GameSavePanel.jsx
import React from "react";
import { useGame } from "../../context/GameContext";
import { useTranslation } from "react-i18next";

function GameSavePanel() {
  const { saveGame, loadGame } = useGame();
  const { t } = useTranslation();

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
        💾 {t("saveProgress")}
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
        📤 {t("loadProgress")}
      </button>
    </div>
  );
}

export default GameSavePanel;
