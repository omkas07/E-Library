from enum import Enum

class Role(str, Enum):
    USER = "user"
    GBA = "GBA"
    KA = "KA"
    AZ = "AZ"

class Membership(str, Enum):
    BASIC = "basic"
    SCHOOL = "school"
    COLLAGE = "collage"
    PENSION = "pension"

class BookCopyStatus(str, Enum):
    GOOD = "good"
    DIRTY = "dirty"
    TERRIBLE = "terrible"
