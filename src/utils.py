import re


def checkPasswordStrength(password: str) -> bool:
    regEx = re.compile(
        r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[\d])(?=.*[!@#$%^&*()]).{8,}$")
    return regEx.search(password) is not None


def findAllPhoneNumbers(text: str) -> list[str]:
    regEx = re.compile(
        r"(?=(?<=[^\d])|(?<=^))(\+7|8)\s?(\s|-|\(|)?\d{3}(\2|\)(\s|-)?)\d{3}(\s|-|)?\d{2}\5\d{2}(?=[^\d]|$)")

    return list(map(lambda x: x[0], regEx.finditer(text)))


def findEmails(text: str):
    regEx = re.compile(
        r"[\w\d+_~-]+@[\w\d.-]+.\w+")

    return list(map(lambda x: x[0], regEx.finditer(text)))


def excludeForSingleQuotes(text: str) -> str:
    return text.replace("'", "\\'").replace("\\", "\\\\")


def commandArgsToExcludedStr(args: list[str]) -> str:
    text = ""

    for arg in args:
        text += f"'{excludeForSingleQuotes(arg)}' "

    return text
