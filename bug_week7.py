# bug_week7.py
# BUG OF THE WEEK - Week 7: Functions
#
# INSTRUCTIONS: This file has 4 bugs in it.
# Use the comments and the test file to help you find and fix them.
#
# Bug 1: Find with the console error message.
# Bug 2: Find with the VS Code Debugger.
# Bug 3: Find with the VS Code Debugger + test cases.
# Bug 4: Can ONLY be found by a thoughtful test case —
#         the one the test file (test_week7.py) calls TEST 10.
#
# This file contains the functions that test_week7.py checks.
# Keep this file and test_week7.py in the SAME folder.


# ============================================================
# FUNCTION 1: format_student()
# ============================================================
def format_student(first_name, last_name, student_id):
    # Make the names look neat: first letter uppercase,
    # remaining letters lowercase.
    first = first_name.title()
    last = last_name.title()

    # Return the student's name and ID in the required format.
    return f"{last}, {first}  (ID: {student_id})"


# ============================================================
# FUNCTION 2: apply_discount()
# ============================================================
def apply_discount(price, discount_percent):
    # Calculate the amount of money taken off the original price.
    discount_amount = price * discount_percent / 100

    # Subtract the discount amount from the original price.
    discounted = price - discount_amount

    # Round to two decimal places because prices use cents.
    return round(discounted, 2)


# ============================================================
# FUNCTION 3: format_schedule()
# ============================================================
def format_schedule(student_name, courses):
    # Start with a heading. .title() capitalizes the student's name.
    result = f"Schedule for {student_name.title()}:\n"

    # Add one line for each course in the list.
    for course in courses:
        result += f"  - {course}\n"

    # Return the completed schedule string.
    # Without this return, the function would give back None.
    return result


# ============================================================
# FUNCTION 4: build_roster()
# ============================================================
def build_roster(course_name, students=None):
    # IMPORTANT: Use None as the default, not a list.
    # A default list can be shared between different function calls.
    # Creating a new list inside the function keeps each call separate.
    if students is None:
        students = ["(enrolled)"]

    # Return a dictionary whose key is the course name.
    return {course_name: students}


# ============================================================
# DEMO CODE
# This section runs only when you run bug_week7.py directly.
# When test_week7.py imports this file, the demo does not run.
# ============================================================
if __name__ == "__main__":
    print("Student:", format_student("jordan", "smith", "S001"))
    print("Discount:", apply_discount(50.00, 20))
    print("Schedule:")
    print(format_schedule("maria", ["Python", "Circuits"]), end="")
    print("Roster:", build_roster("Python"))
