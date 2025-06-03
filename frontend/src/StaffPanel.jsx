import React from "react";

function StaffPanel({ staff, budget }) {
  return (
    <div>
      <h2>Your Resources</h2>
      <p>Your budget: ${budget.toLocaleString()}</p>
      <h3>Your staff:</h3>
      <ul>
        {staff.map((person, index) => (
          <li key={index}>
            {person.name} - {person.type}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default StaffPanel;
