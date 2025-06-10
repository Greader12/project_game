// frontend/src/components/layout/ResourcePanel.jsx
import React from "react";
import { useGame } from "../../context/GameContext";

function ResourcePanel() {
  const { budget, staff } = useGame();

  const totalStaff = staff.length;
  const avgSpeed = (staff.reduce((sum, s) => sum + s.speed, 0) / totalStaff).toFixed(2);
  const totalCost = staff.reduce((sum, s) => sum + s.cost, 0);

  return (
    <div className="bg-gray-900 text-white p-4 rounded-2xl shadow mb-6">
      <h3 className="text-xl font-bold mb-2">📦 Ваши ресурсы</h3>
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 text-center">
        <div>
          <p className="text-sm text-gray-400">💰 Бюджет</p>
          <p className="text-lg font-semibold">${budget.toLocaleString()}</p>
        </div>
        <div>
          <p className="text-sm text-gray-400">👥 Сотрудников</p>
          <p className="text-lg font-semibold">{totalStaff}</p>
        </div>
        <div>
          <p className="text-sm text-gray-400">🚀 Средняя скорость</p>
          <p className="text-lg font-semibold">{avgSpeed}</p>
        </div>
        <div>
          <p className="text-sm text-gray-400">💸 Общая стоимость</p>
          <p className="text-lg font-semibold">${totalCost.toLocaleString()}</p>
        </div>
      </div>
    </div>
  );
}

export default ResourcePanel;
