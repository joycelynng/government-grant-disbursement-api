from enum import Enum

class HousingType(Enum):
    hdb = 'hdb'
    condominium = 'condominium'
    landed = 'landed'

class Gender(Enum):
    male = 'male'
    female = 'female'

class MaritalStatus(Enum):
    single = 'single'
    married = 'married'
    widowed = 'widowed'
    divorced = 'divorced'
    separated = 'separated'

class OccupationType(Enum):
    employed = 'employed'
    unemployed = 'unemployed'
    student = 'student'

housing_type_choices = ('hdb', 'condominium', 'landed')
gender_choices = ('male', 'female')
marital_status_choices = ('single', 'married', 'widowed', 'divorced', 'separated')
occupation_type_choices = ('employed', 'unemployed', 'student')
grant_choices = ('studentencouragement', 'familytogetherness', 'elder', 'babysunshine', 'yologst')