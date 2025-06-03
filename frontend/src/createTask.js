import axios from './axios';

async function createTask(projectId) {
  try {
    const response = await axios.post('/api/create_task', {
      name: 'Первая задача',
      base_duration: 10,
      base_cost: 10000,
      project_id: projectId,
      start_week: 1
    });
    console.log('✅ Задача создана!', response.data);
  } catch (err) {
    console.error('❌ Ошибка создания задачи:', err.message);
  }
}

export default createTask;
