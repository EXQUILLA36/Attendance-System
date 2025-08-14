import { useState } from "react";
import defaultPhoto from "/images.png"; // Default photo path

export default function Modal({ onClose }) {
  const [photo, setPhoto] = useState(null);

  const handlePhotoChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setPhoto(reader.result);
      };
      reader.readAsDataURL(file);
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
              <button style={{backgroundImage: `url(${photo || defaultPhoto})`}} className="bg-cover bg-center bg-gray-200 w-[10vw] h-[10vw] rounded-md shadow-2xl cursor-pointer">
                <input
                  type="file"
                  accept="image/*"
                  onChange={handlePhotoChange}
                  className="w-full h-full opacity-0 cursor-pointer"
                />
              </button>
            </div>
          </div>

          {/* Close button */}
          <button
            onClick={onClose}
            className="bg-red-500 text-white px-4 py-2 rounded cursor-pointer hover:bg-red-600 transition-colors duration-300"
          >
            Close
          </button>
        </div>
      </div>
    </>
  );
}
