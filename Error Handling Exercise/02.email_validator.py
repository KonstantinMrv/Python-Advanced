class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainOnlySmallLettersError(Exception):
    pass


class InvalidCharactersUsedError(Exception):
    pass


class MustContainOnlyOneAtSymbol(Exception):
    pass


email = input("Please, enter an email to validate: ")
INVALID_CHARACTERS = ["?", "!", "|", "&", "#", "%", "^", "*", ".", "/", "\\"]
VALID_DOMAINS = ["com", "bg", "org", "net"]

while email != "End":

    if "@" not in email:
        raise MustContainAtSymbolError("The email should contain @ symbol!")

    if email.count("@") > 1:
        raise MustContainOnlyOneAtSymbol("The email should contain only one @ symbol!")

    name, second = email.split("@")
    domain = second.split(".")

    if len(name) <= 4:
        raise NameTooShortError("The name must contain more than 4 characters!")

    if domain[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Invalid domain!")
    elif len(domain) > 2:
        raise InvalidDomainError("Invalid domain!")

    for el in name:
        if el.isupper():
            raise MustContainOnlySmallLettersError("The email should contain only small letters!")

        if el in INVALID_CHARACTERS:
            raise InvalidCharactersUsedError("Invalid characters used!")

    print("The email is valid.")

    email = input("Please, enter an email to validate: ")

