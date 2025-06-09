import React, { useState } from "react";
import GameController from "../components/GameController";
import StaffPanel from "../components/StaffPanel";
import ProjectProgress from "../components/ProjectProgress";
import EventModal from "../components/EventModal";
import ProjectInfoPanel from "../components/ProjectInfoPanel";

function DashboardPage() {
  const [showEvent, setShowEvent] = useState(false);
  const [eventData, setEventData] = useState(null);
  const [week, setWeek] = useState(1);
  const [budget, setBudget] = useState(5000); // стартовый бюджет


  const handleTriggerEvent = (event) => {
    setEventData(event);
    setShowEvent(true);
  };

  return (
    <div className="main-wrapper">
      <h2>🎯 Project Dashboard</h2>

      {/* Компонент управления симуляцией (недели, события и т.д.) */}
      <GameController onTriggerEvent={handleTriggerEvent} />

      {/* Панель сотрудников */}
      <h3>Your Staff</h3>
      <StaffPanel />

      {/* Прогресс проекта (задачи) */}
      <h3>Project Progress</h3>
      <ProjectProgress />

      {/* События */}
      {showEvent && (
        <EventModal
          event={eventData}
          onClose={() => setShowEvent(false)}
        />
      )}
    </div>
  );
}

export default DashboardPage;
