
import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# -------------------------------
# LETTER GRADE TESTS
# -------------------------------

def test_grade_s():
    assert letter_grade(95) == "S"


def test_grade_a():
    assert letter_grade(85) == "A"


def test_grade_b():
    assert letter_grade(75) == "B"


def test_grade_c():
    assert letter_grade(65) == "C"


def test_grade_d():
    assert letter_grade(55) == "D"


def test_grade_e():
    assert letter_grade(45) == "E"


def test_grade_f():
    assert letter_grade(30) == "F"


def test_invalid_negative_marks():
    with pytest.raises(ValueError):
        letter_grade(-1)


def test_invalid_marks_above_100():
    with pytest.raises(ValueError):
        letter_grade(101)


# -------------------------------
# FINAL MARKS TESTS
# -------------------------------

def test_final_marks_without_project():
    assert final_marks(30, 50, False) == 80


def test_final_marks_with_project():
    assert final_marks(30, 50, True) == 85


def test_project_bonus_capped_at_100():
    assert final_marks(40, 60, True) == 100


def test_invalid_internal_marks():
    with pytest.raises(ValueError):
        final_marks(41, 50, False)


def test_invalid_external_marks():
    with pytest.raises(ValueError):
        final_marks(30, 61, False)


# -------------------------------
# EXAM ELIGIBILITY TESTS
# -------------------------------

def test_fees_not_paid():
    assert exam_eligibility(90, False, False) == "blocked"


def test_eligible_with_attendance():
    assert exam_eligibility(80, True, False) == "eligible"


def test_eligible_with_medical_certificate():
    assert exam_eligibility(70, True, True) == "eligible"


def test_detained():
    assert exam_eligibility(60, True, False) == "detained"
