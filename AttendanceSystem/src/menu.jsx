import React, { useState, useEffect } from "react";
import "./menu.css";
import Attendance from "./attendance.jsx";

export default function Menu() {
  const [activePage, setActivePage] = useState(
    () => localStorage.getItem("activePage") || "dashboard"
  );

  // Update localStorage whenever activePage changes
  useEffect(() => {
    localStorage.setItem("activePage", activePage);
  }, [activePage]);

  const handleNavigation = () => {
    switch (activePage) {
      case "attendance":
        return <Attendance />;
      default:
        return <div>Welcome to the Dashboard</div>;
    }
  };

  return (
    <div className="grid-container">
      <div className="topHeader bg-gray-500 flex items-center px-[1%]">
        <h1>ABLAZA AIRCONDITIONING TRADING</h1>
      </div>

      <div className="sidebar bg-gray-300 px-[10%] py-[10%] text-gray-700 font-sans">
        <h1>Navigation</h1>
        <ul className="flex flex-col gap-4 mt-4 text-[1.2rem] text-gray-500 px-2.5">
          <li><button className="navBtn" onClick={() => setActivePage("dashboard")}>Dashboard</button></li>
          <li><button className="navBtn" onClick={() => setActivePage("attendance")}>Attendance</button></li>
        </ul>
      </div>

      <div className="main p-[2%] font-sans">
        {handleNavigation()}
      </div>
    </div>
  );
}
