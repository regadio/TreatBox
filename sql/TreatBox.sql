create database if not exists treatbox;
use treatbox;
drop table if exists userr;
drop table if exists game_user;
drop table if exists movie_user;
drop table if exists serie_user;
drop table if exists gender;
drop table if exists game;
drop table if exists film;
drop table if exists movie;
create table userr(
id_user int auto_increment primary key,
nickname varchar(100),
email varchar(100),
pass varchar(20),
session_token varchar(1000),
descriptionn varchar(1000),
imagen longblob,
banner longblob
);
create table gender(
id_gender int auto_increment primary key,
namee varchar(80),
tittle varchar(80)
);
create table game(
id_game int auto_increment primary key,
developer varchar(40),
year_release date,
tittle varchar(50),
imagen longblob,
punctuation decimal(3,1),
descriptionn varchar(2000)
);
create table serie(
id_serie int auto_increment primary key,
director varchar(40),
year_release date,
duration varchar(100),
season varchar(50),
tittle varchar(50),
imagen longblob,
punctuation decimal(3,1),
descriptionn varchar(2000)
);
create table movie(
id_movie int auto_increment primary key,
director varchar(40),
year_release date,
duration varchar(100),
guion varchar(50),
tittle varchar(50),
cast varchar(500),
imagen longblob,
punctuation decimal(3,1),
descriptionn varchar(2000)
);
#Relación N:M entre gender y serie
create table serie_gender (
  id_serie_gender int auto_increment primary key,
  id_serie int not null,
  id_gender int not null,
  FOREIGN KEY (id_serie) REFERENCES serie(id_serie),
  FOREIGN KEY (id_gender) REFERENCES gender(id_gender)
);
#Relación N:M entre gender y movie
create table movie_gender (
  id_movie_gender int auto_increment primary key,
  id_movie int not null,
  id_gender int not null,
  FOREIGN KEY (id_movie) REFERENCES movie(id_movie),
  FOREIGN KEY (id_gender) REFERENCES gender(id_gender)
);
#Relación N:M entre gender y game
create table game_gender (
  id_game_gender int auto_increment primary key,
  id_game int not null,
  id_gender int not null,
  FOREIGN KEY (id_game) REFERENCES game(id_game),
  FOREIGN KEY (id_gender) REFERENCES gender(id_gender)
);
#Relación N:M entre game y user
create table game_user (
  id_game_user int auto_increment primary key,
  id_game int not null,
  id_user int not null,
  game_state varchar(30),
  notes decimal(3,1),
  times_pass int,
  final_date datetime,
  comment varchar(2000),
  FOREIGN KEY (id_game) REFERENCES game(id_game),
  FOREIGN KEY (id_user) REFERENCES userr(id_user)
);
#Relación N:M entre serie y user
create table serie_user (
  id_serie_user int auto_increment primary key,
  id_serie int not null,
  id_user int not null,
  serie_state varchar(30),
  director varchar(40),
  year_release date,
  duration varchar(100),
  season varchar(50),
  notes decimal(3,1),
  tittle varchar(50),
  image longblob,
  comment varchar(2000),
  FOREIGN KEY (id_serie) REFERENCES serie(id_serie),
  FOREIGN KEY (id_user) REFERENCES userr(id_user)
);
#Relación N:M entre movie y user
create table movie_user (
  id_movie_user int auto_increment primary key,
  id_movie int not null,
  id_user int not null,
  movie_state varchar(30),
  notes decimal(3,1),
  times_view int,
  final_date datetime,
  comment varchar(2000),
  FOREIGN KEY (id_movie) REFERENCES movie(id_movie),
  FOREIGN KEY (id_user) REFERENCES userr(id_user)
);