// frontend/src/components/game/StaffPanel.jsx
import React, { useState } from "react";
import { useGame } from "../../context/GameContext";
import { useTranslation } from "react-i18next";

function StaffPanel() {
  const { staff, tasks, assignStaffToTask } = useGame();
  const [selectedTaskId, setSelectedTaskId] = useState(null);
  const { t } = useTranslation();


  return (
    <div className="p-4">
      <h3 className="text-xl font-bold mb-4">{t("staffManagement")}</h3>

      <div className="mb-4">
        <label className="mr-2 font-semibold">{t("selectTask")}</label>
        <select
          className="border rounded px-3 py-1"
          value={selectedTaskId || ""}
          onChange={(e) => setSelectedTaskId(Number(e.target.value))}
        >
          <option value="">{t("selectPlaceholder")}</option>
          {tasks.map((task) => (
            <option key={task.id} value={task.id}>
              {task.name}
            </option>
          ))}
        </select>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {staff.map((person, index) => (
          <div
            key={person.id}
            className="border border-gray-600 rounded-2xl shadow-md p-4 bg-gray-800 text-white"
            style={{
              borderLeft: `8px solid hsl(${(index * 60) % 360}, 70%, 50%)`,
            }}
          >
            <h4 className="text-lg font-bold mb-1">{person.name}</h4>
            <p>🚀 Скорость: {person.speed}</p>
            <p>💰 Стоимость: ${person.cost}</p>
            <button
              className="mt-3 bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded"
              onClick={() => {
                if (selectedTaskId) {
                  assignStaffToTask(selectedTaskId, person.id);
                } else {
                  alert(t("selectTaskFirst"));
                }
              }}
            >
             {t("assign")}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default StaffPanel;
