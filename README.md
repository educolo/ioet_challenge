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
We have 4 classes: `Employee`, `DayWorkedTime`, `Rule`, and `Payment`.
- `Employee`: Has the employee name and the worked days as a list of DayWorkedTime
- `DayWorkedTime`: Manage the weekday, start and end times.
- `Rule`: Has the weekday, price, start time, and end time. The worked time inside this rule will be paid at the rule price.
- `Payment`: Process the payment for an Employee with the set of rules given.

`Employee` and `DayWorkedTime` have a factory method inside the class to construct an instance from a string. That can be moved to a factory class, but this solution looks like an over-engineering.
The factory method it's to have an easy way to import the data from the input.txt.

`DayWorkedTime` convert hour with minutes to a float hour representation to manage hourly payments. For example 1 hour and 30 minutes it's the same that 1.5 hours.

`Payment` iterate the list of `Rule` for each worked day to find which Rule applies.
The first 'easy' approach was to iterate hours on the day worked to accumulate on the payment depending on the rule applied, but this could bring performance issues because a day could have 24 hours worked, and an employee could have a lot of worked days. We don't need to iterate hours and add, only multiply hours by hour payment.

`Rule` is quite simple because in the exercise was like a constant, and the variables came from another aspect (worked hours), so I minimized complexity here to have a fast working solution. It could have the possibility to use a method to import from a string, and also to import rules from a txt file, but none of that was a requirement. If we need here better time management to add minutes, could be a good idea to use the same `DayWorkedTime`, this way we reduce repeating code and we assure that `Rule` and `Employee` manage time the same way. Also gives us a pre-built constructor from a string and weekday management. This will need a refactor on the class (at least on the name) to be more clear on what's the usability. Also to change how manage weekdays (using int could be more performant), we have this logic in one place.

The `main.py` file has two functions, one to create the exercise payment rules and another to import the data from the `input.txt` file and print each employee payment on the screen.

Finally, the `run.py` run the functions inside `main.py` after adding the conf_path to avoid import issues.

## Possible improvements
 - Replace weekdays for integers, to avoid using condition 'in' and use more performant comparisons.
 - Import payment rules from txt file
 - Add validations for weekdays to avoid bad input data.
 - Allow minutes in rules (I avoided this on purpose, but I'm not sure about the business needs)
   - To do this, we should use `DayWorkedTime` to have the same "time manager". It will need a refactor on employee.

## Exercise

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

**Monday - Friday**

00:01 - 09:00 25 USD

09:01 - 18:00 15 USD

18:01 - 00:00 20 USD

**Saturday and Sunday**

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