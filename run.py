import sys
import os
from src.main import print_payment_for_employees

conf_path = os.getcwd()
sys.path.append(conf_path)


print_payment_for_employees()
