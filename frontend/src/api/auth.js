import axios from "./axios";

export const login = async (username, password) => {
  const response = await axios.post("/login", { username, password });
  localStorage.setItem("access_token", response.data.access_token);
  return response.data;
};

export const register = async (username, password) => {
  return await axios.post("/register", { username, password });
};

export const logout = () => {
  localStorage.removeItem("access_token");
};
