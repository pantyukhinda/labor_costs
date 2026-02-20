from fastapi import HTTPException, status


class LaborCostsException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UsersAlreadyExistsException(LaborCostsException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"


class IncorrectEmailOrPasswordException(LaborCostsException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect email or password"


class TokenExpiredException(LaborCostsException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token has expired"


class TokenAbsentException(LaborCostsException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token is missing"


class IncorrectTokenFormatException(LaborCostsException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format"


class NoSuchOrganizationException(LaborCostsException):
    status_code = status.HTTP_409_CONFLICT
    detail = "No such organization has been found"
