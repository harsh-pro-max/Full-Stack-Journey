-- SQL Assignments: Database Management

-- 1. Create a table (student) with 3 columns (rollno, name, course).
CREATE TABLE student (
    rollno INT PRIMARY KEY,
    name VARCHAR(255),
    course VARCHAR(255)
);

-- 2. Insert records for 4 students.
INSERT INTO student (rollno, name, course)
VALUES
    (1, 'John', 'Math'),
    (2, 'Alice', 'History'),
    (3, 'Bob', 'Science'),
    (4, 'Eve', 'English');

-- 3. Write a SELECT query to fetch all the students.
SELECT * FROM student;

-- 4. Update the student name of rollno 3 with 'Mohan'.
UPDATE student
SET name = 'Mohan'
WHERE rollno = 3;

-- 5. Delete any student from the table using their rollno.
DELETE FROM student
WHERE rollno = 4;

-- 6. Delete all the data from the student table.
DELETE FROM student;

-- 7. Drop the student table.
DROP TABLE student;

-- 8. Create a Courses table (cid, cname) where cid is a primary key
--    and a Student table (rollno, name, cid) where rollno is a primary key 
--    and cid is a foreign key.
CREATE TABLE Courses (
    cid INT PRIMARY KEY,
    cname VARCHAR(255)
);

CREATE TABLE Student (
    rollno INT PRIMARY KEY,
    name VARCHAR(255),
    cid INT,
    FOREIGN KEY (cid) REFERENCES Courses(cid)
);

-- 9. Insert data into both tables.
INSERT INTO Courses (cid, cname)
VALUES
    (1, 'Python'),
    (2, 'Java'),
    (3, 'C++');

INSERT INTO Student (rollno, name, cid)
VALUES
    (101, 'Alice', 1),
    (102, 'Bob', 2),
    (103, 'Charlie', 1),
    (104, 'David', 3);

-- 10. Select all students who are doing a specific course, e.g., Python.
SELECT s.name
FROM Student s
JOIN Courses c ON s.cid = c.cid
WHERE c.cname = 'Python';