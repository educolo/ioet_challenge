# Exercise challenge for IOET
## Run the script
The script use only python 3.8 standard libraries.
To run de script write in your cmd:
```
python run.py
```

The input.txt file it's located on the 'src' folder.

## Project Structure
```
ioet_challenge/
├── README.md
├── run.py
├── src/
    ├── __init__.py
    ├── employee.py
    ├── exceptions.py
    ├── input.txt
    ├── main.py
    ├── payment.py
    └── tests/
        ├── __init__.py
        ├── test_employee.py
        └── test_payment.py
```
- `README.md`: A brief description of the project and how to use it.
- `run.py`: A file used to run the exersice script.
- `src/`: The main folder containing the project code.
  - `__init__.py`: An empty file indicating that this folder should be treated as a Python package.
  - `employee.py`: Classes for employee (Employee and DayWorkedTime)
  - `exceptions.py`: Custom exceptions file.
  - `input.txt`: Input file for the exercise with employees data and worked times
  - `main.py`: Main file to run the exercise with rule creation and input.txt read functionality.
  - `payment.py`: Classes for payment (Payment and Rule)
  - `tests/`: The tests folder containing the project automatic tests.
    - `__init__.py`: An empty file indicating that this folder should be treated as a Python package.
    - `test_employee.py`: Test specific employee functionalities.
    - `test_payment.py`: Test specific payment functionalities.

## Solution overview

## Exercise

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

Monday - Friday

00:01 - 09:00 25 USD

09:01 - 18:00 15 USD

18:01 - 00:00 20 USD

Saturday and Sunday

00:01 - 09:00 30 USD

09:01 - 18:00 20 USD

18:01 - 00:00 25 USD

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

MO: Monday

TU: Tuesday

WE: Wednesday

TH: Thursday

FR: Friday

SA: Saturday

SU: Sunday

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

Case 1:

INPUT

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:

The amount to pay RENE is: 215 USD

Case 2:

INPUT

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:

The amount to pay ASTRID is: 85 USD