from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

from enumerations import *

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Define household and individual database tables/ schema

class Household(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	individuals = db.relationship("Individual", backref="household")
	housingtype = db.Column(db.Enum(HousingType), nullable=False)

	def __repr__(self):
		return

class Individual(db.Model):
	nric = db.Column(db.String(9), primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	gender = db.Column(db.Enum(Gender), nullable=False)
	maritalstatus = db.Column(db.Enum(MaritalStatus), nullable=False)
	spouse = db.relationship("Individual", backref="spouse")
	occupationtype = db.Column(db.Enum(OccupationType), nullable=False)
	annualincome = db.Column(db.Integer, nullable=False)
	dateofbirth = db.Column(db.Date, nullable=False)

	def __repr__(self):
		return

# Set up request parsers for household and individual post/ put/ patch requests

household_post_args = reqparse.RequestParser()
household_post_args.add_argument("id", type=int, required=True) # help
household_post_args.add_argument("individuals", type=list)
household_post_args.add_argument("housingtype", type=str, required=True)

household_put_args = reqparse.RequestParser()
household_put_args.add_argument("id", type=int, required=True)
household_put_args.add_argument("individuals", type=list)
household_put_args.add_argument("housingtype", type=str, required=True)

household_patch_args = reqparse.RequestParser()
household_patch_args.add_argument("id", type=int, required=True)
household_patch_args.add_argument("individuals", type=list)
household_patch_args.add_argument("housingtype", type=str)

individual_post_args = reqparse.RequestParser()
individual_post_args.add_argument("nric", type=str, required=True) # help
individual_post_args.add_argument("name", type=str, required=True)
individual_post_args.add_argument("gender", type=str, required=True)
individual_post_args.add_argument("maritalstatus", type=str, required=True)
individual_post_args.add_argument("spouse", type=str)
individual_post_args.add_argument("occupationtype", type=str, required=True)
individual_post_args.add_argument("annualincome", type=int, required=True)
individual_post_args.add_argument("dateofbirth", type=str, required=True)

individual_put_args = reqparse.RequestParser()
individual_put_args.add_argument("nric", type=str, required=True)
individual_put_args.add_argument("name", type=str, required=True)
individual_put_args.add_argument("gender", type=str, required=True)
individual_put_args.add_argument("maritalstatus", type=str, required=True)
individual_put_args.add_argument("spouse", type=str)
individual_put_args.add_argument("occupationtype", type=str, required=True)
individual_put_args.add_argument("annualincome", type=int, required=True)
individual_put_args.add_argument("dateofbirth", type=str, required=True)

individual_patch_args = reqparse.RequestParser()
individual_patch_args.add_argument("nric", type=str, required=True)
individual_patch_args.add_argument("name", type=str)
individual_patch_args.add_argument("gender", type=str)
individual_patch_args.add_argument("maritalstatus", type=str)
individual_patch_args.add_argument("spouse", type=str)
individual_patch_args.add_argument("occupationtype", type=str)
individual_patch_args.add_argument("annualincome", type=int)
individual_patch_args.add_argument("dateofbirth", type=str)

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
		return	

	@marshal_with(household_resource_fields)
	def put(self, path):
		return

	@marshal_with(household_resource_fields)
	def patch(self, path):
		return	
	
	@marshal_with(household_resource_fields)
	def delete(self, path):
		return

class IndividualResource(Resource):
	@marshal_with(household_resource_fields)
	def get(self, path):
		return

	@marshal_with(household_resource_fields)
	def post(self, path):
		return	

	@marshal_with(household_resource_fields)
	def put(self, path):
		return

	@marshal_with(household_resource_fields)
	def patch(self, path):
		return	
	
	@marshal_with(household_resource_fields)
	def delete(self, path):
		return

api.add_resource(HouseholdResource, "/households/<string:path>")
api.add_resource(IndividualResource, "/individuals/<string:path>")

if __name__ == "__main__":
	app.run(debug=True)