from flask import Flask
from flask_restful import Api, Resource, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

import os.path
import datetime

from enumerations import *
from requestparsers import *
from checks import *

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Define household and individual database tables/ schema

# class Household(db.Model):
# 	__tablename__ = 'household'
# 	id = db.Column(db.Integer, primary_key=True)
# 	individuals = db.relationship('Individual', backref='household')
# 	housing_type = db.Column(db.Enum(HousingType), nullable=False)

# 	def __repr__(self):
# 		return

class Individual(db.Model):
	__tablename__ = 'individual'
	nric = db.Column(db.String(9), primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	gender = db.Column(db.Enum(Gender), nullable=False)
	marital_status = db.Column(db.Enum(MaritalStatus), nullable=False)
	spouse = db.relationship('Individual', uselist=False, remote_side=[nric])
	occupation_type = db.Column(db.Enum(OccupationType), nullable=False)
	annual_income = db.Column(db.Integer, nullable=False)
	date_of_birth = db.Column(db.Date, nullable=False)

	spouse_nric = db.Column(db.String, db.ForeignKey('individual.nric'))
	# household_id = db.Column(db.Integer, db.ForeignKey('household.id'))

	def __repr__(self):
		return

# Create database

if os.path.exists('database.db'):
	os.remove('database.db')

db.create_all()

# Set up household and individual resource fields, to format household/ individual resource data in response

spouse_resource_fields = {
	'nric': fields.String,
	'name': fields.String,
	'gender': fields.String,
	'marital_status': fields.String,
	'occupation_type': fields.String,
	'annual_income': fields.Integer,
	'date_of_birth': fields.DateTime(dt_format='iso8601')
}

individual_resource_fields = {
	'nric': fields.String,
	'name': fields.String,
	'gender': fields.String,
	'marital_status': fields.String,
	'spouse': fields.Nested(spouse_resource_fields, allow_null=True),
	'occupation_type': fields.String,
	'annual_income': fields.Integer,
	'date_of_birth': fields.DateTime(dt_format='iso8601')
}

# household_resource_fields = {
# 	'id': fields.Integer,
# 	'individuals': fields.List(fields.Nested(individual_resource_fields, allow_null=True)),
# 	'housing_type': fields.String
# }

# Define household and individual resources and corresponding get/ post/ put/ patch/ delete methods

# class HouseholdResource(Resource):
# 	@marshal_with(household_resource_fields)
# 	def get(self):
# 		args = household_get_args.parse_args(strict=True)

# 		if False:
# 			abort(400) # client error: bad request

# 		result = Household.query.filter_by(id=id).first()

# 		if result is None:
# 			abort(404) # client error: not found
		
# 		return result, 200 # success: ok

# 	@marshal_with(household_resource_fields)
# 	def post(self):
# 		args = household_post_args.parse_args(strict=True)

# 		if False:
# 			abort(400) # client error: bad request
		
# 		household = Household(
# 			id=args['id'], 
# 			individuals=args['individuals'], 
# 			housing_type=args['housingtype']
# 			)

# 		db.session.add(household)
# 		db.session.commit()

# 		return household, 201 # success: created

# 	@marshal_with(household_resource_fields)
# 	def put(self):
# 		args = household_post_args.parse_args(strict=True)

# 		return 400 # client error: bad request
# 		return 200 # success: ok

# 	@marshal_with(household_resource_fields)
# 	def patch(self):
# 		args = household_patch_args.parse_args(strict=True)
		
# 		return 400 # client error: bad request
# 		return 200 # success: ok
	
# 	@marshal_with(household_resource_fields)
# 	def delete(self):
# 		args = household_get_args.parse_args(strict=True)
		
# 		return 400 # client error: bad request
# 		return 200 # success: ok

class IndividualResource(Resource):
	@marshal_with(individual_resource_fields)
	def get(self):
		args = individual_get_args.parse_args(strict=True)

		if not valid_individual_args('get', args):
			abort(400) # client error: bad request

		result = Individual.query

		if args['nric'] is not None:
			result = result.filter(Individual.nric == args['nric'])

		if args['name'] is not None:
			result = result.filter(Individual.name.like('%' + args['name'] + '%'))

		if args['gender'] is not None:
			result = result.filter(Individual.gender.value == args['gender'])

		if args['maritalstatus'] is not None:
			result = result.filter(Individual.marital_status.value == args['maritalstatus'])

		if args['spouse'] is not None:
			result = result.filter(Individual.spouse.nric == args['spouse'])

		if args['occupationtype'] is not None:
			result = result.filter(Individual.occupation_type.value == args['occupationtype'])

		if args['annualincomebelow'] is not None:
			result = result.filter(Individual.annual_income < args['annualincomebelow'])

		if args['annualincomeabove'] is not None:
			result = result.filter(Individual.annual_income > args['annualincomeabove'])

		if args['dateofbirthbefore'] is not None:
			result = result.filter(Individual.date_of_birth < datetime.datetime.strptime(args['dateofbirthbefore'], '%Y-%m-%d'))

		if args['dateofbirthafter'] is not None:
			result = result.filter(Individual.date_of_birth > datetime.datetime.strptime(args['dateofbirthafter'], '%Y-%m-%d'))
	
		if result is None:
			abort(404) # client error: not found

		return result.all(), 200 # success: ok

	@marshal_with(individual_resource_fields)
	def post(self):
		args = individual_post_args.parse_args(strict=True)

		if not valid_individual_args('post', args):
			abort(400) # client error: bad request

		result = Individual.query.filter_by(nric=args['nric']).first()

		if result:
			abort(409) # client error: conflict

		if args['spouse']:
			spouse = Individual.query.filter_by(nric=args['spouse']).first()

			if spouse is None:
				abort(409) # client error: conflict

			if \
			not (args['maritalstatus'] == 'married' or args['maritalstatus'] == 'widowed') or \
			spouse.gender.value == args['gender'] or \
			(spouse.spouse is not None and spouse.spouse.nric != args['nric']):
				abort(409) # client error: conflict

		individual = Individual(
			nric=args['nric'],
			name=args['name'], 
			gender=args['gender'], 
			marital_status=args['maritalstatus'], 
			spouse=Individual.query.filter_by(nric=args['spouse']).first(), 
			occupation_type=args['occupationtype'], 
			annual_income=args['annualincome'],
			date_of_birth=datetime.datetime.strptime(args['dateofbirth'], '%Y-%m-%d'),
			# household_id
		)

		db.session.add(individual)
		db.session.commit()

		if args['spouse']:
			spouse = Individual.query.filter_by(nric=args['spouse']).first()
			spouse.spouse = individual
			spouse.marital_status = individual.marital_status
			individual.spouse_nric = spouse.nric
			spouse.spouse_nric = individual.nric
			db.session.commit()

		return individual, 201 # success: created

	@marshal_with(individual_resource_fields)
	def put(self):
		args = individual_post_args.parse_args(strict=True)

		return 400 # client error: bad request
		return 200 # success: ok

	@marshal_with(individual_resource_fields)
	def patch(self):
		args = individual_patch_args.parse_args(strict=True)

		return 400 # client error: bad request
		return 200 # success: ok
	
	@marshal_with(individual_resource_fields)
	def delete(self):
		args = individual_get_args.parse_args(strict=True)

		return 400 # client error: bad request
		return 200 # success: ok

# Add household and individual resources to api

# api.add_resource(HouseholdResource, '/households')
api.add_resource(IndividualResource, '/individuals')

if __name__ == '__main__':
	app.run(debug=True)