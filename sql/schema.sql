#define users
drop table if exists users;
create table users ( id int not null auto_increment, primary key(id) , name varchar(255) not null, card_id int not null );
#define istream
drop table if exists istream;
create table istream ( id int not null auto_increment, primary key(id), card_id int not null, time time not null );
