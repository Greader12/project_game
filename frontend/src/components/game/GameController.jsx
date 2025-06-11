
import React from "react";
import { useGame } from "../../context/GameContext";

function GameController() {
  const {
    week,
    budget,
    staff,
    tasks,
    assignStaffToTask,
    simulateWeek,
    handleRest
  } = useGame();

  return (
    <div className="game-container">
      <h2>📅 Неделя: {week}</h2>
      <h3>💰 Бюджет: ${budget.toLocaleString()}</h3>

      <div className="staff-grid">
        {staff.map(person => (
          <div className="staff-card" key={person.id} style={{ backgroundColor: person.color }}>
            <h3>⭐ {person.level} / {person.name} ({person.profession})</h3>
            <p>💰 Стоимость: ${person.costPerDay} в день</p>
            <p>🛌 Усталость: {person.fatigue}%</p>
            <p>💡 Мораль: {person.morale}%</p>
            <button onClick={() => handleRest(person.id)}>Отдохнуть</button>
          </div>
        ))}
      </div>

      <h3>📈 Диаграмма проекта</h3>
      <table className="gantt-chart">
        <thead>
          <tr>
            <th>Задача</th>
            <th>Длительность</th>
            <th>Прогресс</th>
            <th>Назначение</th>
          </tr>
        </thead>
        <tbody>
          {tasks.map(task => (
            <tr key={task.id}>
              <td>{task.name}</td>
              <td>{task.duration} дней</td>
              <td>
                <progress value={task.progress} max={task.duration}></progress>
              </td>
              <td>
                <select
                  value={task.assignedStaffId || ""}
                  onChange={(e) => assignStaffToTask(task.id, e.target.value)}
                >
                  <option value="">Назначить</option>
                  {staff.map(person => (
                    <option key={person.id} value={person.id}>
                      {person.name}
                    </option>
                  ))}
                </select>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <button onClick={simulateWeek} className="start-button mt-4">▶ Следующая неделя</button>
    </div>
  );
}

export default GameController;
