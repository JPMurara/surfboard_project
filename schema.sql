-- PGPASSWORD=Kl4A5PcUULa4dyy1FrnOBwygs1PFb8Xm psql -h dpg-cintu85gkuvudi85lii0-a.singapore-postgres.render.com -U surfboard_project_user surfboard_project < schema.sql

CREATE TABLE IF NOT EXISTS shapers (
    id serial PRIMARY KEY,
    shaper_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    url TEXT NOT NULL,
    is_admin BOOLEAN,
    password_hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS stores (
    id serial PRIMARY KEY,
    store_name TEXT NOT NULL UNIQUE,
    url TEXT NOT NULL,
    post_code INT NOT NULL
);			
		
-- CREATE TABLE IF NOT EXISTS shapers (
--     id serial PRIMARY KEY,
--     shaper_name TEXT NOT NULL UNIQUE,
--     url TEXT NOT NULL
-- );

CREATE TABLE IF NOT EXISTS surfboards (
    id serial PRIMARY KEY,
    shaper_id INT,
    model_name TEXT NOT NULL UNIQUE,
    model_type TEXT NOT NULL,
    min_wave_size INT NOT NULL,
    max_wave_size INT NOT NULL,
    wave_type TEXT NOT NULL,
    break_type TEXT NOT NULL,
    skill_level TEXT NOT NULL,
    img_single TEXT NOT NULL,
    img_detail TEXT NOT NULL,
    url TEXT NOT NULL,
    CONSTRAINT fk_shapers
        FOREIGN KEY (shaper_id)
        REFERENCES shapers(id)
);
