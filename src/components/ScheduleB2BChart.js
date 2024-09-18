import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

// Register necessary Chart.js components
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function ScheduleB2BChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('/api/b2b')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  const chartData = {
    labels: data.map(team => team[0]), // Team names
    datasets: [
      {
        label: 'Total B2B Games',
        data: data.map(team => team[3]), // Total B2B counts
        backgroundColor: 'rgba(75, 192, 192, 0.6)', // Green
      }
    ]
  };

  const options = {
    scales: {
      y: { beginAtZero: true }
    },
    plugins: {
      title: { display: true, text: 'Back-to-Back Games (Home, Away, and Total)' },
      legend: { position: 'top' }
    }
  };

  return (
    <div style={{ margin: '20px' }}>
      <Bar data={chartData} options={options} />
    </div>
  );
}

export default ScheduleB2BChart;
