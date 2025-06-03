import React, { useState } from "react";
import axios from "axios";

function CreateProject() {
  const [name, setName] = useState('');
  const [budget, setBudget] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('/api/create_project', {
        name: name,
        budget: parseInt(budget)
      }, { withCredentials: true });

      alert('Project created with ID: ' + response.data.project_id);
    } catch (error) {
      console.error(error);
      alert('Failed to create project');
    }
  };

  return (
    <div>
      <h2>Create New Project</h2>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          placeholder="Project Name" 
          value={name}
          onChange={(e) => setName(e.target.value)}
        /><br/>
        <input 
          type="number" 
          placeholder="Budget" 
          value={budget}
          onChange={(e) => setBudget(e.target.value)}
        /><br/>
        <button type="submit">Create Project</button>
      </form>
    </div>
  );
}

export default CreateProject;
