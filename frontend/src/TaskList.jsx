import React, { useEffect, useState } from "react";
import axios from "./axios";

export default function TaskList() {
  const [tasks, setTasks] = useState([]);
  const [staff, setStaff] = useState([]);
  const [assignments, setAssignments] = useState({});
  const [newTask, setNewTask] = useState({ name: "", base_cost: "", base_duration: "" });

  useEffect(() => {
    fetchTasks();
    fetchStaff();
  }, []);

  const fetchTasks = async () => {
    try {
      const res = await axios.get("/api/project_tasks/1"); // id проекта
      setTasks(res.data);
    } catch (err) {
      console.error("Ошибка загрузки задач", err);
    }
  };

  const fetchStaff = async () => {
    try {
      const res = await axios.get("/api/staff");
      setStaff(res.data);
    } catch (err) {
      console.error("Ошибка загрузки сотрудников", err);
    }
  };

  const handleAssign = (taskId, staffId) => {
    setAssignments((prev) => ({
      ...prev,
      [taskId]: staffId,
    }));
  };

  const handleCreateTask = async () => {
    try {
      const projectId = 1; // пока фиксированно
      const response = await axios.post("/api/tasks", {
        ...newTask,
        project_id: projectId,
      });
      console.log("Task created:", response.data);
      window.location.reload(); // перезагрузка страницы
    } catch (error) {
      console.error("Ошибка создания задачи:", error);
    }
  };

  const getStaffName = (staffId) => {
    const s = staff.find((s) => s.id === parseInt(staffId));
    return s ? `${s.name} (${s.type})` : "-";
  };

  const calculate = (task, staffId) => {
    const s = staff.find((s) => s.id === parseInt(staffId));
    if (!s) return { duration: "-", cost: "-" };
    const duration = task.base_duration / s.speed_modifier;
    const cost = task.base_cost * s.cost_modifier;
    return { duration: duration.toFixed(1), cost: cost.toFixed(0) };
  };

  return (
    <div>
      <h2>📝 Project Tasks</h2>

      {/* Форма создания задачи */}
      <div style={{ marginBottom: "20px" }}>
        <h3>Создать новую задачу</h3>
        <input
          type="text"
          placeholder="Task Name"
          value={newTask.name}
          onChange={(e) => setNewTask({ ...newTask, name: e.target.value })}
        />
        <input
          type="number"
          placeholder="Base Cost"
          value={newTask.base_cost}
          onChange={(e) => setNewTask({ ...newTask, base_cost: e.target.value })}
        />
        <input
          type="number"
          placeholder="Base Duration"
          value={newTask.base_duration}
          onChange={(e) => setNewTask({ ...newTask, base_duration: e.target.value })}
        />
        <button onClick={handleCreateTask}>Add Task</button>
      </div>

      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>Task</th>
            <th>Assign Staff</th>
            <th>Duration</th>
            <th>Cost</th>
          </tr>
        </thead>
        <tbody>
          {tasks.map((task) => {
            const staffId = assignments[task.id];
            const result = staffId ? calculate(task, staffId) : { duration: "-", cost: "-" };
            return (
              <tr key={task.id}>
                <td>{task.name}</td>
                <td>
                  <select
                    value={staffId || ""}
                    onChange={(e) => handleAssign(task.id, e.target.value)}
                  >
                    <option value="">-- Select --</option>
                    {staff.map((s) => (
                      <option key={s.id} value={s.id}>
                        {s.name} ({s.type})
                      </option>
                    ))}
                  </select>
                </td>
                <td>{result.duration} weeks</td>
                <td>${result.cost}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
