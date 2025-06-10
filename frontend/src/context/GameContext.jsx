// src/context/GameContext.jsx
import axios from "../api/axios";
import React, { createContext, useContext, useState, useEffect } from "react";

const GameContext = createContext();

export function GameProvider({ children }) {
  const [week, setWeek] = useState(1);
  const [budget, setBudget] = useState(10000);
  
  const [staff, setStaff] = useState([
    { id: 1, name: "Alice", speed: 3, cost: 1000 },
    { id: 2, name: "Bob", speed: 2, cost: 800 },
    { id: 3, name: "Charlie", speed: 1, cost: 600 }
  ]);

  const [tasks, setTasks] = useState([
    { id: 1, name: "Design UI", duration: 6, progress: 0, assignedStaffId: null },
    { id: 2, name: "API Backend", duration: 8, progress: 0, assignedStaffId: null },
    { id: 3, name: "Frontend Integration", duration: 5, progress: 0, assignedStaffId: null }
  ]);

  const [events, setEvents] = useState([
    { week: 2, type: "fire" },
    { week: 5, type: "vacation" },
    { week: 6, type: "motivation" },
    { week: 8, type: "conflict" }
  ]);


  const assignStaffToTask = (taskId, staffId) => {
    setTasks(prevTasks =>
      prevTasks.map(task =>
        task.id === taskId ? { ...task, assignedStaffId: staffId } : task
      )
    );
  };

  const nextWeek = () => {
    setWeek(prev => prev + 1);

    setTasks(prevTasks => prevTasks.map(task => {
      if (!task.assignedStaffId) return task;
      const assigned = staff.find(s => s.id === task.assignedStaffId);
      const speed = assigned ? assigned.speed : 1;
      const newProgress = Math.min(task.progress + speed * 100 / task.duration, 100);
      return { ...task, progress: newProgress };
    }));

    setBudget(prev => prev - 500);
  };

  const saveGame = async () => {
    try {
      await axios.post("/save_game", {
        week, budget, staff, tasks
      });
      alert("Game progress saved successfully!");
    } catch (err) {
      console.error("Failed to save game:", err);
      alert("Error saving game.");
    }
  };

  const loadGame = async () => {
    try {
      const res = await axios.get("/load_game");
      const data = res.data;
      setWeek(data.week);
      setBudget(data.budget);
      setStaff(data.staff);
      setTasks(data.tasks);
      alert("Game progress loaded successfully!");
    } catch (err) {
      console.error("Failed to load game:", err);
      alert("Error loading game.");
    }
  };

    
  return (
    <GameContext.Provider
        value={{
          week, budget, staff, tasks, events,
          assignStaffToTask, nextWeek,
          saveGame, loadGame
        }}
    >
      {children}
    </GameContext.Provider>
  );
}

export function useGame() {
  return useContext(GameContext);
}
