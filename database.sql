CREATE DATABASE cq_db;
CREATE TABLE category (
	cat_id BIGSERIAL NOT NULL PRIMARY KEY,
	cat_name VARCHAR(15) NOT NULL
);
CREATE TABLE usr (
	usr_id BIGSERIAL NOT NULL PRIMARY KEY,
	usr_name VARCHAR(18) NOT NULL,
	usr_registrationDate DATE NOT NULL,
	usr_totalUpvotes INT,
	usr_totalDownvotes INT
);
CREATE TABLE thread (
	thr_id BIGSERIAL NOT NULL PRIMARY KEY,
	thr_title VARCHAR(100) NOT NULL,
	thr_content TEXT NOT NULL,
	thr_keywords JSON,
	thr_postDate DATE NOT NULL,
	thr_upvotes INT,
	thr_downvotes INT,
	thr_category BIGINT NOT NULL REFERENCES category (cat_id),
	thr_author BIGINT NOT NULL REFERENCES usr (usr_id)
);
CREATE TABLE comment (
	com_id BIGSERIAL NOT NULL PRIMARY KEY,
	com_text VARCHAR(1000) NOT NULL,
	com_postDate DATE NOT NULL,
	com_upvotes INT,
	com_downvotes INT,
	com_author BIGINT NOT NULL REFERENCES usr (usr_id),
	com_thrlocation BIGINT NOT NULL REFERENCES thread (thr_id)
);

INSERT INTO category VALUES (1, 'Animals');
INSERT INTO category VALUES (2, 'Education');
INSERT INTO category VALUES (3, 'Fashion');
INSERT INTO category VALUES (4, 'Foods, drinks');
INSERT INTO category VALUES (5, 'Health');
INSERT INTO category VALUES (6, 'Holidays');
INSERT INTO category VALUES (7, 'IT');
INSERT INTO category VALUES (8, 'Politics');
INSERT INTO category VALUES (9, 'Religion');
INSERT INTO category VALUES (10, 'Sport');
INSERT INTO category VALUES (11, 'Science');
INSERT INTO category VALUES (12, 'Travel');
INSERT INTO usr VALUES (1, 'john', now(), 8, 4);
INSERT INTO usr VALUES (2, 'jack', now(), 6, 4);
INSERT INTO usr VALUES (3, 'jill', now(), 5, 2);
INSERT INTO thread VALUES (1, 'Cats', 'Cats are cute!', '{ "keywords": ["cat", "cute"] }', now(), 3, 0, 1, 2);
INSERT INTO thread VALUES (2, 'What is your favourite dog breed?', 'My is Labrador', '{ "keywords": ["dogs"] }', now(), 2, 1, 1, 1);
INSERT INTO thread VALUES (3, 'Election', 'Who do you vote for?', '{ "keywords": ["election", "vote"] }', now(), 1, 2, 8, 1);
INSERT INTO thread VALUES (4, 'Africa travel', 'Any suggestions?', '{ "keywords": ["africa"] }', now(), 2, 1, 12, 2);
INSERT INTO thread VALUES (5, 'Holidays in this year?', 'Anyone got the list?', '{ "keywords": [""] }', now(), 1, 2, 6, 3);
INSERT INTO comment VALUES (1, 'Yes they are!', now(), 3, 0, 1, 1);
INSERT INTO comment VALUES (2, 'True.', now(), 2, 0, 3, 1);
INSERT INTO comment VALUES (3, 'Golden retriever is the best.', now(), 1, 0, 3, 2);
INSERT INTO comment VALUES (4, 'Top secret', now(), 1, 1, 2, 3);
INSERT INTO comment VALUES (5, 'Egypt is a nice place. I would recommend it!', now(), 1, 0, 3, 4);
INSERT INTO comment VALUES (6, 'Google it', now(), 2, 1, 1, 5);
INSERT INTO comment VALUES (7, 'Why do you want holidays?', now(), 0, 2, 2, 5);