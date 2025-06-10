// frontend/src/components/tasks/ProjectProgress.jsx
import React, { useState } from "react";
import { useGame } from "../../context/GameContext";
import { useEffect } from "react";
import { useTranslation } from "react-i18next";


function ProjectProgress() {
  const { tasks, staff } = useGame();
  const { t } = useTranslation();
  const [filter, setFilter] = useState(() => localStorage.getItem("taskProgressFilter") || "all");
  useEffect(() => {
    localStorage.setItem("taskProgressFilter", filter);
  }, [filter]);

  const getStaffName = (id) => {
    const person = staff.find((s) => s.id === id);
    return person ? person.name : "—";
  };

  const filteredTasks = tasks.filter((task) => {
    if (filter === "completed") return task.progress >= 100;
    if (filter === "inprogress") return task.progress > 0 && task.progress < 100;
    if (filter === "notstarted") return task.progress === 0;
    return true;
  });

  return (
    <div className="p-4">
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-xl font-bold">{t("taskProgress")}</h3>
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
        <p className="text-sm text-gray-400">Нет задач для отображения.</p>
      ) : (
        <div className="overflow-x-auto">
          <table className="min-w-full border border-gray-700 text-white bg-gray-900 rounded-xl">
            <thead className="bg-gray-800 text-sm text-gray-300">
              <tr>
                <th className="p-2 text-left">{t("task")}</th>
                <th className="p-2 text-left">{t("duration")}</th>
                <th className="p-2 text-left">{t("progress")}</th>
                <th className="p-2 text-left">{t("assigned")}</th>
              </tr>
            </thead>
            <tbody>
              {filteredTasks.map((task) => (
                <tr key={task.id} className="border-t border-gray-700">
                  <td className="p-2">{task.name}</td>
                  <td className="p-2">{task.duration} недель</td>
                  <td className="p-2">
                    <div className="w-full bg-gray-700 rounded overflow-hidden h-6">
                      <div
                        className="bg-green-500 h-full text-sm text-center text-white transition-all"
                        style={{ width: `${task.progress}%` }}
                      >
                        {Math.round(task.progress)}%
                      </div>
                    </div>
                  </td>
                  <td className="p-2">{getStaffName(task.assignedStaffId)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default ProjectProgress;
