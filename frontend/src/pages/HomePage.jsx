// src/pages/HomePage.jsx
import React from "react";
import { useTranslation } from "react-i18next";

function HomePage() {
  const { t } = useTranslation();

  return (
    <div className="main-wrapper">
      <h2>🏗️ {t("homeWelcome")}</h2>
      <p>{t("homeContinue")}</p>
    </div>
  );
}

export default HomePage;
