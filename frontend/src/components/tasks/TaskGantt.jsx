// src/components/tasks/TaskGantt.jsx
import React, { useState, useEffect } from "react";
import { useGame } from "../../context/GameContext";
import { useTranslation } from "react-i18next";

function TaskGantt({ totalWeeks = 20 }) {
  const { tasks, week } = useGame();
  const { t } = useTranslation();
  const [filter, setFilter] = useState(() => localStorage.getItem("taskGanttFilter") || "all");

  useEffect(() => {
    localStorage.setItem("taskGanttFilter", filter);
  }, [filter]);

  const filteredTasks = tasks.filter((task) => {
    if (filter === "completed") return task.progress >= 100;
    if (filter === "inprogress") return task.progress > 0 && task.progress < 100;
    if (filter === "notstarted") return task.progress === 0;
    return true;
  });

  return (
    <div className="bg-gray-900 text-white p-4 rounded-xl shadow mb-6">
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-lg font-bold">🗂 {t("ganttTitle")}</h3>
        <select
          className="bg-gray-800 text-white px-3 py-1 rounded border border-gray-600"
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
        >
          <option value="all">{t("all")}</option>
          <option value="inprogress">{t("inprogress")}</option>
          <option value="completed">{t("completed")}</option>
          <option value="notstarted">{t("notstarted")}</option>
        </select>
      </div>

      {filteredTasks.length === 0 ? (
        <p className="text-sm text-gray-400">{t("noTasks")}</p>
      ) : (
        <div className="space-y-4">
          {filteredTasks.map((task, index) => {
            const start = task.startWeek || 0;
            const end = start + (task.duration || 1) - 1;
            const progressPercent = Math.min(task.progress ?? 0, 100);

            const barStart = `${(start / totalWeeks) * 100}%`;
            const barWidth = `${(task.duration / totalWeeks) * 100}%`;

            return (
              <div key={task.id}>
                <p className="mb-1">
                  <strong>{task.name}</strong> ({start}–{end})
                </p>
                <div className="relative w-full h-6 bg-gray-700 rounded overflow-hidden">
                  <div
                    className="absolute top-0 h-full bg-blue-500"
                    style={{
                      left: barStart,
                      width: barWidth,
                      opacity: 0.4,
                    }}
                  />
                  <div
                    className="absolute top-0 h-full bg-green-500 text-white text-xs text-center"
                    style={{
                      left: barStart,
                      width: `${(progressPercent / 100) * parseFloat(barWidth)}%`,
                      minWidth: "2rem",
                      lineHeight: "1.5rem",
                    }}
                  >
                    {Math.round(progressPercent)}%
                  </div>
                  <div
                    className="absolute top-0 bottom-0 w-1 bg-purple-400"
                    style={{
                      left: `${(week / totalWeeks) * 100}%`,
                    }}
                  />
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

export default TaskGantt;
