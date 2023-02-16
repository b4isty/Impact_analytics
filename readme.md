# Graduation Ceremony Attendance Probability Calculator
This program calculates the probability of a student missing their graduation ceremony based on their attendance record.

### Problem Statement
A student must attend classes in order to be eligible to attend their graduation ceremony. The student cannot miss classes for four or more consecutive days. The graduation ceremony takes place on the last day of the academic year, which is the Nth day.

The program needs to solve the following problems:

1. Determine the number of ways to attend classes over N days.
2. Calculate the probability that the student will miss their graduation ceremony.
The solution is represented in the string format as "Answer of (2) / Answer of (1)", without actually dividing or reducing the fraction to a decimal.

### Program Solution
The program uses a dynamic programming approach to solve the problem. It creates a 2D list to store intermediate results and fills in the base cases of the table. Then, it computes the dynamic programming table using a bottom-up approach.

The final result is extracted from the table to determine the total ways to attend and the total ways to miss the last day of the academic year. The program returns the result in the required string format.

### Usage
1. Clone the repository or download the code files.
2. Run the program in any Python environment.
3. Input the number of academic days when prompted.
4. The program will output the probability that the student will miss their graduation ceremony and the number of ways to attend classes over number of academic days entered.

To run the test.py file execute below command

```shell
python test.py
```

To run the program execute below command

```shell
python main.py
```

Program Output
```
Enter number of academic days: 5
Number of academic days is 5
Probability of missing the graduation ceremony: 14/29
```

```
Enter number of academic days: 10
Number of academic days is 10
Probability of missing the graduation ceremony: 372/773
```