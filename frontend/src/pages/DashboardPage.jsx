import React, { useState } from "react";
import GameController from "../components/game/GameController";
import ProjectProgress from "../components/tasks/ProjectProgress";
import StaffPanel from "../components/game/StaffPanel";
import GameSavePanel from "../components/layout/GameSavePanel";
import ResourcePanel from "../components/layout/ResourcePanel";

import Modal from "../components/layout/Modal"; // ✅ заменили EventModal
import { useTranslation } from "react-i18next";
import { useGame } from "../context/GameContext";

function DashboardPage() {
  const [eventData, setEventData] = useState(null);
  const { t } = useTranslation();
  const { simulateWeek } = useGame();

  const handleTriggerEvent = (event) => {
    setEventData(event);
  };

  return (
    <div className="main-wrapper">
      <h2 className="text-xl font-bold mb-4">🎯 {t("dashboardTitle")}</h2>

      <GameSavePanel />
      <ResourcePanel />

      <GameController onTriggerEvent={handleTriggerEvent} />
      <StaffPanel />
      <ProjectProgress />

      {eventData && (
        <Modal onClose={() => setEventData(null)}>
          <p>📣 Событие: <strong>{eventData.type}</strong></p>
        </Modal>
      )}
    </div>
  );
}

export default DashboardPage;
