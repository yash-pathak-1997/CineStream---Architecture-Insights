-- Table: public.content

-- DROP TABLE IF EXISTS public.content;

CREATE TABLE IF NOT EXISTS public.content
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    title character varying(40) COLLATE pg_catalog."default",
    platform character varying(10) COLLATE pg_catalog."default",
    type character varying(10) COLLATE pg_catalog."default",
    image_url character varying(100) COLLATE pg_catalog."default",
    video_url character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT content_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.content
    OWNER to postgres;


-- Table: public.access_list

-- DROP TABLE IF EXISTS public.access_list;

CREATE TABLE IF NOT EXISTS public.access_list
(
    id integer NOT NULL,
    CONSTRAINT access_list_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.access_list
    OWNER to postgres;


INSERT INTO content(title, platform, type, image_url, video_url) VALUES
('RRR', 'netflix', 'movie', 'static/Netflix/RRR.jpg', 'static/Netflix/RRR.mp4'),
('Spider-Man Into The Spider Verse', 'netflix', 'movie', 'static/Netflix/Spider-Man Into The Spider-Verse.jpg', 'static/Netflix/SPIDER-MAN INTO THE SPIDER-VERSE.mp4'),
('Money Heist', 'netflix', 'series', 'static/Netflix/Money Heist.jpg', 'static/Netflix/Money Heist.mp4'),
('Peaky Blinders', 'netflix', 'series', 'static/Netflix/Peaky Blinders.jpg', 'static/Netflix/Peaky Blinders.mp4'),
('Farzi', 'prime', 'series', 'static/Amazon Prime/Farzi.jpg', 'static/Amazon Prime/FARZI.mp4'),
('Mirzapur', 'prime', 'series', 'static/Amazon Prime/Mirzapur.jpg', 'static/Amazon Prime/Mirzapur.mp4'),
('Pathaan', 'prime', 'movie', 'static/Amazon Prime/Pathaan.jpg', 'static/Amazon Prime/Pathaan.mp4'),
('The Batman', 'prime', 'movie', 'static/Amazon Prime/The Batman.jpg', 'static/Amazon Prime/THE BATMAN.mp4'),
('Avengers Endgame', 'hotstar', 'movie', 'static/Hotstar/Avengers Endgame.jpg', 'static/Hotstar/Avengers Endgame.mp4'),
('Chhichhore', 'hotstar', 'movie', 'static/Hotstar/Chhichhore.jpg', 'static/Hotstar/Chhichhore.mp4'),
('Daredevil', 'hotstar', 'series', 'static/Hotstar/Daredevil.jpg', 'static/Hotstar/Daredevil.mp4'),
('The Night Manager', 'hotstar', 'series', 'static/Hotstar/The Night Manager.jpg', 'static/Hotstar/The Night Manager.mp4');