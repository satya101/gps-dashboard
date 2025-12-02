
import React, { useEffect, useState } from "react";
import axios from "axios";
import DeviceCard from "../components/DeviceCard";

export default function App() {
  const [devices, setDevices] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/devices").then(res => setDevices(res.data));
  }, []);

  return (
    <div className='p-6'>
      <h1 className='text-3xl font-bold mb-4'>GPS Dashboard</h1>
      <div className='grid grid-cols-1 md:grid-cols-3 gap-4'>
        {devices.map(d => <DeviceCard key={d} id={d} />)}
      </div>
    </div>
  );
}
