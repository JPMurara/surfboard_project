-- create tables in here
-- PGPASSWORD=Kl4A5PcUULa4dyy1FrnOBwygs1PFb8Xm psql -h dpg-cintu85gkuvudi85lii0-a.singapore-postgres.render.com -U surfboard_project_user surfboard_project < schema.sql

id	first_name	last_name	email	post_code	state	password		
INT PRIMARY KEY	TEXT NOT NULL	TEXT NOT NULL	TEXT NOT NULL	INT NOT NULL	TEXT NOT NULL	TEXT NOT NULL		
								
id	factory_id	factory_name	email	post_code	state	password		
INT PRIMARY KEY	INT	TEXT NOT NULL	TEXT NOT NULL	INT NOT NULL	TEXT NOT NULL	TEXT NOT NULL		
								
id	store_id	store_name	email	post_code	state	password		
INT PRIMARY KEY	INT	TEXT NOT NULL	TEXT NOT NULL	INT NOT NULL	TEXT NOT NULL	TEXT NOT NULL		
								
id	surfboard_id	shaper_id	model_name	wave_type	model_type	wave_size	break	skill_level
INT PRIMARY KEY	INT	INT	TEXT NOT NULL	TEXT NOT NULL	TEXT NOT NULL	INT NOT NULL	TEXT NOT NULL	TEXT NOT NULL
