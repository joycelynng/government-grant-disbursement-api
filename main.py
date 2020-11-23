from flask import Flask
from flask_restful import Api, Resource, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

from enumerations import *
from requestparsers import *

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Define household and individual database tables/ schema

class Household(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	individuals = db.relationship('Individual', backref='household')
	housingtype = db.Column(db.Enum(HousingType), nullable=False)

	def __repr__(self):
		return

class Individual(db.Model):
	nric = db.Column(db.String(9), primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	gender = db.Column(db.Enum(Gender), nullable=False)
	maritalstatus = db.Column(db.Enum(MaritalStatus), nullable=False)
	spouse = db.relationship('Individual', backref='spouse')
	occupationtype = db.Column(db.Enum(OccupationType), nullable=False)
	annualincome = db.Column(db.Integer, nullable=False)
	dateofbirth = db.Column(db.Date, nullable=False)

	def __repr__(self):
		return

# Set up resource fields for household and individual, to format how household/ individual resource data is rendered in response

individual_resource_fields = {}

individual_resource_fields = {
	'nric': fields.String,
	'name': fields.String,
	'gender': fields.String,
	'maritalstatus': fields.String,
	'spouse': fields.Nested(individual_resource_fields, allow_null=True),
	'occupationtype': fields.String,
	'annualincome': fields.String,
	'dateofbirth': fields.DateTime(dt_format='rfc822')
}

household_resource_fields = {
	'id': fields.Integer,
	'individuals': fields.List(fields.Nested(individual_resource_fields, allow_null=True)),
	'housingtype': fields.String
}

# Define household and individual resources and corresponding get/ post/ put/ patch/ delete methods

class HouseholdResource(Resource):
	@marshal_with(household_resource_fields)
	def get(self, path):
		return

	@marshal_with(household_resource_fields)
	def post(self, path):
		args = household_post_args.parse_args(strict=True)
		return

	@marshal_with(household_resource_fields)
	def put(self, path):
		args = household_put_args.parse_args(strict=True)
		return

	@marshal_with(household_resource_fields)
	def patch(self, path):
		args = household_patch_args.parse_args(strict=True)
		return	
	
	@marshal_with(household_resource_fields)
	def delete(self, path):
		return

class IndividualResource(Resource):
	@marshal_with(individual_resource_fields)
	def get(self, path):
		return

	@marshal_with(individual_resource_fields)
	def post(self, path):
		args = individual_post_args.parse_args(strict=True)
		return	

	@marshal_with(individual_resource_fields)
	def put(self, path):
		args = individual_put_args.parse_args(strict=True)
		return

	@marshal_with(individual_resource_fields)
	def patch(self, path):
		args = individual_patch_args.parse_args(strict=True)
		return	
	
	@marshal_with(individual_resource_fields)
	def delete(self, path):
		return

api.add_resource(HouseholdResource, '/households/<string:path>')
api.add_resource(IndividualResource, '/individuals/<string:path>')

if __name__ == '__main__':
	app.run(debug=True)