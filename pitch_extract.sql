-- CREATE TABLE selected_pitches (game_id VARCHAR(11),
--   home_team_id VARCHAR(11), bat_home_id INTEGER, park_name VARCHAR(256),
--   pit_id INTEGER, pitch_seq VARCHAR(256), x VARCHAR(11), y VARCHAR(11),
--   zone VARCHAR(11), pitch_res VARCHAR(11),Name VARCHAR(50),
--   Race VARCHAR(11), Hispanic INTEGER);
--
-- CREATE TABLE pitcher_info (Name VARCHAR(50), ID INTEGER,
--   Race VARCHAR(11), Hispanic INTEGER);
-- .mode csv
-- .import "PITCHf_x ID Name and Race.csv" pitcher_info

INSERT INTO selected_pitches (game_id, home_team_id, bat_home_id, park_name,
  pit_id, pitch_seq, x, y, zone, pitch_res, Name, Race, Hispanic)
SELECT game_id, home_team_id, bat_home_id, park_name, pit_id, pitch_seq, x, y, zone, pitch_res,
  Name, Race, Hispanic
FROM pitches
LEFT JOIN pitcher_info
  ON pit_id = ID
WHERE pit_id IN (477132, 592789, 605228, 453286, 456501, 519144, 434378,
  519242, 446372, 518516, 500779, 547888, 456034, 543294, 452657, 544931,
  592717, 453562, 592351, 573186, 593372, 533167, 628317, 594798, 543699,
  476451, 457918, 429722, 527054, 501381, 502042, 407793, 543521, 592662,
  462136, 592332, 519141, 605242, 605242, 425794, 112526, 595191, 461829,
  605200, 453214, 518633, 607074, 545333, 572971, 282332, 502188, 518452,
  502190, 471911, 445060, 547874, 501957, 519043, 467100, 425844, 543022,
  543606, 592767, 527048, 640455, 605151, 571666, 453178, 434622, 608665,
  468504, 489119, 450172, 570649, 434628, 448802, 573185, 450729, 502043,
  543408, 433587, 285079, 458708, 519076, 434671, 502624, 571578, 605538,
  434538, 605232, 502327, 466412, 606131, 450308, 448306)
  AND pitch_res IN ("C", "B");
