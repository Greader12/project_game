// frontend/src/components/layout/LanguageSwitcher.jsx
import React, { useEffect, useState } from "react";
import { useTranslation } from "react-i18next";

function LanguageSwitcher() {
  const { i18n } = useTranslation();
  const [lang, setLang] = useState(() => localStorage.getItem("lang") || "ru");

  const toggleLanguage = () => {
    const newLang = lang === "ru" ? "en" : "ru";
    setLang(newLang);
    i18n.changeLanguage(newLang);
    localStorage.setItem("lang", newLang);
  };

  useEffect(() => {
    i18n.changeLanguage(lang);
  }, [lang, i18n]);

  return (
    <button
      onClick={toggleLanguage}
      className="px-3 py-1 bg-gray-700 text-white rounded hover:bg-gray-600 text-sm"
      title="Сменить язык"
    >
      🌐 {lang === "ru" ? "RU" : "EN"}
    </button>
  );
}

export default LanguageSwitcher;
