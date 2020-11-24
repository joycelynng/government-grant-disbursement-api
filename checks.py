import datetime
import re

def valid_individual_args(method, args):
    if args['nric'] is not None and not valid_nric(args['nric']):
        return False

    if args['spouse'] is not None and not valid_nric(args['spouse']):
        return False

    if method == 'post':
        if args['annualincome'] is not None and not valid_annual_income(args['annualincome']):
            return False

        if args['dateofbirth'] is not None and not valid_date(args['dateofbirth']):
            return False

    if method == 'get':
        if args['annualincomebelow'] is not None and not valid_annual_income(args['annualincomebelow']):
            return False

        if args['annualincomeabove'] is not None and not valid_annual_income(args['annualincomeabove']):
            return False

        if args['dateofbirthbefore'] is not None and not valid_date(args['dateofbirthbefore']):
            return False

        if args['dateofbirthafter'] is not None and not valid_date(args['dateofbirthafter']):
            return False

    return True

def valid_household_args(method, args):
    if method == 'post':
        if args['individuals'] is not None:
            for nric in args['individuals']:
                if not valid_nric(nric):
                    return False
    
    if method == 'get':
        if args['nric'] is not None and not valid_nric(args['nric']):
            return False
        
        if args['agebelow'] is not None and not valid_age(args['agebelow']):
            return False

        if args['ageabove'] is not None and not valid_age(args['ageabove']):
            return False

        if args['householdincomebelow'] is not None and not valid_annual_income(args['householdincomebelow']):
            return False

        if args['householdincomeabove'] is not None and not valid_annual_income(args['householdincomeabove']):
            return False
    
    return True

def valid_nric(nric):
    match = re.match(r'^[stfg]\d{7}[abcdefghijklmnpqrtuwxz]$', nric)

    if not match:
        return False

    char = list(nric)

    sum = \
    int(char[1]) * 2 + \
    int(char[2]) * 7 + \
    int(char[3]) * 6 + \
    int(char[4]) * 5 + \
    int(char[5]) * 4 + \
    int(char[6]) * 3 + \
    int(char[7]) * 2

    if char[0] == 't' or char[0] == 'g':
        sum += 4

    remainder = sum % 11

    if char[0] == 'f' or char[0] == 'g':
        if remainder == 0 and char[8] != 'x':
            return False
        if remainder == 1 and char[8] != 'w':
            return False
        if remainder == 2 and char[8] != 'u':
            return False
        if remainder == 3 and char[8] != 't':
            return False
        if remainder == 4 and char[8] != 'r':
            return False
        if remainder == 5 and char[8] != 'q':
            return False
        if remainder == 6 and char[8] != 'p':
            return False
        if remainder == 7 and char[8] != 'n':
            return False
        if remainder == 8 and char[8] != 'm':
            return False   
        if remainder == 9 and char[8] != 'l':
            return False
        if remainder == 10 and char[8] != 'k':
            return False

    if char[0] == 's' or char[0] == 't':
        if remainder == 0 and char[8] != 'j':
            return False
        if remainder == 1 and char[8] != 'z':
            return False
        if remainder == 2 and char[8] != 'i':
            return False
        if remainder == 3 and char[8] != 'h':
            return False
        if remainder == 4 and char[8] != 'g':
            return False
        if remainder == 5 and char[8] != 'f':
            return False
        if remainder == 6 and char[8] != 'e':
            return False
        if remainder == 7 and char[8] != 'd':
            return False
        if remainder == 8 and char[8] != 'c':
            return False   
        if remainder == 9 and char[8] != 'b':
            return False
        if remainder == 10 and char[8] != 'a':
            return False

    return True

def valid_annual_income(annual_income):
    if annual_income < 0:
        return False
    return True

def valid_date(date):
    try:
        parsed_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False

    if parsed_date > datetime.datetime.today():
        return False
    
    return True

def valid_age(age):
    if age < 0 or age > 150:
        return False
    return True