import sqlite3
import json
import os

# Define file paths
directory_path = 'dev_test_data'  # Directory containing your JSON files

file_paths = {
    'team': os.path.join(directory_path, 'team.json'),
    'team_affiliate': os.path.join(directory_path, 'team_affiliate.json'),
    'game_schedule': os.path.join(directory_path, 'game_schedule.json'),
    'player': os.path.join(directory_path, 'player.json'),
    'roster': os.path.join(directory_path, 'roster.json'),
    'lineup': os.path.join(directory_path, 'lineup.json')  # Include the lineup.json file path
}

# Initialize database connection
conn = sqlite3.connect('lac_fullstack_dev.db')  # This will create a file named 'lac_fullstack_dev.db'
cursor = conn.cursor()

# Create table schemas
schemas = {
    'team': '''
        CREATE TABLE IF NOT EXISTS team (
            teamId INTEGER PRIMARY KEY,
            leagueLk TEXT,
            teamName TEXT,
            teamNameShort TEXT,
            teamNickname TEXT
        );
    ''',
    'team_affiliate': '''
        CREATE TABLE IF NOT EXISTS team_affiliate (
            nba_teamId INTEGER,
            nba_abrv TEXT,
            glg_teamId INTEGER,
            glg_abrv TEXT,
            PRIMARY KEY (nba_teamId, glg_teamId)
        );
    ''',
    'game_schedule': '''
        CREATE TABLE IF NOT EXISTS game_schedule (
            game_id INTEGER PRIMARY KEY,
            home_id INTEGER,
            home_score INTEGER,
            away_id INTEGER,
            away_score INTEGER,
            game_date TEXT
        );
    ''',
    'player': '''
        CREATE TABLE IF NOT EXISTS player (
            player_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT
        );
    ''',
    'roster': '''
        CREATE TABLE IF NOT EXISTS roster (
            team_id INTEGER,
            player_id INTEGER,
            first_name TEXT,
            last_name TEXT,
            position TEXT,
            contract_type TEXT,
            PRIMARY KEY (team_id, player_id)
        );
    ''',
    'lineup': '''
        CREATE TABLE IF NOT EXISTS lineup (
            team_id INTEGER,
            player_id INTEGER,
            lineup_num INTEGER,
            period INTEGER,
            time_in REAL,
            time_out REAL,
            game_id INTEGER,
            PRIMARY KEY (team_id, player_id, lineup_num, game_id)
        );
    '''
}

# Execute table creation
for table_name, schema in schemas.items():
    cursor.execute(schema)

# Function to load JSON data into tables
def load_data_into_table(file_path, table_name):
    with open(file_path, 'r') as f:
        data = json.load(f)
        if isinstance(data, dict):
            data = [data]  # Ensure it's a list of dictionaries
        if data:
            # Dynamically get columns from the first item in the data
            columns = ', '.join(data[0].keys())
            placeholders = ', '.join('?' * len(data[0]))

            # Insert the data
            insert_query = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
            for row in data:
                cursor.execute(insert_query, tuple(row.values()))

# Load data into respective tables
for table_name, file_path in file_paths.items():
    load_data_into_table(file_path, table_name)

# Commit and close the connection
conn.commit()
conn.close()

print("Database creation and data insertion completed.")
