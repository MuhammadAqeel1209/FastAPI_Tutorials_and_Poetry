"use client";  // Add this line

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first!");
      return;
    }
  
    const formData = new FormData();
    formData.append("file", file);
  
    try {
      const res = await axios.post("http://127.0.0.1:8000/upload/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
  
      console.log("Upload Response:", res.data);  // Debugging log
      setResult(res.data);
    } catch (error) {
      console.error("Upload failed:", error);
      alert("Upload failed. Check the console for errors.");
    }
  };
  
  
  return (
    <div className="p-10">
      <h1 className="text-2xl font-bold">Resume Analyzer</h1>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload} className="bg-blue-500 text-white p-2 ml-2">
        Upload
      </button>
      {result && (
        <div className="mt-5">
          <h2 className="text-xl font-semibold">Analysis</h2>
          <p><b>File:</b> {result.filename}</p>
          <p><b>Word Count:</b> {result.analysis.word_count}</p>
          <p><b>Keywords:</b> {result.analysis.keywords.join(", ")}</p>
        </div>
      )}
    </div>
  );
}
