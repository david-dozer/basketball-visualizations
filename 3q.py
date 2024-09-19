import sqlite3

conn = sqlite3.connect('lac_fullstack_dev.db')
cursor = conn.cursor()
#3a
# query = """WITH b2b_games_home AS (
#     -- Find consecutive home games (Home-Home B2Bs)
#     SELECT
#         g1.home_id AS team_id,
#         g1.game_date AS game1_date,
#         g2.game_date AS game2_date,
#         julianday(g2.game_date) - julianday(g1.game_date) AS days_diff,
#         'Home' AS b2b_type
#     FROM
#         game_schedule g1
#     JOIN
#         game_schedule g2 ON g1.home_id = g2.home_id
#     WHERE
#         g1.game_id <> g2.game_id
#         AND julianday(g2.game_date) - julianday(g1.game_date) = 1 -- Back-to-back games
#         AND g1.home_id = g2.home_id -- Home-Home games
# )

# -- Count and sort by Home-Home B2Bs
# SELECT
#     t.teamName,
#     COUNT(*) AS home_b2b_count
# FROM
#     b2b_games_home b2b
# JOIN
#     team t ON b2b.team_id = t.teamId
# GROUP BY
#     b2b.team_id
# ORDER BY
#     home_b2b_count DESC;
# """
#3a away
# query = """WITH b2b_games_away AS (
#     -- Find consecutive away games (Away-Away B2Bs)
#     SELECT
#         g1.away_id AS team_id,
#         g1.game_date AS game1_date,
#         g2.game_date AS game2_date,
#         julianday(g2.game_date) - julianday(g1.game_date) AS days_diff,
#         'Away' AS b2b_type
#     FROM
#         game_schedule g1
#     JOIN
#         game_schedule g2 ON g1.away_id = g2.away_id
#     WHERE
#         g1.game_id <> g2.game_id
#         AND julianday(g2.game_date) - julianday(g1.game_date) = 1 -- Back-to-back games
#         AND g1.away_id = g2.away_id -- Away-Away games
# )

# -- Count and sort by Away-Away B2Bs
# SELECT
#     t.teamName,
#     COUNT(*) AS away_b2b_count
# FROM
#     b2b_games_away b2b
# JOIN
#     team t ON b2b.team_id = t.teamId
# GROUP BY
#     b2b.team_id
# ORDER BY
#     away_b2b_count DESC;
# """

#3b
# query = """WITH team_games AS (
#     -- Get all games (home and away) for each team
#     SELECT
#         home_id AS team_id,
#         game_id,
#         game_date
#     FROM
#         game_schedule
#     UNION ALL
#     SELECT
#         away_id AS team_id,
#         game_id,
#         game_date
#     FROM
#         game_schedule
# ),

# team_game_intervals AS (
#     -- Calculate the difference in days between consecutive games for each team
#     SELECT
#         tg.team_id,
#         t.teamName,
#         tg.game_id AS game1_id,
#         tg.game_date AS game1_date,
#         LEAD(tg.game_id) OVER (PARTITION BY tg.team_id ORDER BY tg.game_date) AS game2_id,
#         LEAD(tg.game_date) OVER (PARTITION BY tg.team_id ORDER BY tg.game_date) AS game2_date,
#         julianday(LEAD(tg.game_date) OVER (PARTITION BY tg.team_id ORDER BY tg.game_date)) -
#         julianday(tg.game_date) AS rest_days
#     FROM
#         team_games tg
#     JOIN
#         team t ON tg.team_id = t.teamId
# ),

# longest_rest AS (
#     -- Find the maximum rest period for each team
#     SELECT
#         team_id,
#         teamName,
#         game1_date,
#         game2_date,
#         rest_days
#     FROM
#         team_game_intervals
#     WHERE
#         rest_days IS NOT NULL
# )

# -- Select the team(s) with the longest rest
# SELECT
#     teamName,
#     game1_date AS first_game_date,
#     game2_date AS second_game_date,
#     rest_days
# FROM
#     longest_rest
# WHERE
#     rest_days = (SELECT MAX(rest_days) FROM longest_rest)
# ORDER BY
#     teamName;
# """

#3c
# query = """WITH team_games AS (
#     -- Get all games (home and away) for each team
#     SELECT
#         home_id AS team_id,
#         game_id,
#         game_date
#     FROM
#         game_schedule
#     UNION ALL
#     SELECT
#         away_id AS team_id,
#         game_id,
#         game_date
#     FROM
#         game_schedule
# ),

# game_sequences AS (
#     -- Calculate 3-game sequences and the difference between the first and third game
#     SELECT
#         tg.team_id,
#         t.teamName,
#         tg.game_date AS game1_date,
#         LEAD(tg.game_date, 1) OVER (PARTITION BY tg.team_id ORDER BY tg.game_date) AS game2_date,
#         LEAD(tg.game_date, 2) OVER (PARTITION BY tg.team_id ORDER BY tg.game_date) AS game3_date,
#         julianday(LEAD(tg.game_date, 2) OVER (PARTITION BY tg.team_id ORDER BY tg.game_date)) -
#         julianday(tg.game_date) AS days_between_first_and_third
#     FROM
#         team_games tg
#     JOIN
#         team t ON tg.team_id = t.teamId
# ),

# three_in_four_games AS (
#     -- Identify 3-in-4 sequences (where the difference between the first and third game is <= 4 days)
#     SELECT
#         team_id,
#         teamName,
#         COUNT(*) AS three_in_four_count
#     FROM
#         game_sequences
#     WHERE
#         days_between_first_and_third <= 4 -- 3 games in 4 days
#         AND days_between_first_and_third IS NOT NULL
#     GROUP BY
#         team_id, teamName
# )

# -- Rank teams based on the number of 3-in-4s
# SELECT
#     teamName,
#     three_in_four_count,
#     RANK() OVER (ORDER BY three_in_four_count DESC) AS rank
# FROM
#     three_in_four_games
# ORDER BY
#     rank;
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