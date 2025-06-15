
import React, { createContext, useContext, useState } from "react";

const GameContext = createContext();

export function GameProvider({ children }) {
  const [week, setWeek] = useState(1);
  const [budget, setBudget] = useState(100000);
  const [staff, setStaff] = useState(generateStaff());
  const [tasks, setTasks] = useState(generateTasks());
  const [gameOver, setGameOver] = useState(false);

  function generateStaff() {
    const names = ["Ava", "Alex", "Olivia", "Noah", "Mason"];
    const professions = [
      { name: "Pilot", color: "blue" },
      { name: "Engineer", color: "orange" },
      { name: "Mission Specialist", color: "gray" },
      { name: "Medic", color: "green" },
      { name: "Scientist", color: "purple" }
    ];

    return names.map((name, i) => {
      const level = Math.ceil(Math.random() * 2);
      const cost = 900 + level * 100 + Math.floor(Math.random() * 200);
      return {
        id: i + 1,
        name,
        profession: professions[i].name,
        color: professions[i].color,
        level,
        costPerDay: cost,
        fatigue: 30 + Math.floor(Math.random() * 20),
        morale: 80 + Math.floor(Math.random() * 10),
      };
    });
  }

  function generateTasks() {
    const baseTasks = [
      "Design UI", "API Backend", "Frontend Integration",
      "Testing", "Deployment"
    ];

    return baseTasks.map((name, i) => ({
      id: i + 1,
      name,
      duration: 5 + Math.floor(Math.random() * 5),
      progress: 0,
      assignedStaffId: null
    }));
  }

  function assignStaffToTask(taskId, staffId) {
    setTasks(prev =>
      prev.map(task =>
        task.id === taskId ? { ...task, assignedStaffId: parseInt(staffId) } : task
      )
    );
  }

  function handleRest(staffId) {
    setStaff(prev =>
      prev.map(p =>
        p.id === staffId
          ? {
              ...p,
              fatigue: Math.max(0, p.fatigue - 30),
              morale: Math.min(100, p.morale + 20)
            }
          : p
      )
    );
  }

  function simulateWeek() {
    if (gameOver) return;

    const allDone = tasks.every(t => t.progress >= t.duration);
    if (budget <= 0 || allDone) {
      setGameOver(true);
      return;
    }

    setWeek(prev => prev + 1);

    setTasks(prevTasks =>
      prevTasks.map(task => {
        if (task.assignedStaffId && task.progress < task.duration) {
          const person = staff.find(s => s.id === task.assignedStaffId);
          if (!person) return task;

          let speed = 1 + 0.1 * person.level;
          if (task.name.includes(person.profession)) {
            speed *= 1.1;
          }

          const newProgress = task.progress + speed;
          return {
            ...task,
            progress: Math.min(newProgress, task.duration)
          };
        }
        return task;
      })
    );

    const dailyCost = staff.reduce((sum, p) => sum + p.costPerDay, 0);
    setBudget(prev => Math.max(0, prev - dailyCost));

    setStaff(prev =>
      prev.map(p => ({
        ...p,
        fatigue: Math.min(100, p.fatigue + 2),
        morale: Math.max(0, p.morale - 1)
      }))
    );
  }

  return (
    <GameContext.Provider
      value={{
        week,
        budget,
        staff,
        tasks,
        assignStaffToTask,
        simulateWeek,
        handleRest
      }}
    >
      {children}
    </GameContext.Provider>
  );
}

export function useGame() {
  return useContext(GameContext);
}
