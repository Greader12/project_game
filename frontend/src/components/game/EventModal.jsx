// src/components/game/EventModal.jsx
import React from "react";
import { useTranslation } from "react-i18next";

function EventModal({ event, onClose }) {
  const { t } = useTranslation();

  return (
    <div style={{
      position: "fixed",
      top: 0, left: 0,
      width: "100vw",
      height: "100vh",
      backgroundColor: "rgba(0, 0, 0, 0.6)",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      zIndex: 1000
    }}>
      <div style={{
        background: "#2d2d3a",
        padding: "30px",
        borderRadius: "12px",
        boxShadow: "0 5px 15px rgba(0,0,0,0.5)",
        color: "#fff",
        maxWidth: "400px",
        textAlign: "center"
      }}>
        <h3>{event.title}</h3>
        <p>{event.description}</p>
        {event.impact && <p><strong>{t("impact")}:</strong> {event.impact}</p>}
        <button onClick={onClose} style={{
          marginTop: "20px",
          padding: "10px 20px",
          backgroundColor: "#805ad5",
          color: "#fff",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer"
        }}>
          {t("close")}
        </button>
      </div>
    </div>
  );
}

export default EventModal;
