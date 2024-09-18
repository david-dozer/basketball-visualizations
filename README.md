# Basketball Performance Dashboard

## Overview

This is a basketball performance dashboard that allows you to visualize important team data regarding back-to-back (B2B) games. The application currently supports two types of visualizations:

1. **B2B Game Schedules**: Displays teams' back-to-back game schedules.
2. **B2B Win-Loss Records**: Displays the win-loss record for teams in back-to-back games.

To access these visuals, you'll need to log in with the appropriate credentials. Different users have access to different types of visuals.

## Features

- **Login-based access**: Each user is granted specific access to one of the visualizations based on their role.
- **B2B Game Schedule**: View a chart displaying each team's back-to-back game schedule.
- **B2B Win-Loss Record**: View a chart displaying how well teams perform in back-to-back games (wins and losses).

## Login Credentials

| Username  | Password     | Visualization                          |
|-----------|--------------|-----------------------------------------|
| user_one  | password123  | B2B Game Schedule (ScheduleB2BChart)    |
| user_two  | 123password  | B2B Win-Loss Record (WinLossB2BChart)   |

### Example Login:

- **User One**:
  - **Username**: `user_one`
  - **Password**: `password123`
  - Visualization: Displays the B2B Game Schedule.
  
- **User Two**:
  - **Username**: `user_two`
  - **Password**: `123password`
  - Visualization: Displays the B2B Win-Loss Record.

## Visualizations

### 1. **B2B Game Schedule (Available to user_one)**

- **Description**: This visualization shows a schedule of back-to-back (B2B) games for each NBA team. A B2B game is defined as two consecutive games played on consecutive days by the same team. This chart helps the user understand the team's schedule density and how frequently they are involved in B2B games.
  
- **How it works**: 
  - Each team is plotted on the X-axis.
  - The Y-axis represents the dates of the B2B games.
  - The chart highlights when teams play two games on consecutive days, which can affect team performance due to fatigue.

- **Component**: `ScheduleB2BChart.js`

### 2. **B2B Win-Loss Record (Available to user_two)**

- **Description**: This visualization shows the win-loss record for each team when they are involved in back-to-back (B2B) games. It gives insight into how teams perform under the pressure of playing consecutive games with no rest days in between.

- **How it works**:
  - The X-axis lists the teams.
  - The Y-axis shows the number of wins and losses in B2B games.
  - Each team has two bars: one for wins and one for losses, providing a clear view of their performance in B2B situations.

- **Component**: `WinLossB2BChart.js`

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>

2. **Run backend**:
```bash
   cd backend
   python app.py
```

3. **Run frontend**:
```bash
   cd frontend
   npm install 
   npm start
```

4. **Access the application**:
   - Open your web browser and navigate to `http://localhost:3000`
   - Use the following credentials to log in:
     - For B2B Game Schedule: 
       - Username: `user_one`
       - Password: `password123`
     - For B2B Win-Loss Record:
       - Username: `user_two`
       - Password: `123password`

## Usage

1. On the login page, enter the appropriate username and password based on which visualization you want to see.
2. After successful login, you will be presented with the corresponding visualization:
   - `user_one` will see the B2B Game Schedule
   - `user_two` will see the B2B Win-Loss Record
3. To switch between visualizations, you need to log out and log in with the other user's credentials.

Note: The application uses session-based authentication, so make sure your browser accepts cookies from localhost.

If the frontend does not load correctly, ensure that the backend server is running and accessible at http://localhost:5000.


