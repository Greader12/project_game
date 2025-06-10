// src/components/game/GameController.jsx
import React from "react";
import { useGame } from "../../context/GameContext";
import { useTranslation } from "react-i18next";

function GameController({ onTriggerEvent }) {
  const { week, nextWeek } = useGame();
  const { t } = useTranslation();

  const handleNextWeek = () => {
    if (Math.random() < 0.2) {
      const event = {
        title: t("randomEventTitle"),
        description: t("randomEventDescription"),
        impact: t("randomEventImpact")
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
      <h3>🕓 {t("simulationControl")}</h3>
      <p>{t("currentWeek")}: <strong>{week}</strong></p>
      <button onClick={handleNextWeek} style={{
        padding: "10px 20px",
        backgroundColor: "#6b46c1",
        color: "#fff",
        border: "none",
        borderRadius: "5px",
        cursor: "pointer"
      }}>
        {t("nextWeek")}
      </button>
    </div>
  );
}

export default GameController;
