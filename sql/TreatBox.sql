create database if not exists treatbox;
use treatbox;
drop table if exists userr;
drop table if exists game_user;
drop table if exists movie_user;
drop table if exists serie_user;
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
  FOREIGN KEY (id_user) REFERENCES userr(id_user)
);


#Relación N:M entre serie y user
create table serie_user (
  id_serie_user int auto_increment primary key,
  id_serie int not null,
  id_user int not null,
  serie_state varchar(30),
  notes decimal(3,1),
  times_view int,
  final_date datetime,
  comment varchar(2000),
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
  FOREIGN KEY (id_user) REFERENCES userr(id_user)
);