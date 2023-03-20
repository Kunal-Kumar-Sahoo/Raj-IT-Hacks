DROP DATABASE RAJITHACKS;

CREATE DATABASE RAJITHACKS;

USE RAJITHACKS;
CREATE TABLE users (
    email_id varchar(30) PRIMARY KEY CHECK ( email_id LIKE '%@%.%' ),
    password TEXT NOT NULL,
    role CHAR NOT NULL
);

CREATE TABLE startup(
      name VARCHAR(30) PRIMARY KEY,
      place VARCHAR(30) NOT NULL,
      domain VARCHAR(30) NOT NULL,
      description TEXT NOT NULL,
      email_id varchar(30) NOT NULL CHECK ( email_id LIKE '%@%.%' ),
      funding INTEGER,
      valuation INTEGER,
      revenue INTEGER DEFAULT 0,
      future_plans TEXT,
      risk CHAR NOT NULL,
      FOREIGN KEY (email_id) REFERENCES users(email_id)
);


CREATE TABLE people(
    account_no INTEGER AUTO_INCREMENT,
    email_id VARCHAR(100) NOT NULL CHECK ( email_id LIKE '%@%.%' ),
    name VARCHAR(30) NOT NULL,
    balance DOUBLE NOT NULL,
    pool_investment INTEGER DEFAULT 0,
    PRIMARY KEY(account_no),
    FOREIGN KEY (email_id) REFERENCES users(email_id)
);

CREATE TABLE investors(
    name VARCHAR(30) PRIMARY KEY,
    successful_startups TEXT NOT NULL,
    investment INTEGER DEFAULT 0
);