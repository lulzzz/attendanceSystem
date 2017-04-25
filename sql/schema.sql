#define users
drop table if exists users;
create table users (  name varchar(255) not null, card_id int not null, branch varchar(50) not null );
#define istream
drop table if exists istream;
create table istream ( card_id int not null, time varchar(14) not null );
drop table if exists time_per_week 
create table { card_id int not null, time_in_seconds int not null };
