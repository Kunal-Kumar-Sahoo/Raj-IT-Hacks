CREATE DATABASE RAJITHACKS;

USE RAJITHACKS;

CREATE TABLE startup(
      name VARCHAR(30) PRIMARY KEY,
      place VARCHAR(30) NOT NULL,
      domain VARCHAR(30) NOT NULL,
      description TEXT NOT NULL,
      funding INTEGER,
      valuation INTEGER,
      future_plans TEXT,
      risk CHAR NOT NULL
);

CREATE TABLE people(
    account_no VARCHAR(10) PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    balance DOUBLE NOT NULL
);

CREATE TABLE fundpool (
    account_no VARCHAR(10) NOT NULL,
    name VARCHAR(30) NOT NULL,
    invested_amount INTEGER NOT NULL,
    PRIMARY KEY (account_no, name),
    FOREIGN KEY (account_no) REFERENCES people(account_no),
    FOREIGN KEY (name) REFERENCES startup(name)
);