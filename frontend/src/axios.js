import axios from 'axios';

export default axios.create({
  baseURL: 'http://localhost:5000',  // ✅ Бэкенд по адресу 5000 порт
  withCredentials: true // если есть сессии
});
