import React, { useEffect, useState } from "react";
import AttendanceCard from "./attendanceCard";
import scan from "/scan.png"

export default function Attendance() {
  const [employees, setEmployee] = useState([]);
  

  useEffect(() => {
    // Fetch employee data from the API or any other source
    fetch("http://192.168.100.210:5000/api/attendance")
      .then((response) => response.json())
      .then((data) => setEmployee(data))
      .catch((error) => console.error("Error fetching employee data:", error));
  }, []);

  return (
    <>
      <div className="text-black relative h-full">
        <h1>Attendance Status</h1>
        <button
          className=" bg-gray-100 z-10 rounded-full w-[8vw] aspect-square cursor-pointer hover:scale-110 transition-all duration-300 fixed bottom-10 right-10 text-7xl text-gray-600 flex justify-center items-center shadow-[5px_5px_8px_#bebebe,_-5px_-5px_10px_#ffffff]">
            <img src="/scan.png" alt="Scan Icon" className="w-[60%] h-[60%] object-contain" />
        </button>
        <div className="w-full flex flex-col gap-4 h-[80vh] ">
          {employees.map((emp, index) => (
            <AttendanceCard key={index} student={emp} />
          ))}
        </div>
      </div>
    </>
  );
}
