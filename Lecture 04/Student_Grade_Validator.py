class InvalidGradeError(Exception):
    pass


def validate_grade(value):
    try:
        grade = float(value)

        if grade < 0 or grade > 100:
            raise InvalidGradeError("Grade must be between 0 and 100")

        return grade

    except ValueError:
        raise InvalidGradeError("Please enter a numeric value")


# User Interface
value = input("Enter student grade: ")

try:
    grade = validate_grade(value)
    print("Valid grade:", grade)

except InvalidGradeError as e:
    print("Error:", e)