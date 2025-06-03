import React, { useEffect, useState } from 'react';
import axios from '../axios'; // твой axios
import './ProjectProgress.css'; // стили для панели

const ProjectProgress = ({ projectId }) => {
  const [progress, setProgress] = useState(null);

  useEffect(() => {
    fetchProjectProgress();
  }, [projectId]);

  const fetchProjectProgress = async () => {
    const response = await axios.get(`/api/finalize_project/${projectId}`);
    setProgress(response.data);
  };

  if (!progress) {
    return <p>Загрузка прогресса...</p>;
  }

  const costPercent = Math.min((progress.total_cost / progress.max_budget) * 100, 100);
  const durationPercent = Math.min((progress.total_duration / (progress.max_weeks * 7)) * 100, 100);

  return (
    <div className="project-progress">
      <h2>Прогресс проекта</h2>

      <div className="progress-bar">
        <p>💰 Бюджет: {progress.total_cost} / {progress.max_budget}</p>
        <div className="progress-track">
          <div className="progress-fill" style={{ width: `${costPercent}%` }}></div>
        </div>
      </div>

      <div className="progress-bar">
        <p>🕒 Длительность: {progress.total_duration} дней / {progress.max_weeks * 7} дней</p>
        <div className="progress-track">
          <div className="progress-fill" style={{ width: `${durationPercent}%` }}></div>
        </div>
      </div>

      <div className={`status ${progress.status === "Success" ? 'success' : 'failure'}`}>
        {progress.status === "Success" ? "✅ Проект успешен!" : "❌ Проект провален"}
      </div>
    </div>
  );
};

export default ProjectProgress;
