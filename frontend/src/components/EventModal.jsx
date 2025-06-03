import React from "react";

function EventModal({ event, onClose }) {
  if (!event) return null; // Если события нет, ничего не показывать

  return (
    <div style={styles.overlay}>
      <div style={styles.modal}>
        <h2>Event!</h2>
        <p>{event}</p>
        <button onClick={onClose} style={styles.button}>OK</button>
      </div>
    </div>
  );
}

const styles = {
  overlay: {
    position: "fixed",
    top: 0, left: 0, right: 0, bottom: 0,
    backgroundColor: "rgba(0,0,0,0.5)",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    zIndex: 1000
  },
  modal: {
    backgroundColor: "#fff",
    padding: 20,
    borderRadius: 8,
    textAlign: "center",
    minWidth: "300px"
  },
  button: {
    marginTop: 20,
    padding: "10px 20px",
    fontSize: "16px",
    cursor: "pointer"
  }
};

export default EventModal;
