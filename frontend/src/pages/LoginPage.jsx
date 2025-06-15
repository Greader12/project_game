import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../api/auth";
import { useTranslation } from "react-i18next";

function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const { t } = useTranslation();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await login(username, password);
      navigate("/dashboard");
    } catch (error) {
      console.error('Login failed:', error);
      alert(t("loginError"));
    }
  };

  return (
    <div>
      <h2>{t("login")}</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder={t("username")}
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        /><br />
        <input
          type="password"
          placeholder={t("password")}
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        /><br />
        <button type="submit">{t("login")}</button>
      </form>
    </div>
  );
}

export default LoginPage;
