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

// Register Chart.js components
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function WinLossB2BChart() {
  const [b2bData, setB2bData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch B2B win-loss data
  useEffect(() => {
    setLoading(true);
    fetch('/api/b2b_win_loss')
      .then(response => response.json())
      .then(data => {
        console.log('B2B Data:', data); // Inspect the data structure
        setB2bData(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching B2B data:', error);
        setError('Error fetching B2B data');
        setLoading(false);
      });
  }, []);

  // Chart data structure
  const chartData = {
    labels: b2bData.map(team => team[0]),  // Team names
    datasets: [
      {
        label: 'B2B Wins',
        data: b2bData.map(team => team[1]),  // B2B wins
        backgroundColor: 'rgba(75, 192, 192, 0.6)',  // Green for wins
      },
      {
        label: 'B2B Losses',
        data: b2bData.map(team => team[2]),  // B2B losses
        backgroundColor: 'rgba(255, 99, 132, 0.6)',  // Red for losses
      }
    ]
  };

  // Chart options
  const options = {
    scales: {
      y: { beginAtZero: true }
    },
    plugins: {
      title: { display: true, text: 'B2B Wins vs Losses for Teams' },
      legend: { position: 'top' }
    }
  };

  return (
    <div>
      {loading ? (
        <p>Loading B2B data...</p>
      ) : error ? (
        <p>{error}</p>
      ) : (
        b2bData.length > 0 ? (
          <div style={{ margin: '20px' }}>
            <h2>B2B Wins and Losses</h2>
            <Bar data={chartData} options={options} />
          </div>
        ) : (
          <p>No B2B data available.</p>
        )
      )}
    </div>
  );
}

export default WinLossB2BChart;
