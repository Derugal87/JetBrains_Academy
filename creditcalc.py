import argparse
import sys
from math import ceil, log

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, help="Can be either 'annuity' or 'diff'")
parser.add_argument("--periods", type=int, help="Denotes the number of months and/or years  needed to repay the credit")
parser.add_argument("--principal", type=float, help="Valid with every combination")
parser.add_argument("--payment", type=float, help="If --type=diff, their combination is invalid")
parser.add_argument("--interest", type=float, help="Must always be specified.")

args = parser.parse_args()

if len(sys.argv) == 5:
    interest = args.interest
    type = args.type
    principal = args.principal
    periods = args.periods
    if interest is not None:
        if interest >= 0:
            if type == 'annuity':
                payment = args.payment
                if principal is not None and payment is not None:
                    if principal >= 0:
                        if payment >= 0:
                            i = interest / (12 * 100)  # where i - nominal_interest_rate
                            month_number = ceil(log(payment / (payment - i * principal), (1 + i)))
                            year = month_number // 12
                            month = month_number % 12
                            if year == 1:
                                if month == 1:
                                    print(f'It will take {year} year and {month} month to repay this loan!')
                                    print(f'Overpayment = {(int(payment * (year * 12 + month) - principal))}')
                                elif month == 0:
                                    print(f'It will take {year} year to repay this loan!')
                                    print(f'Overpayment = {(int(payment * (year * 12) - principal))}')
                                else:
                                    print(f'It will take {year} year and {month} months to repay this loan!')
                                    print(f'Overpayment = {(int(payment * (year * 12 + month) - principal))}')
                            elif year == 0:
                                if month == 1:
                                    print(f'It will take {month} month to repay this loan!')
                                    print(f'Overpayment = {(int(payment * month - principal))}')
                                elif month == 0:
                                    print(f'You"re repaid this loan!')
                                else:
                                    print(f'It will take {month} months to repay this loan!')
                                    print(f'Overpayment = {(int(payment * month - principal))}')
                            else:
                                if month == 1:
                                    print(f'It will take {year} years and {month} month to repay this loan!')
                                    print(f'Overpayment = {(int(payment * (year * 12 + month) - principal))}')
                                elif month == 0:
                                    print(f'It will take {year} years to repay this loan!')
                                    print(f'Overpayment = {(int(payment * (year * 12) - principal))}')
                                else:
                                    print(f'It will take {year} years and {month} months to repay this loan!')
                                    print(f'Overpayment = {(int(payment * (year * 12 + month) - principal))}')
                        else:
                            print('Incorrect parameters')
                    else:
                        print('Incorrect parameters')
                elif principal is not None and periods is not None:
                    if principal >= 0:
                        if periods > 0:
                            i = interest / (12 * 100)  # where i - nominal_interest_rate
                            payment = ceil(principal * (i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1))
                            print(f'Your annuity payment = {payment}!')
                            print(f'Overpayment = {int(payment * periods - principal)}')
                        else:
                            print('Incorrect parameters')
                    else:
                        print('Incorrect parameters')
                elif payment is not None and periods is not None:
                    if payment >= 0:
                        if periods > 0:
                            i = interest / (12 * 100)  # where i - nominal_interest_rate
                            principal = int(payment / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)))
                            print(f'Your loan principal = {principal}!')
                            print(f'Overpayment = {int(payment * periods - principal)}')
                        else:
                            print('Incorrect parameters')
                    else:
                        print('Incorrect parameters')
                else:
                    print('Incorrect parameters')
            elif type == 'diff':
                if principal is not None and periods is not None:
                    if principal >= 0:
                        if periods > 0:
                            i = interest / (12 * 100)  # nominal_interest_rate
                            result = 0  # all the payments
                            m = 1  # first_month
                            while m <= periods:
                                diff_payment = principal / periods + i * (principal - ((principal * (m - 1)) / periods))
                                print(f'Month {m}: payment is {ceil(diff_payment)}')
                                result += ceil(diff_payment)
                                m += 1
                            print()
                            print(f'Overpayment = {int(result - principal)}')
                        else:
                            print('Incorrect parameters')
                    else:
                        print('Incorrect parameters')
                else:
                    print('Incorrect parameters')
            else:
                print('Incorrect parameters')
        else:
            print('Incorrect parameters')
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
