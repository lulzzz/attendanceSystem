#define users
drop table if exists users;
create table users (  name varchar(255) not null, card_id int not null, branch varchar(50) not null );
#define istream
drop table if exists istream;
create table istream ( card_id int not null, time varchar(14) not null );
