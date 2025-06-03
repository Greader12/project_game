import React, { useEffect, useState } from 'react';
import setupProject from './setupProject';
import createTask from './createTask';
import StaffPanel from './components/StaffPanel';
import ProjectProgress from './components/ProjectProgress';

function App() {
  const [projectId, setProjectId] = useState(null);
  const [currentWeek, setCurrentWeek] = useState(1);
  const [eventLog, setEventLog] = useState([]);

  useEffect(() => {
    async function initialize() {
      const id = await setupProject();
      await createTask(id);
      setProjectId(id);
    }
    initialize();
  }, []);

  useEffect(() => {
    if (!projectId) return;

    const timer = setInterval(() => {
      setCurrentWeek(prev => {
        const nextWeek = prev + 1;

        // 🎲 Проверка события только каждую 10ю неделю
        if (nextWeek % 10 === 0) {
          if (Math.random() < 0.2) { // 20% шанс события
            const events = ['Vacation', 'Sabotage', 'Motivation'];
            const randomEvent = events[Math.floor(Math.random() * events.length)];
            const eventMessage = `🎲 Неделя ${nextWeek}: Событие - ${randomEvent}`;
            alert(eventMessage);
            setEventLog(prevLog => [...prevLog, eventMessage]);
          }
        }

        return nextWeek;
      });
    }, 1000); // 1 неделя = 1 секунда

    return () => clearInterval(timer);
  }, [projectId]);

  if (!projectId) {
    return <p>⏳ Инициализация проекта...</p>;
  }

  return (
    <div className="App">
      <h2>📅 Текущая неделя: {currentWeek}</h2>
      <StaffPanel />
      <ProjectProgress projectId={projectId} />

      <div className="event-log">
        <h3>📝 Лог событий:</h3>
        <ul>
          {eventLog.map((event, index) => (
            <li key={index}>{event}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
