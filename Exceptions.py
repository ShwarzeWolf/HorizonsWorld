class HorizonsWorldExceptions(Exception):
    """Base class to store all Exceptions which could be raised by this project"""
    pass


class HeroNotFoundException(HorizonsWorldExceptions):
    """Exception raised then no hero with such id was found in database"""
    pass
