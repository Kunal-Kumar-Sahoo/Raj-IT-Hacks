USE RAJITHACKS;

CREATE TABLE problems(
    problem_id INTEGER AUTO_INCREMENT,
    problem_description TEXT NOT NULL,
    problem_location VARCHAR(30) NOT NULL,
    PRIMARY KEY(problem_id)
);