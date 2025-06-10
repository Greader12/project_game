import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { register } from "../api/auth";
import { useTranslation } from "react-i18next";

function RegisterPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const { t } = useTranslation();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await register(username, password);
      alert(t("registerSuccess"));
      navigate("/login");
    } catch (error) {
      console.error('Registration failed:', error);
      alert(t("registerError"));
    }
  };

  return (
    <div>
      <h2>{t("register")}</h2>
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
        <button type="submit">{t("register")}</button>
      </form>
    </div>
  );
}

export default RegisterPage;
