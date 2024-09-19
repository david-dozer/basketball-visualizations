import sqlite3

conn = sqlite3.connect('lac_fullstack_dev.db')
cursor = conn.cursor()

# 4a
# query = """WITH PlayerNames AS (
#     SELECT 
#         p.player_id, 
#         p.first_name || ' ' || p.last_name AS player_name
#     FROM player p
# ),
# LineupWithNames AS (
#     SELECT 
#         l.game_id, 
#         l.team_id, 
#         l.lineup_num, 
#         l.period, 
#         strftime('%M:%S', l.time_in, 'unixepoch') AS time_in, 
#         strftime('%M:%S', l.time_out, 'unixepoch') AS time_out,
#         pn.player_name,
#         ROW_NUMBER() OVER (PARTITION BY l.game_id, l.team_id, l.lineup_num, l.period ORDER BY l.time_in) AS player_position
#     FROM lineup l
#     LEFT JOIN PlayerNames pn ON l.player_id = pn.player_id
# )
# SELECT 
#     game_id, 
#     team_id, 
#     lineup_num, 
#     period, 
#     MAX(time_in) AS time_in, 
#     MAX(time_out) AS time_out,
#     MAX(CASE WHEN player_position = 1 THEN player_name END) AS player1,
#     MAX(CASE WHEN player_position = 2 THEN player_name END) AS player2,
#     MAX(CASE WHEN player_position = 3 THEN player_name END) AS player3,
#     MAX(CASE WHEN player_position = 4 THEN player_name END) AS player4,
#     MAX(CASE WHEN player_position = 5 THEN player_name END) AS player5
# FROM LineupWithNames
# GROUP BY game_id, team_id, lineup_num, period
# ORDER BY game_id, team_id, lineup_num, period;
# """

# 4b
# query = """WITH PlayerNames AS (
#     SELECT 
#         p.player_id, 
#         p.first_name || ' ' || p.last_name AS player_name
#     FROM player p
# ),
# GameInfo AS (
#     SELECT 
#         gs.game_id,
#         gs.game_date,
#         gs.home_id AS team_id,
#         gs.away_id AS opponent_id,
#         t.teamName AS team,
#         ot.teamName AS opponent
#     FROM game_schedule gs
#     JOIN team t ON gs.home_id = t.teamId
#     JOIN team ot ON gs.away_id = ot.teamId
# ),
# PlayerLineup AS (
#     SELECT 
#         l.game_id, 
#         l.team_id, 
#         l.lineup_num, 
#         l.period, 
#         strftime('%M:%S', l.time_in, 'unixepoch') AS time_in, 
#         strftime('%M:%S', l.time_out, 'unixepoch') AS time_out,
#         pn.player_name,
#         ROW_NUMBER() OVER (PARTITION BY l.game_id, l.team_id, l.player_id, l.period ORDER BY l.time_in) AS stint_number
#     FROM lineup l
#     LEFT JOIN PlayerNames pn ON l.player_id = pn.player_id
# ),
# StintDetails AS (
#     SELECT 
#         pl.game_id,
#         gi.game_date,
#         gi.team,
#         gi.opponent,
#         pl.player_name,
#         pl.period,
#         pl.stint_number,
#         MIN(pl.time_in) AS stint_start_time,
#         MAX(pl.time_out) AS stint_end_time
#     FROM PlayerLineup pl
#     JOIN GameInfo gi ON pl.game_id = gi.game_id AND pl.team_id = gi.team_id
#     GROUP BY pl.game_id, gi.team, gi.opponent, pl.player_name, pl.period, pl.stint_number
# )
# SELECT 
#     game_date,
#     team,
#     opponent,
#     player_name,
#     period,
#     stint_number,
#     stint_start_time,
#     stint_end_time
# FROM StintDetails
# ORDER BY game_date, team, period, stint_number;
# """
# 4c
# query = """WITH PlayerNames AS (
#     SELECT 
#         p.player_id, 
#         p.first_name || ' ' || p.last_name AS player_name
#     FROM player p
# ),
# GameInfo AS (
#     SELECT 
#         gs.game_id,
#         gs.game_date,
#         gs.home_id AS team_id,
#         gs.away_id AS opponent_id,
#         t.teamName AS team,
#         ot.teamName AS opponent
#     FROM game_schedule gs
#     JOIN team t ON gs.home_id = t.teamId
#     JOIN team ot ON gs.away_id = ot.teamId
# ),
# PlayerLineup AS (
#     SELECT 
#         l.game_id, 
#         l.team_id, 
#         l.lineup_num, 
#         l.period, 
#         (720 - l.time_in) AS stint_start_seconds, 
#         (720 - l.time_out) AS stint_end_seconds,
#         pn.player_name,
#         ROW_NUMBER() OVER (PARTITION BY l.game_id, l.team_id, l.player_id, l.period ORDER BY l.time_in) AS stint_number
#     FROM lineup l
#     LEFT JOIN PlayerNames pn ON l.player_id = pn.player_id
# ),
# StintDetails AS (
#     SELECT 
#         pl.game_id,
#         pl.player_name,
#         pl.period,
#         pl.stint_number,
#         (pl.stint_end_seconds - pl.stint_start_seconds) AS stint_length_seconds
#     FROM PlayerLineup pl
# )
# -- Calculate average number of stints and average stint length per player per game
# SELECT 
#     sd.game_id,
#     sd.player_name,
#     COUNT(sd.stint_number) AS total_stints,
#     AVG(sd.stint_length_seconds) AS avg_stint_length_seconds,
#     strftime('%M:%S', AVG(sd.stint_length_seconds), 'unixepoch') AS avg_stint_length_mmss
# FROM StintDetails sd
# GROUP BY sd.game_id, sd.player_name
# ORDER BY sd.game_id, sd.player_name;
# """

