import React, { useEffect, useState, useCallback } from "react";
import Swal from "sweetalert2";
import "./GameController.css";

const names = ["Alex", "Emma", "Liam", "Olivia", "Noah", "Ava", "Ethan", "Sophia", "Mason", "Isabella"];
const professions = [
  { name: "Engineer", color: "#FFA500" },
  { name: "Pilot", color: "#0000FF" },
  { name: "Medic", color: "#008000" },
  { name: "Scientist", color: "#800080" },
  { name: "Mission Specialist", color: "#808080" }
];

function GameController() {
  const [tasks, setTasks] = useState([]);
  const [staff, setStaff] = useState([]);
  const [currentDay, setCurrentDay] = useState(1);
  const [budget, setBudget] = useState(1000000);
  const [simulationRunning, setSimulationRunning] = useState(false);
  const [deadline, setDeadline] = useState(100); // 100 дней

  const randomInRange = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

  const generateStaff = () => {
    const availableNames = [...names];
    const availableProfessions = [...professions];
    const generated = [];

    while (generated.length < 5) {
      const nameIndex = Math.floor(Math.random() * availableNames.length);
      const professionIndex = Math.floor(Math.random() * availableProfessions.length);

      const name = availableNames.splice(nameIndex, 1)[0];
      const profession = availableProfessions.splice(professionIndex, 1)[0];

      const levelRand = Math.random();
      const level = levelRand < 0.8 ? 1 : levelRand < 0.95 ? 2 : 3;
      const baseCost = 1000 + (level - 1) * 500; // 1000/1500/2000
      const costPerDay = Math.floor(baseCost * (0.9 + Math.random() * 0.2)); // ±10%

      generated.push({
        id: generated.length + 1,
        name,
        profession: profession.name,
        color: profession.color,
        level,
        costPerDay,
        fatigue: 0,
        morale: 100
      });
    }
    return generated;
  };

  const generateTasks = () => {
    const taskNames = [
      "Assemble Command Module",
      "Calibrate Navigation Systems",
      "Test Communication Array",
      "Install Life Support",
      "Medical System Diagnostics"
    ];
    const availableProfessions = [...professions];

    return taskNames.map((task, index) => {
      let requiredProfession = null;
      if (Math.random() > 0.5) {
        const profIndex = Math.floor(Math.random() * availableProfessions.length);
        requiredProfession = availableProfessions.splice(profIndex, 1)[0].name;
      }
      return {
        id: index + 1,
        name: requiredProfession ? `(${requiredProfession}) ${task}` : task,
        requiredProfession,
        duration: randomInRange(10, 20), // дней
        progress: 0,
        completed: false,
        assignedStaffId: null
      };
    });
  };

  const handleAssignStaff = (taskId, staffId) => {
    setTasks(prevTasks =>
      prevTasks.map(task => (task.id === taskId ? { ...task, assignedStaffId: parseInt(staffId) } : task))
    );
  };

  const startSimulation = () => {
    setSimulationRunning(true);
  };

  const stopGame = useCallback((message) => {
    setSimulationRunning(false);
    Swal.fire({
      title: "Game Over",
      text: message,
      icon: "error",
      confirmButtonText: "OK"
    });
  }, []);

  const calculateSpeed = (person, task) => {
    let speed = 1;
    speed += 0.05 * person.level; // +5% за уровень
    if (task.requiredProfession && task.requiredProfession === person.profession) {
      speed *= 1.1; // +10% если профессия совпадает
    }
    return speed;
  };

  useEffect(() => {
    setStaff(generateStaff());
    setTasks(generateTasks());
  }, []);

  useEffect(() => {
    if (simulationRunning) {
      const timer = setInterval(() => {
        setCurrentDay(prevDay => {
          if (prevDay >= deadline) {
            stopGame("Deadline exceeded! You lose!");
            return prevDay;
          }
          return prevDay + 1;
        });

        setTasks(prevTasks => {
          const updatedTasks = prevTasks.map(task => {
            if (task.completed || task.assignedStaffId === null) return task;

            const person = staff.find(p => p.id === task.assignedStaffId);
            if (!person) return task;

            const speed = calculateSpeed(person, task);
            const newProgress = task.progress + speed;
            const isCompleted = newProgress >= task.duration;

            return {
              ...task,
              progress: isCompleted ? task.duration : newProgress,
              completed: isCompleted
            };
          });

          const allCompleted = updatedTasks.every(task => task.completed);
          if (allCompleted) {
            stopGame("Project completed successfully! You win!");
          }

          return updatedTasks;
        });

        setBudget(prevBudget => {
          const dailyCosts = staff.reduce((sum, person) => sum + person.costPerDay, 0);
          const newBudget = prevBudget - dailyCosts;
          if (newBudget <= 0) {
            stopGame("Budget exceeded! You lose!");
          }
          return newBudget;
        });

        setStaff(prevStaff =>
          prevStaff.map(person => ({
            ...person,
            fatigue: Math.min(person.fatigue + 2, 100),
            morale: Math.max(person.morale - 1, 0)
          }))
        );

      }, 1000);

      return () => clearInterval(timer);
    }
  }, [simulationRunning, staff, stopGame, deadline]);

  const handleRest = (id) => {
    setStaff(prevStaff =>
      prevStaff.map(person =>
        person.id === id
          ? { ...person, fatigue: Math.max(person.fatigue - 30, 0), morale: Math.min(person.morale + 20, 100) }
          : person
      )
    );
  };

  return (
    <div className="game-container">
      <h2>Current Day: {currentDay}</h2>
      <h3>Your Budget: ${budget.toLocaleString()}</h3>

      <div className="staff-grid">
        {staff.map(person => (
          <div className="staff-card" key={person.id} style={{ backgroundColor: person.color }}>
            <h3>⭐ {person.level} / {person.name} ({person.profession})</h3>
            <p>💰 Cost: ${person.costPerDay} per day</p>
            <p>🛌 Fatigue: {person.fatigue}%</p>
            <p>💡 Morale: {person.morale}%</p>
            <button onClick={() => handleRest(person.id)}>Rest</button>
          </div>
        ))}
      </div>

      <h3>Project Gantt Chart</h3>
      <table className="gantt-chart">
        <thead>
          <tr>
            <th>Task</th>
            <th>Duration</th>
            <th>Progress</th>
            <th>Assign Staff</th>
          </tr>
        </thead>
        <tbody>
          {tasks.map(task => (
            <tr key={task.id}>
              <td>{task.name}</td>
              <td>{task.duration} days</td>
              <td>
                <progress value={task.progress} max={task.duration}></progress>
              </td>
              <td>
                <select
                  value={task.assignedStaffId || ""}
                  onChange={(e) => handleAssignStaff(task.id, e.target.value)}
                >
                  <option value="">Assign?</option>
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

      {!simulationRunning && (
        <button onClick={startSimulation} className="start-button">Start Setup</button>
      )}
    </div>
  );
}

export default GameController;
