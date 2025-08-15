import React from "react";

export default function AttendanceCard({ student }) {
  return (
    <>
      <div className="flex gap-5 relative w-full h-fit p-2 bg-[#e0e5ec] shadow-[5px_5px_8px_#bebebe,_-5px_-5px_8px_#ffffff] rounded-sm">
        <div
          className="bg-white w-[10%] aspect-square rounded-md shadow-[5px_5px_8px_#bebebe,_-5px_-5px_8px_#ffffff]"
          style={{
            backgroundImage: `url(data:image/jpeg;base64,${student.photo})`,
            backgroundSize: "cover",
            backgroundPosition: "center",
          }}
        ></div>
        <div>
          <h2 className="text-gray-600 text-2xl break-words whitespace-normal">{student.name}</h2>
          <p className="text-gray-600 break-words whitespace-normal">ID: {student.id}</p>
        </div>
      </div>
    </>
  );
}
