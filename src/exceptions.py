class HorizonsWorldExceptions(Exception):
    """Base class to store all Exceptions which could be raised by this project"""
    pass


class HeroNotFoundException(HorizonsWorldExceptions):
    """Exception raised then no hero with such id was found in database"""
    pass


class IncorrectHeroBirthdayException(HorizonsWorldExceptions):
    """Exception raised then Hero birthday could not be converted into date"""
    pass


class NoSuchHeroSideException(HorizonsWorldExceptions):
    """Exception raised then users tries to add Hero side, which is not listed in enum Sides"""
    pass
