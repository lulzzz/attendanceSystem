drop table users if exists;
create table users ( id int not null auto_increment, primary key(id) , name varchar(255) not null, card_id int not null );
#put there definition for istream
