from flask_restful import reqparse

from enumerations import *

# Set up request parsers for household and individual get/ post/ put/ patch/ delete requests

household_get_args = reqparse.RequestParser() # household_delete_args # help
household_get_args.add_argument('id', type=int, case_sensitive=False, trim=True)
household_get_args.add_argument('nric', type=str, case_sensitive=False, trim=True)
household_get_args.add_argument('housingtype', type=str, case_sensitive=False, trim=True, choices=housing_type_choices)
household_get_args.add_argument('agebelow', type=int)
household_get_args.add_argument('ageabove', type=int)
household_get_args.add_argument('spouses', type=bool)
household_get_args.add_argument('householdincomebelow', type=int)
household_get_args.add_argument('householdincomeabove', type=int)
household_get_args.add_argument('grant', type=str, case_sensitive=False, trim=True, choices=grant_choices)

household_post_args = reqparse.RequestParser() # household_put_args
household_post_args.add_argument('id', type=int, required=True)
household_post_args.add_argument('individuals', type=list, case_sensitive=False, trim=True)
household_post_args.add_argument('housingtype', type=str, case_sensitive=False, trim=True, choices=housing_type_choices, required=True)

household_patch_args = reqparse.RequestParser()
household_patch_args.add_argument('id', type=int, required=True)
household_patch_args.add_argument('individuals', type=list, case_sensitive=False, trim=True)
household_patch_args.add_argument('housingtype', type=str, case_sensitive=False, trim=True, choices=housing_type_choices)

individual_get_args = reqparse.RequestParser() # individual_delete_args # help
individual_get_args.add_argument('nric', type=str, case_sensitive=False, trim=True)
individual_get_args.add_argument('name', type=str, case_sensitive=False, trim=True)
individual_get_args.add_argument('gender', type=str, case_sensitive=False, trim=True, choices=gender_choices)
individual_get_args.add_argument('maritalstatus', type=str, case_sensitive=False, trim=True, choices=marital_status_choices)
individual_get_args.add_argument('spouse', type=str, case_sensitive=False, trim=True)
individual_get_args.add_argument('occupationtype', type=str, case_sensitive=False, trim=True, choices=occupation_type_choices)
individual_get_args.add_argument('annualincomebelow', type=int)
individual_get_args.add_argument('annualincomeabove', type=int)
individual_get_args.add_argument('dateofbirthbefore', type=str, case_sensitive=False, trim=True)
individual_get_args.add_argument('dateofbirthafter', type=str, case_sensitive=False, trim=True)

individual_post_args = reqparse.RequestParser() # individual_put_args
individual_post_args.add_argument('nric', type=str, case_sensitive=False, trim=True, required=True)
individual_post_args.add_argument('name', type=str, case_sensitive=False, trim=True, required=True)
individual_post_args.add_argument('gender', type=str, case_sensitive=False, trim=True, choices=gender_choices, required=True)
individual_post_args.add_argument('maritalstatus', type=str, case_sensitive=False, trim=True, choices=marital_status_choices, required=True)
individual_post_args.add_argument('spouse', type=str, case_sensitive=False, trim=True)
individual_post_args.add_argument('occupationtype', type=str, case_sensitive=False, trim=True, choices=occupation_type_choices, required=True)
individual_post_args.add_argument('annualincome', type=int, required=True)
individual_post_args.add_argument('dateofbirth', type=str, case_sensitive=False, trim=True, required=True)

individual_patch_args = reqparse.RequestParser()
individual_patch_args.add_argument('nric', type=str, case_sensitive=False, trim=True, required=True)
individual_patch_args.add_argument('name', type=str, case_sensitive=False, trim=True)
individual_patch_args.add_argument('gender', type=str, case_sensitive=False, trim=True, choices=gender_choices)
individual_patch_args.add_argument('maritalstatus', type=str, case_sensitive=False, trim=True, choices=marital_status_choices)
individual_patch_args.add_argument('spouse', type=str, case_sensitive=False, trim=True)
individual_patch_args.add_argument('occupationtype', type=str, case_sensitive=False, trim=True, choices=occupation_type_choices)
individual_patch_args.add_argument('annualincome', type=int)
individual_patch_args.add_argument('dateofbirth', type=str, case_sensitive=False, trim=True)