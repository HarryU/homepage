drop table if exists users;
create table users (
	id integer primary key autoincrement,
	username text not null,
	passwd_hash text not null
);

drop table if exists blogposts;
create table blogposts (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);
