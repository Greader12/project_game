// src/components/layout/ResourcePanel.jsx
import React from "react";
import { useGame } from "../../context/GameContext";
import { useTranslation } from "react-i18next";

function ResourcePanel() {
  const { budget, week } = useGame();
  const { t } = useTranslation();

  return (
    <div className="bg-gray-800 text-white p-4 rounded-xl shadow mb-4">
      <h3 className="text-lg font-bold mb-2">📊 {t("resources")}</h3>
      <p className="mb-1">💰 {t("budget")}: <strong>${budget}</strong></p>
      <p>📅 {t("currentWeek")}: <strong>{week}</strong></p>
    </div>
  );
}

export default ResourcePanel;
