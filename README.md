# eCRF Data Validator
#### Description:

**Project Overview**
My final project for CS50P is called the "eCRF Data Validator". I work in the Clinical Data field, and I wanted to build something useful for my daily job. In clinical trials, hospitals collect patient data in forms called eCRFs, and we usually export this data as CSV files. The problem is that humans make typing mistakes. Sometimes they type negative ages, impossible heart rates, or wrong words.

My program reads a CSV file with patient data, checks if the medical numbers make sense, and prints a report on the screen showing exactly where the errors (called "Queries") are. This way, I don't have to check thousands of rows manually.

**Files in this Project**
To follow the CS50P rules, I kept my project organized in four specific files:

*   `project.py`: This is my main program. It contains the `main()` function that reads the file, and three other functions (`check_status`, `check_age`, and `check_heart_rate`) that do the mathematical and logical checks.
*   `test_project.py`: This is my testing file. I used `pytest` to test my three functions. I created tests for correct values, incorrect values, and edge cases to make sure my code is bulletproof.
*   `patients.csv`: This is a fake dataset I created. I put some intentional errors in it (like a patient with an age of -5, and a heart rate of 350) so I could test if my program really catches the mistakes.
*   `requirements.txt`: Because I only used standard Python libraries (`csv` and `sys`) for my main code, the only external library I needed to add here was `pytest` for the testing part.

**Design Choices and Challenges**
While writing this code, I had to make a few important design decisions based on what we learned in the course:

First, I decided to use `csv.DictReader` instead of the normal `csv.reader`. I did this because the regular reader uses index numbers (like `row[1]`). If the hospital changes the order of the columns in the CSV, my program would break. By using `DictReader`, I can call the data by its name, like `row["age"]`. This is much safer.

Second, I used `sys.argv` for the input. I wanted to force the user to type the name of the file in the terminal (like `python project.py patients.csv`). If they just type `python project.py`, my program catches the error using an `if` statement and uses `sys.exit()` to explain how to use the program correctly.

The biggest challenge was how to validate the numbers. When you read a CSV in Python, everything is a string. So, if a hospital types "NA" instead of a number for the age, the program will crash if I just try to use `int()`. To fix this, I put my validation rules inside three separate functions. Inside `check_age` and `check_heart_rate`, I used a `try` block to convert the string to an integer, and an `except ValueError` block. This way, if the data is letters instead of numbers, my function just returns `False` instead of crashing the whole program.

I kept these three functions completely separate from the `main()` loop. They only take one variable and return `True` or `False`. This was very important because it was the only way I could test them easily using `pytest` in my `test_project.py` file. I am very proud of how clean and testable the final code is.
