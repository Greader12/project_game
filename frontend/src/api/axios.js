import axios from "axios";

const axiosInstance = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "/api",  // 🚀 <-- СЮДА
  withCredentials: true
});

// Подставляем токен при каждом запросе
axiosInstance.interceptors.request.use((config) => {
  const token = localStorage.getItem("access_token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Интерцептор для ответа — ловим 401 и обновляем токен
axiosInstance.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // Проверка: ошибка 401 и мы ещё не пробовали обновить токен
    if (error.response && error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      try {
        // Запрос на обновление токена
        const refreshResponse = await axios.post(
          import.meta.env.VITE_API_URL + '/token/refresh',
          {},
          { withCredentials: true }
        );
        const newToken = refreshResponse.data.access_token;

        // Сохраняем новый токен
        localStorage.setItem('access_token', newToken);

        // Обновляем заголовок в оригинальном запросе
        originalRequest.headers.Authorization = `Bearer ${newToken}`;

        // Повторяем оригинальный запрос
        return axiosInstance(originalRequest);
      } catch (refreshError) {
        // Не удалось обновить токен — разлогиниваем
        localStorage.removeItem('access_token');
        window.location.href = "/login";
        return Promise.reject(refreshError);
      }
    }

    // Если ошибка не 401 или повторный запрос тоже не удался
    return Promise.reject(error);
  }
);

export default axiosInstance;
