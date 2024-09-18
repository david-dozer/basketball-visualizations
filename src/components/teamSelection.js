import React, { useState, useEffect } from 'react';

function TeamSelection({ onSelectTeam }) {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('/api/teams') // Assuming there's an endpoint to get all NBA teams
      .then(response => response.json())
      .then(data => {
        // console.log('Teams data:', data); // Log the data to inspect its structure
        setTeams(data);
      });
  }, []);  

  return (
    <div>
      <h3>Select a Team</h3>
      <div className="team-selection">
        {teams.length > 0 && teams.map(team => (
          <button 
            key={team.teamId}          // Ensure each button has a unique key
            onClick={() => onSelectTeam(team[0])} // When clicked, pass the teamId
            className="team-button"
          >
            {/* {console.log('Team object:', team)}  */}
            {/* Log the team object to inspect its structure */}
            {team[1]}            {/* Display the teamName inside the button */}
          </button>
        ))}
      </div>
    </div>
  );
}

export default TeamSelection;
