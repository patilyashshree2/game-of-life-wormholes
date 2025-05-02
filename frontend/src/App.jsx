import React, { useState } from 'react';
import axios from 'axios';

export default function App() {
  const [files, setFiles] = useState({});
  const [images, setImages] = useState({});
  const [loading, setLoading] = useState(false);
  const backendURL = "https://your-backend-name.onrender.com";
  // const backendURL = "http://localhost:8000";


  const handleFileChange = (e) => {
    setFiles({ ...files, [e.target.name]: e.target.files[0] });
  };

  const handleSubmit = async () => {
    setLoading(true);
    const formData = new FormData();
    formData.append('starting_position', files.starting_position);
    formData.append('horizontal_tunnel', files.horizontal_tunnel);
    formData.append('vertical_tunnel', files.vertical_tunnel);
    
    const res = await axios.post(`${backendURL}/api/generate`, formData);
    const result = res.data;
    const imageMap = {};

    for (const iteration of Object.keys(result)) {
      const blobRes = await axios.get(`${backendURL}/${result[iteration]}`, {
        responseType: 'blob',
      });
      const url = URL.createObjectURL(blobRes.data);
      imageMap[iteration] = url;
    }

    setImages(imageMap);
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6 sm:p-8 md:p-10 lg:p-12">
      <div className="max-w-3xl mx-auto bg-white rounded-xl shadow-lg p-6 space-y-6">
        <h1 className="text-3xl font-bold text-center text-blue-700">Game of Life with Wormholes</h1>

        <div className="grid gap-4 sm:grid-cols-2">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1"> Starting Position </label>
            <input
              type="file"
              name="starting_position"
              accept="image/png"
              placeholder="Upload starting_position.png"
              onChange={handleFileChange}
              className="block w-full text-sm text-gray-600 file:mr-4 file:py-2 file:px-4
                         file:rounded file:border-0 file:text-sm file:font-semibold
                         file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
            />
          </div><br></br>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1"> Horizontal Tunnel </label>
            <input
              type="file"
              name="horizontal_tunnel"
              accept="image/png"
              placeholder="Upload horizontal_tunnel.png"
              onChange={handleFileChange}
              className="block w-full text-sm text-gray-600 file:mr-4 file:py-2 file:px-4
                         file:rounded file:border-0 file:text-sm file:font-semibold
                         file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
            />
          </div><br></br>

          <div className="sm:col-span-2">
            <label className="block text-sm font-medium text-gray-700 mb-1"> Vertical Tunnel </label>
            <input
              type="file"
              name="vertical_tunnel"
              accept="image/png"
              placeholder="Upload vertical_tunnel.png"
              onChange={handleFileChange}
              className="block w-full text-sm text-gray-600 file:mr-4 file:py-2 file:px-4
                         file:rounded file:border-0 file:text-sm file:font-semibold
                         file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
            />
          </div>
        </div><br></br>

        <button
          className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          onClick={handleSubmit}
          disabled={loading}
        >
          {loading ? "Generating..." : "Generate All Iterations"}
        </button>

        {loading && <p className="text-center text-blue-600 font-medium">Processing images, please wait...</p>}

        {Object.keys(images).length > 0 && (
          <div className="space-y-6">
            {["1", "10", "100", "1000"].map((iter) => (
              <div key={iter} className="border rounded-lg p-4 bg-gray-50">
                <h2 className="text-lg font-semibold text-gray-800 mb-2">After {iter} Iteration{iter > 1 ? 's' : ''}:</h2>
                <img
                  src={images[iter]}
                  alt={`Output after ${iter}`}
                  className="w-full max-w-full h-auto border rounded shadow"
                />
                <a
                  href={images[iter]}
                  download={`iteration_${iter}.png`}
                  className="inline-block mt-2 text-blue-600 font-medium underline"
                >
                  Download PNG
                </a>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}