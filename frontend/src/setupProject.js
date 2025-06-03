import axios from './axios';

const username = 'testuser';
const password = 'testpass';
const projectName = 'Мой проект';
const budget = 1000000;

async function setupProject() {
  try {
    await axios.post('/api/register', { username, password });
    console.log('✅ Пользователь зарегистрирован!');
  } catch (err) {
    if (err.response && err.response.status === 409) {
      console.log('ℹ️ Пользователь уже существует, пропускаем регистрацию');
    } else {
      console.error('❌ Ошибка регистрации:', err.message);
      return;
    }
  }

  try {
    await axios.post('/api/login', { username, password });
    console.log('✅ Успешный вход!');
  } catch (err) {
    console.error('❌ Ошибка входа:', err.message);
    return;
  }

  try {
    const response = await axios.post('/api/create_project', { name: projectName, budget });
    const projectId = response.data.project_id;
    console.log('✅ Проект создан с ID:', projectId); // 👈
    return projectId;
  } catch (err) {
    console.error('❌ Ошибка создания проекта:', err.message);
  }
}

export default setupProject;