# 4d
# query = """
# WITH PlayerNames AS (
#     SELECT 
#         p.player_id, 
#         p.first_name || ' ' || p.last_name AS player_name
#     FROM player p
# ),
# GameInfo AS (
#     SELECT 
#         gs.game_id,
#         gs.game_date,
#         gs.home_id AS team_id,
#         gs.away_id AS opponent_id,
#         t.teamName AS team,
#         ot.teamName AS opponent,
#         CASE 
#             WHEN gs.home_score > gs.away_score THEN 'Win'
#             ELSE 'Loss'
#         END AS result
#     FROM game_schedule gs
#     JOIN team t ON gs.home_id = t.teamId
#     JOIN team ot ON gs.away_id = ot.teamId
# ),
# PlayerLineup AS (
#     SELECT 
#         l.game_id, 
#         l.team_id, 
#         l.lineup_num, 
#         l.period, 
#         (720 - l.time_in) AS stint_start_seconds, 
#         (720 - l.time_out) AS stint_end_seconds,
#         pn.player_name,
#         ROW_NUMBER() OVER (PARTITION BY l.game_id, l.team_id, l.player_id, l.period ORDER BY l.time_in) AS stint_number
#     FROM lineup l
#     LEFT JOIN PlayerNames pn ON l.player_id = pn.player_id
# ),
# StintDetails AS (
#     SELECT 
#         pl.game_id,
#         gi.game_date,
#         gi.team,
#         gi.opponent,
#         gi.result,
#         pl.player_name,
#         pl.period,
#         pl.stint_number,
#         (pl.stint_end_seconds - pl.stint_start_seconds) AS stint_length_seconds
#     FROM PlayerLineup pl
#     JOIN GameInfo gi ON pl.game_id = gi.game_id AND pl.team_id = gi.team_id
# )
# -- Calculate average number of stints and average stint length per player per game
# SELECT 
#     sd.player_name,
#     COUNT(DISTINCT sd.game_id) AS total_games,
#     ROUND(AVG(sd.stint_length_seconds), 3) AS avg_stint_length_seconds,
#     ROUND(AVG(sd.stint_number), 3) AS avg_stints_per_game,
#     COUNT(DISTINCT CASE WHEN sd.result = 'Win' THEN sd.game_id END) AS total_wins,
#     ROUND(AVG(CASE WHEN sd.result = 'Win' THEN sd.stint_length_seconds END), 3) AS avg_stint_length_seconds_wins,
#     ROUND(AVG(CASE WHEN sd.result = 'Win' THEN sd.stint_number END), 3) AS avg_stints_per_game_wins,
#     COUNT(DISTINCT CASE WHEN sd.result = 'Loss' THEN sd.game_id END) AS total_losses,
#     ROUND(AVG(CASE WHEN sd.result = 'Loss' THEN sd.stint_length_seconds END), 3) AS avg_stint_length_seconds_losses,
#     ROUND(AVG(CASE WHEN sd.result = 'Loss' THEN sd.stint_number END), 3) AS avg_stints_per_game_losses,
#     ROUND((AVG(CASE WHEN sd.result = 'Win' THEN sd.stint_length_seconds END) - AVG(CASE WHEN sd.result = 'Loss' THEN sd.stint_length_seconds END)), 3) AS diff_avg_stint_length_seconds,
#     ROUND((AVG(CASE WHEN sd.result = 'Win' THEN sd.stint_number END) - AVG(CASE WHEN sd.result = 'Loss' THEN sd.stint_number END)), 3) AS diff_avg_stints_per_game
# FROM StintDetails sd
# GROUP BY sd.player_name
# ORDER BY sd.player_name;
# """

cursor.execute(query)
results = cursor.fetchall()

# Write results to output.txt
with open('output.txt', 'w') as f:
    # Write header
    column_names = [description[0] for description in cursor.description]  # Get column names
    f.write(f"{' | '.join(column_names)}\n")  # Write header
    f.write('-' * (len(' | '.join(column_names))) + '\n')  # Separator line
    
    # Write data
    for row in results:
        f.write(f"{' | '.join(map(str, row))}\n")  # Convert each row to string and join

print("Results have been written to output.txt")

conn.close()