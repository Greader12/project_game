import React from 'react';
import StaffPanel from '../components/StaffPanel';
import ProjectProgress from '../components/ProjectProgress';

function ProjectDetailsPage() {
  return (
    <div style={{ padding: '20px' }}>
      <h2>Project Details</h2>
      {/* Панель сотрудников */}
      <div style={{ marginBottom: '20px' }}>
        <StaffPanel />
      </div>
      {/* Прогресс проекта */}
      <div>
        <ProjectProgress />
      </div>
    </div>
  );
}

export default ProjectDetailsPage;
