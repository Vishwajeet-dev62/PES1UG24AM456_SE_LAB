
import re


def average_marks(marks_csv):
    """Calculate the average of comma-separated marks."""

    if not isinstance(marks_csv, str):
        raise ValueError("Marks must be provided as a CSV string")

    if not marks_csv.strip():
        raise ValueError("Marks cannot be empty")

    values = marks_csv.split(",")

    marks = []

    for value in values:
        value = value.strip()

        if not value:
            raise ValueError("Empty mark found")

        try:
            mark = int(value)
        except ValueError:
            raise ValueError("Marks must contain valid integers")

        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")

        marks.append(mark)

    return round(sum(marks) / len(marks), 2)


def parse_srn(srn):
    """Extract campus, year and department from an SRN."""

    if not isinstance(srn, str):
        raise ValueError("SRN must be a string")

    pattern = r"PES1UG(\d{2})([A-Z]{2})(\d{3})"

    match = re.fullmatch(pattern, srn)

    if not match:
        raise ValueError("Invalid SRN format")

    year = int(match.group(1))
    department = match.group(2)

    return "PES1", year, department


def short_name(full_name):
    """Convert a full name into an abbreviated name."""

    if not isinstance(full_name, str):
        raise ValueError("Name must be a string")

    parts = full_name.split()

    if len(parts) != 2:
        raise ValueError("Enter exactly first name and last name")

    first, last = parts

    return first[0].upper() + ". " + last.capitalize()


def main():

    print("==== Running average_marks ====")

    try:
        user_input = input("Enter marks as CSV (e.g. 78,85,92): ")
        result = average_marks(user_input)
        print("Average Marks:", result)
    except ValueError as error:
        print("Error:", error)

    print("\n==== Running parse_srn ====")

    try:
        user_input = input("Enter an SRN (e.g. PES1UG23CS123): ")
        result = parse_srn(user_input)
        print("Campus, Year and Dept:", result)
    except ValueError as error:
        print("Error:", error)

    print("\n==== Running short_name ====")

    try:
        user_input = input("Enter first and last name (e.g. ravi kumar): ")
        result = short_name(user_input)
        print("Short Name:", result)
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
