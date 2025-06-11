import React, { useEffect, useState } from 'react';
import axios from "../../api/axios"; // Подключи твой axios файл
import Modal from "../layout/Modal"; // Подключение модалки
import './StaffPanel.css'; // Стили для карточек

const StaffPanel = () => {
  const [staffList, setStaffList] = useState([]);
  const [selectedStaff, setSelectedStaff] = useState(null);
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    fetchStaff();
  }, []);

  const fetchStaff = async () => {
    const response = await axios.get('/api/staff');
    setStaffList(response.data);
  };

  const handleCompleteTask = async (staffId) => {
    const response = await axios.post('/api/complete_task', { staff_id: staffId });
    if (response.data.level) {
      const upgradedStaff = staffList.find(s => s.id === staffId);
      setSelectedStaff(upgradedStaff);
      setShowModal(true);
    }
    fetchStaff();
  };

  const handleUpgrade = async (type) => {
    if (selectedStaff) {
      await axios.post('/api/upgrade_skill', {
        staff_id: selectedStaff.id,
        upgrade: type
      });
      setShowModal(false);
      fetchStaff();
    }
  };

  return (

      <div className="staff-grid">
        {staffList.map(staff => (
          <div key={staff.id} className="staff-card">
            <h3>{staff.name}</h3>
            <p>🏅 Уровень: {staff.level}</p>
            <div className="xp-bar">
              <div
                className="xp-progress"
                style={{ width: `${staff.xp}%` }}
              ></div>
            </div>
            <p>💡 Мораль: {staff.morale}%</p>
            <p>🔥 Усталость: {staff.fatigue}%</p>
            <p>💰 Стоимость в день: ${Number(staff.cost || 0).toFixed(2)}</p>
            <button onClick={() => handleCompleteTask(staff.id)}>Выполнить задачу</button>
          </div>
        ))}

      {showModal && selectedStaff && (
        <Modal open={true} onClose={() => setShowModal(false)}>
          <h2>🎉 {selectedStaff.name} повысил уровень!</h2>
          <p>Выберите улучшение:</p>
          <button onClick={() => handleUpgrade('speed')}>+10% Скорость</button>
          <button onClick={() => handleUpgrade('cost')}>-5% Стоимость</button>
          <button onClick={() => handleUpgrade('morale')}>+5% Мораль</button>
        </Modal>
      )}
    </div>
  );
};

export default StaffPanel;