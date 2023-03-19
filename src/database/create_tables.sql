drop database rajithacks;

CREATE DATABASE RAJITHACKS;

USE RAJITHACKS;
CREATE TABLE users (
    email_id varchar(30) PRIMARY KEY CHECK ( email_id LIKE '%@%.%' ),
    password TEXT NOT NULL,
    role CHAR NOT NULL
);

insert into users values('joseph@gmail.com','12345678','s');
insert into users values('robert@gmail.com','@3457@$#','p');
insert into users values('rose@gmail.com','**34!678','s');
insert into users values('lily_h@gmail.com','45678123','p');
insert into users values('tourist@gmail.com','1745238','s');

CREATE TABLE startup(
      name VARCHAR(30) PRIMARY KEY,
      place VARCHAR(30) NOT NULL,
      domain VARCHAR(30) NOT NULL,
      description TEXT NOT NULL,
      email_id varchar(30) NOT NULL CHECK ( email_id LIKE '%@%.%' ),
      funding INTEGER,
      valuation INTEGER,
      future_plans TEXT,
      risk CHAR NOT NULL,
      FOREIGN KEY (email_id) REFERENCES users(email_id)
);

insert into startup values('tourist','india','tech','software development company','tourist@gmail.com',200000, 55000,'more secured plattforms', 'l');
insert into startup values('rose','afghanistan','healthcare','providing high quality products in rural areas','rose@gmail.com',30000, 40000,'well coordinated, user centric and more effective', 'v');
insert into startup values('lily','england','fintech','targeting small scale buisness men and help them','lily_h@gmail.com',20500, 6500,'expanding to blockchain and more secured', 'h');
insert into startup values('robert','russia','agriculture','production of high quality agriculture products','robert@gmail.com',88000, 78000,'increasing crop yields to feed growing population', 'l');
insert into startup values('joseph','saudi arab','gold mines','pure and best quality gold','joseph@gmail.com',45000, 50000,'purest gold and reasonable price', 'h');

CREATE TABLE people(
    account_no VARCHAR(10) PRIMARY KEY,
    email_id varchar(30) NOT NULL CHECK ( email_id LIKE '%@%.%' ) ,
    name VARCHAR(30) NOT NULL,
    balance DOUBLE NOT NULL,
    FOREIGN KEY (email_id) REFERENCES users(email_id)
);

insert into people values('1234567890','lily_h@gmail.com','lily','20200');
insert into people values('6789012345','robert@gmail.com','robert','30000');
insert into people values('1290345678','tourist@gmail.com','tourist','90000');
insert into people values('5690123478','joseph@gmail.com','joseph','50000');
insert into people values('1289034567','rose@gmail.com','rose','25000');


CREATE TABLE fundpool (
    account_no VARCHAR(10) NOT NULL,
    name VARCHAR(30) NOT NULL,
    invested_amount INTEGER NOT NULL,
    PRIMARY KEY (account_no, name),
    FOREIGN KEY (account_no) REFERENCES people(account_no),
    FOREIGN KEY (name) REFERENCES startup(name)
);

insert into fundpool values('6789012345','robert',80000);
insert into fundpool values('1234567890','lily',7000);
insert into fundpool values('5690123478','joseph',12000);
insert into fundpool values('1290345678','tourist',8700);
insert into fundpool values('1289034567','rose',5600);


