import React from "react";
import "./attendanceCard.css"; // Assuming you have a CSS file for styling

export default function AttendanceCard({ student }) {
  return (
    <div className="attendance-card h-[18vw] bg-gray-200 shadow-lg w-fit p-4 rounded-lg">
      {student.photo && (
        <div className="photo-container w-[10vw] aspect-square  rounded-md mb-4" style={{ backgroundImage: `url(data:image/jpeg;base64,${student.photo})`, backgroundSize: 'cover', backgroundPosition: 'center' }}></div>
      )}
      <div className="flex flex-col mt-4 max-w-[10vw]">
        <h2 className="text-black break-words whitespace-normal">{student.name}</h2>
        <p className="text-gray-600">ID: {student.id}</p>
      </div>
    </div>
  );
}
