import React from "react";

function GanttChart({ tasks = [], staff = [], assignStaffToTask }) {
  if (!tasks.length || !staff.length) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Project Gantt Chart</h2>
      <table>
        <thead>
          <tr>
            <th>Task</th>
            <th>Start Week</th>
            <th>Duration</th>
            <th>Progress</th>
            <th>Assign Staff</th>
          </tr>
        </thead>
        <tbody>
          {tasks.map((task) => (
            <tr key={task.id}>
              <td>{task.name}</td>
              <td>{task.start_week}</td>
              <td>{task.base_duration} weeks</td>
              <td>
                {task.progress}/{task.base_duration}
              </td>
              <td>
                <select
                  value={task.assignedStaffId || ""}
                  onChange={(e) => assignStaffToTask(task.id, parseInt(e.target.value))}
                >
                  <option value="">Assign?</option>
                  {staff.map((person) => (
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
    </div>
  );
}

export default GanttChart;