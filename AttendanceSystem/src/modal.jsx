import { useState } from "react";
import defaultPhoto from "/images.png"; // Default photo path

export default function Modal({ onClose }) {
  const [photo, setPhoto] = useState(null);
  const [photoFile, setPhotoFile] = useState(null);
  const [employeeId, setEmployeeId] = useState("");
  const [employeeName, setEmployeeName] = useState("");
  const [employeeRate, setEmployeeRate] = useState("");

  const handlePhotoChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setPhotoFile(file);

      // for preview only
      const reader = new FileReader();
      reader.onloadend = () => {
        setPhoto(reader.result); // preview image base64 string
      };
      reader.readAsDataURL(file);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!photoFile || !employeeName || !employeeId || !employeeRate) {
      return; // or show your validation error
    }

    const formData = new FormData();
    formData.append("photo", photoFile);
    formData.append("employeeName", employeeName);
    formData.append("employeeId", employeeId);
    formData.append("employeeRate", employeeRate);

    try {
      const response = await fetch("http://192.168.100.210:5001/api/upload", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        console.log("Upload successful!");
        window.location.reload();
        onClose();
      } else {
        console.log("Upload failed.");
      }
    } catch (error) {
      console.error("Upload error:", error);
    }
  };

  return (
    <>
      <div className="fixed inset-0 backdrop-blur-xs bg-opacity-50 flex justify-center items-center">
        {/* Modal content */}
        <div className="bg-white p-6 rounded shadow-lg w-1/3 text-gray-600">
          <div>
            <h2 className="text-xl font-bold mb-4">Add New Employee</h2>

            <div className="flex flex-col gap-4 my-5">
              <form onSubmit={handleSubmit} className="flex flex-col gap-2">
                <div className="flex flex-row gap-4">
                  <div className="w-[40%] aspect-square shadow-black shadow-md rounded-md hover:scale-105 transition-all duration-300">
                    <button
                      style={{
                        backgroundImage: `url(${photo || defaultPhoto})`,
                      }}
                      className="bg-cover bg-center relative bg-gray-200 w-full h-full rounded-md shadow-2xl cursor-pointer "
                    >
                      <input
                        type="file"
                        accept="image/*"
                        onChange={handlePhotoChange}
                        className="w-full h-full opacity-0 cursor-pointer"
                      />
                    </button>
                  </div>

                  <div className="flex flex-col relative w-[80%] justify-between">
                    <input
                      className="w-full h-10 rounded-sm border-1 px-2"
                      type="text"
                      placeholder="Enter Employee Name"
                      value={employeeName}
                      onChange={(e) => setEmployeeName(e.target.value)}
                    />
                    <input
                      className="w-full h-10 rounded-sm border-1 px-2"
                      type="text"
                      placeholder="Enter Employee Id"
                      value={employeeId}
                      onChange={(e) => setEmployeeId(e.target.value)}
                    />
                    <input
                      className="w-full h-10 rounded-sm border-1 px-2"
                      type="text"
                      placeholder="Enter Employee Rate"
                      value={employeeRate}
                      onChange={(e) => setEmployeeRate(e.target.value)}
                    />
                  </div>
                </div>
                <div className="flex gap-2 justify-end">
                  <button
                    type="submit"
                    className="bg-green-500 text-white px-5 py-2 rounded cursor-pointer hover:bg-green-600 transition-colors duration-300"
                  >
                    Add
                  </button>
                  <button
                    onClick={onClose}
                    className="bg-red-500 text-white px-4 py-2 rounded cursor-pointer hover:bg-red-600 transition-colors duration-300"
                  >
                    Close
                  </button>
                </div>
              </form>
            </div>
          </div>

          {/* Close / Add button */}
        </div>
      </div>
    </>
  );
}
