
import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# =====================================
# LETTER GRADE - BRANCH COVERAGE TESTS
# =====================================

def test_grade_s():
    assert letter_grade(90) == "S"


def test_grade_s_upper_boundary():
    assert letter_grade(100) == "S"


def test_grade_a():
    assert letter_grade(80) == "A"


def test_grade_b():
    assert letter_grade(70) == "B"


def test_grade_c():
    assert letter_grade(60) == "C"


def test_grade_d():
    assert letter_grade(50) == "D"


def test_grade_e():
    assert letter_grade(40) == "E"


def test_grade_f():
    assert letter_grade(39) == "F"


def test_invalid_negative_marks():
    with pytest.raises(ValueError):
        letter_grade(-1)


def test_invalid_marks_above_100():
    with pytest.raises(ValueError):
        letter_grade(101)


# =====================================
# FINAL MARKS - BRANCH COVERAGE TESTS
# =====================================

def test_internal_marks_exceed_limit():
    with pytest.raises(ValueError):
        final_marks(41, 50, False)


def test_external_marks_exceed_limit():
    with pytest.raises(ValueError):
        final_marks(30, 61, False)


def test_both_marks_valid():
    assert final_marks(30, 50, False) == 80


def test_project_bonus_applied():
    assert final_marks(30, 50, True) == 85


def test_project_bonus_exceeds_100():
    assert final_marks(40, 60, True) == 100


def test_project_bonus_does_not_exceed_100():
    assert final_marks(20, 30, True) == 55


# =====================================
# EXAM ELIGIBILITY - BRANCH COVERAGE
# =====================================

def test_fees_not_paid():
    assert exam_eligibility(90, False, False) == "blocked"


def test_attendance_above_75():
    assert exam_eligibility(80, True, False) == "eligible"


def test_attendance_exactly_75():
    assert exam_eligibility(75, True, False) == "eligible"


def test_attendance_below_75_with_medical():
    assert exam_eligibility(70, True, True) == "eligible"


def test_attendance_65_without_medical():
    assert exam_eligibility(65, True, False) == "detained"


def test_attendance_below_65_with_medical():
    assert exam_eligibility(60, True, True) == "detained"


def test_attendance_below_65_without_medical():
    assert exam_eligibility(60, True, False) == "detained"


def test_fees_paid_and_low_attendance():
    assert exam_eligibility(50, True, False) == "detained"
