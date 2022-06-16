--
-- File generated with SQLiteStudio v3.3.3 on Πεμ Ιουν 16 15:14:19 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Course
DROP TABLE IF EXISTS Course;

CREATE TABLE Course (
    Id           INTEGER     PRIMARY KEY AUTOINCREMENT,
    Title        STRING (25) NOT NULL,
    DepartmentId INTEGER     REFERENCES Department (Id)
                             NOT NULL
);

INSERT INTO Course (Id, Title, DepartmentId) VALUES (1, 'Flask', 2);
INSERT INTO Course (Id, Title, DepartmentId) VALUES (2, 'Node', 2);

-- Table: CourseStudents
DROP TABLE IF EXISTS CourseStudents;

CREATE TABLE CourseStudents (
    CourseId  INTEGER NOT NULL
                      REFERENCES Course (Id),
    StudentId INTEGER REFERENCES Student (Id)
                      NOT NULL,
    PRIMARY KEY (
        CourseId,
        StudentId
    )
);

INSERT INTO CourseStudents (CourseId, StudentId) VALUES (1, 1);
INSERT INTO CourseStudents (CourseId, StudentId) VALUES (1, 2);
INSERT INTO CourseStudents (CourseId, StudentId) VALUES (2, 2);

-- Table: Department
DROP TABLE IF EXISTS Department;

CREATE TABLE Department (
    Id    INTEGER     PRIMARY KEY AUTOINCREMENT,
    Title STRING (25) NOT NULL
);

INSERT INTO Department (Id, Title) VALUES (1, 'Design');
INSERT INTO Department (Id, Title) VALUES (2, 'Web');

-- Table: Lectiurer
DROP TABLE IF EXISTS Lectiurer;

CREATE TABLE Lectiurer (
    Id        INTEGER      PRIMARY KEY AUTOINCREMENT,
    Firstname STRING (50)  NOT NULL,
    Lastname  STRING (100) NOT NULL,
    AFM       CHAR (9)     NOT NULL
                           UNIQUE
);

INSERT INTO Lectiurer (Id, Firstname, Lastname, AFM) VALUES (1, 'Lecturer', 1, '111111111');
INSERT INTO Lectiurer (Id, Firstname, Lastname, AFM) VALUES (2, 'Leturer', 2, '222222222');

-- Table: Student
DROP TABLE IF EXISTS Student;

CREATE TABLE Student (
    Id        INTEGER      PRIMARY KEY AUTOINCREMENT
                           NOT NULL,
    AM        STRING (5)   NOT NULL
                           UNIQUE,
    Firstname STRING (50)  NOT NULL,
    Lastname  STRING (100) NOT NULL,
    Graduated BOOLEAN      NOT NULL
                           DEFAULT (0),
    BirthDate DATE,
    MentorId  INTEGER      REFERENCES Lectiurer (Id)
);

INSERT INTO Student (Id, AM, Firstname, Lastname, Graduated, BirthDate, MentorId) VALUES (1, 'S0001', 'John', 'Doe', 0, '1990-01-01', NULL);
INSERT INTO Student (Id, AM, Firstname, Lastname, Graduated, BirthDate, MentorId) VALUES (2, 'S0002', 'Joan', 'Doe', 1, NULL, 2);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
