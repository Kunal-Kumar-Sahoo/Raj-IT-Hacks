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



-- CREATE TABLE fundpool (
--     account_no INTEGER NOT NULL,
--     name VARCHAR(30) NOT NULL,
--     invested_amount INTEGER NOT NULL,
--     PRIMARY KEY (account_no, name),
--     FOREIGN KEY (account_no) REFERENCES people(account_no),
--     FOREIGN KEY (name) REFERENCES startup(name)
-- );
