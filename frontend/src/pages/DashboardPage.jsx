// src/pages/DashboardPage.jsx
import React, { useState } from "react";
import ProjectInfoPanel from "../components/layout/ProjectInfoPanel";
import GameController from "../components/game/GameController";
import EventModal from "../components/game/EventModal";
import ProjectProgress from "../components/tasks/ProjectProgress";
import StaffPanel from "../components/game/StaffPanel";
import GameSavePanel from "../components/layout/GameSavePanel";
import ResourcePanel from "../components/layout/ResourcePanel";
import Timeline from "../components/layout/Timeline";
import TaskGantt from "../components/tasks/TaskGantt";



function DashboardPage() {
  const [eventData, setEventData] = useState(null);

  const handleTriggerEvent = (event) => {
    setEventData(event);
  };

  return (
    <div className="main-wrapper">
      <h2>🎯 Project Dashboard</h2>
      <GameSavePanel />
      <ResourcePanel />
      <Timeline totalWeeks={20} />
      <TaskGantt totalWeeks={20} />



      {/* Панель информации о проекте */}
      <ProjectInfoPanel />

      {/* Управление неделями и событиями */}
      <GameController onTriggerEvent={handleTriggerEvent} />

      {/* Панель сотрудников */}
      <StaffPanel />

      {/* Прогресс задач */}
      <ProjectProgress />

      {/* Модальное окно события */}
      {eventData && (
        <EventModal event={eventData} onClose={() => setEventData(null)} />
      )}
    </div>
  );
}

export default DashboardPage;
