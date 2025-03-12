USE college;

CREATE TABLE student(
rollno INT PRIMARY KEY,
name VARCHAR(50)
);
SELECT * FROM student;

INSERT INTO student
(rollno, name)
VALUES
(01, "Salik"),
(02, "Atif"),
(03, "Faika");

INSERT INTO student
(rollno, name)
VALUES
(04, "Irtaqa");
INSERT INTO student VALUES (05, "Anees");