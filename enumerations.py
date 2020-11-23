from enum import Enum

class HousingType(Enum):
    hdb = "hdb"
    condominium = "condominium"
    landed = "landed"

class Gender(Enum):
    male = "male"
    female = "female"

class MaritalStatus(Enum):
    single = "single"
    married = "married"
    widowed = "widowed"
    divorced = "divorced"
    separated = "separated"

class OccupationType(Enum):
    employed = "employed"
    unemployed = "unemployed"
    student = "student"