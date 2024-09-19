import sqlite3

conn = sqlite3.connect('lac_fullstack_dev.db')
cursor = conn.cursor()

#2a
# query = """
# WITH win_loss AS (
#     -- Calculate wins for home teams
#     SELECT
#         home_id AS team_id,
#         COUNT(CASE WHEN home_score > away_score THEN 1 END) AS wins,
#         COUNT(CASE WHEN home_score < away_score THEN 1 END) AS losses,
#         COUNT(*) AS games_played
#     FROM
#         game_schedule
#     GROUP BY
#         home_id

#     UNION ALL

#     -- Calculate wins for away teams
#     SELECT
#         away_id AS team_id,
#         COUNT(CASE WHEN away_score > home_score THEN 1 END) AS wins,
#         COUNT(CASE WHEN away_score < home_score THEN 1 END) AS losses,
#         COUNT(*) AS games_played
#     FROM
#         game_schedule
#     GROUP BY
#         away_id
# )

# -- Sum up total wins, losses, and games played for each team
# SELECT
#     t.teamName,
#     SUM(wl.games_played) AS games_played,
#     SUM(wl.wins) AS wins,
#     SUM(wl.losses) AS losses,
#     ROUND(SUM(wl.wins) * 1.0 / SUM(wl.games_played), 2) AS win_percentage
# FROM
#     win_loss wl
# JOIN
#     team t ON wl.team_id = t.teamId
# GROUP BY
#     t.teamName
# ORDER BY
#     win_percentage DESC;
# """

#2b
# query = """
# WITH win_loss_rank AS (
#     -- Calculate win-loss and total games played (home and away)
#     SELECT
#         t.teamName,
#         COUNT(g.game_id) AS games_played,
#         SUM(CASE WHEN g.home_id = t.teamId THEN 1 ELSE 0 END) AS home_games,
#         SUM(CASE WHEN g.away_id = t.teamId THEN 1 ELSE 0 END) AS away_games,
#         SUM(CASE WHEN g.home_score > g.away_score AND g.home_id = t.teamId THEN 1 ELSE 0 END +
#             CASE WHEN g.away_score > g.home_score AND g.away_id = t.teamId THEN 1 ELSE 0 END) AS wins,
#         SUM(CASE WHEN g.home_score < g.away_score AND g.home_id = t.teamId THEN 1 ELSE 0 END +
#             CASE WHEN g.away_score < g.home_score AND g.away_id = t.teamId THEN 1 ELSE 0 END) AS losses
#     FROM
#         team t
#     JOIN
#         game_schedule g ON t.teamId = g.home_id OR t.teamId = g.away_id
#     WHERE
#         strftime('%Y-%m', g.game_date) = '2024-01' -- Change '2024-01' to the target month
#     GROUP BY
#         t.teamName
# ),

# -- Ranking teams by games played, home games, and away games
# ranked AS (
#     SELECT
#         teamName,
#         games_played,
#         wins,
#         losses,
#         ROUND(wins * 1.0 / games_played, 2) AS win_percentage,
#         home_games,
#         away_games,
#         RANK() OVER (ORDER BY games_played DESC) AS rank_games_played,
#         RANK() OVER (ORDER BY home_games DESC) AS rank_home_games,
#         RANK() OVER (ORDER BY away_games DESC) AS rank_away_games
#     FROM
#         win_loss_rank
# )

# -- Final output with rankings and win-loss records
# SELECT
#     teamName,
#     games_played,
#     wins,
#     losses,
#     win_percentage,
#     home_games,
#     rank_home_games,
#     away_games,
#     rank_away_games,
#     rank_games_played
# FROM
#     ranked
# ORDER BY
#     win_percentage DESC;
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