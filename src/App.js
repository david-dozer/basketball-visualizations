import React, { useState, useEffect } from 'react';
import ScheduleB2BChart from './components/ScheduleB2BChart';
import WinLossB2BChart from './components/WinLossB2BChart';

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [role, setRole] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const login = (e) => {
    e.preventDefault();
    fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    })
      .then(res => res.json())
      .then(data => {
        if (data.role) {
          setLoggedIn(true);
          setRole(data.role);
        } else {
          alert("Invalid credentials");
        }
      });
  };

  const logout = () => {
    fetch('/api/logout', { method: 'POST' })
      .then(() => {
        setLoggedIn(false);
        setRole('');
      });
  };

  return (
    <div className="app-container" style={{ background: 'linear-gradient(black, darkgray)', color: 'white' }}>
      <header className="app-header" style={{ padding: '20px', textAlign: 'center', color: 'red' }}>
        <h1>Basketball Performance Dashboard</h1>
      </header>
      {!loggedIn ? (
        <form onSubmit={login} style={{ padding: '20px', textAlign: 'center' }}>
          <input 
            type="text" 
            placeholder="Username" 
            value={username} 
            onChange={e => setUsername(e.target.value)} 
            style={{ margin: '10px', padding: '5px' }}
          />
          <input 
            type="password" 
            placeholder="Password" 
            value={password} 
            onChange={e => setPassword(e.target.value)} 
            style={{ margin: '10px', padding: '5px' }}
          />
          <button type="submit" style={{ padding: '5px 10px' }}>Login</button>
        </form>
      ) : (
        <div style={{ padding: '20px' }}>
          <button onClick={logout} style={{ padding: '5px 10px' }}>Logout</button>
          {role === 'b2b' && <ScheduleB2BChart />}
          {role === 'b2b_win_loss' && <WinLossB2BChart />}
        </div>
      )}
    </div>
  );
}

export default App;
