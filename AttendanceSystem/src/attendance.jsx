import React, { useEffect, useState } from "react";
import "./attendance.css";
import Modal from "./modal";

import AttendanceCard from "./attendanceCard";

export default function Attendance() {
  const [employees, setEmployee] = useState([]);

  const [isOpen, setisOpen] = useState(false);

  useEffect(() => {
    // Fetch employee data from the API or any other source 
    fetch( "http://192.168.100.210:5000/api/attendance")
      .then((response) => response.json())
      .then((data) => setEmployee(data))
      .catch((error) => console.error("Error fetching employee data:", error));
  }, []);
  
  return (
    <>
      <div className="flex flex-col gap-4 ">
        <h1 className="text-black">Employee List</h1>
        <button
          onClick={() => setisOpen(true)} 
          className=" bg-gray-200 rounded-full w-[5vw] h-[5vw] shadow-lg cursor-pointer hover:scale-110 transition-all duration-300 fixed bottom-10 right-10 text-7xl text-gray-600 flex justify-center items-center pb-3">
          +
        </button>

        {isOpen && <Modal onClose={() => setisOpen(false)} />
          }
        <div className="flex flex-row gap-4 justify-between flex-wrap overflow-y-auto">
          {employees.map((emp, index) => (
            <AttendanceCard key={index} student={emp} />
          ))}
        </div>
      </div>
    </>
  );
}
