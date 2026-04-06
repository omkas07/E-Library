from enum import Enum

class Role(str, Enum):
    USER = "user"
    HEAD = "HEAD ADMIN"
    VICE = "VICE ADMIN"
    JUNIOR = "JUNIOR ADMIN"

class Membership(str, Enum):
    BASIC = "basic"
    SCHOOL = "school"
    COLLAGE = "collage"
    PENSION = "pension"

class BookCopyStatus(str, Enum):
    GOOD = "good"
    DIRTY = "dirty"
    TERRIBLE = "terrible"
