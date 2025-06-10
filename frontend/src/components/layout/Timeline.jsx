// frontend/src/components/layout/Timeline.jsx
import React from "react";
import { useGame } from "../../context/GameContext";
import { useTranslation } from "react-i18next";

function Timeline({ totalWeeks = 20 }) {
  const { t } = useTranslation();

  const { week, tasks, events = [] } = useGame(); // добавим events в контексте

  const weekMarks = Array.from({ length: totalWeeks }, (_, i) => i + 1);

  const hasEvent = (w) => events.some((e) => e.week === w);

  return (
    <div className="bg-gray-900 text-white p-4 rounded-xl shadow mb-6">
      <h3 className="text-lg font-bold mb-3">{t("timeline")}</h3>
      <div className="overflow-x-auto">
        <div className="flex space-x-2 text-sm">
          {weekMarks.map((w) => {
            const isCurrent = w === week;
            const hasEventThisWeek = hasEvent(w);

            return (
              <div
                key={w}
                className={`relative flex items-center justify-center w-10 h-10 rounded-full ${
                  isCurrent
                    ? "bg-purple-600 text-white font-bold scale-110"
                    : "bg-gray-700 text-gray-300"
                }`}
              >
                {w}
                    {hasEventThisWeek && (
                    <span
                        className="absolute -top-1 -right-1 text-lg"
                        title={t(events.find((e) => e.week === w)?.type || "eventOccurred")}
                    >
                        {(() => {
                        const event = events.find((e) => e.week === w);
                        switch (event?.type) {
                            case "fire":
                            return "🔥"; // болезнь
                            case "vacation":
                            return "🏖️"; // отпуск
                            case "motivation":
                            return "⚡"; // мотивация
                            case "conflict":
                            return "💢"; // конфликт
                            default:
                            return "❗";
                        }
                        })()}
                    </span>
                    )}

              </div>
            );
          })}
        </div>
      </div>
      <p className="text-right text-xs text-gray-400 mt-2">
        {t("currentWeek")}: {week}
      </p>
    </div>
  );
}

export default Timeline;
