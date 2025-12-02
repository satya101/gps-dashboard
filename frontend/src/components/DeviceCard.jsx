
import React, { useEffect, useState } from "react";
import axios from "axios";

export default function DeviceCard({ id }) {
  const [health, setHealth] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:8000/devices/${id}/gnss/health`).then(res => setHealth(res.data));
  }, []);

  return (
    <div className='bg-gray-800 p-4 rounded-xl shadow'>
      <h2 className='text-xl font-semibold mb-2'>{id}</h2>
      {health ? (
        <>
          <p>Total Records: {health.total}</p>
          <p>Bad Ratio: {(health.bad_ratio * 100).toFixed(1)}%</p>
          <p className={health.is_unhealthy ? "text-red-400" : "text-green-400"}>
            {health.is_unhealthy ? "UNHEALTHY" : "HEALTHY"}
          </p>
        </>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}
