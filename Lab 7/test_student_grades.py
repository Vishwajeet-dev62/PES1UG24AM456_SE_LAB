
import pytest
from hypothesis import given, strategies as st

from student_grades import average_marks, parse_srn, short_name


# --------------------------------------------------
# 1. AVERAGE MARKS - VALID INPUTS
# --------------------------------------------------

@given(
    st.lists(
        st.integers(min_value=0, max_value=100),
        min_size=1,
        max_size=20
    )
)
def test_average_marks_valid(marks):

    csv_input = ",".join(map(str, marks))
    expected = round(sum(marks) / len(marks), 2)

    assert average_marks(csv_input) == expected


# --------------------------------------------------
# 2. AVERAGE MARKS - INVALID INPUTS
# --------------------------------------------------

@given(
    st.sampled_from([
        "",
        " ",
        ",",
        "10,",
        ",20",
        "10,,20",
        "abc",
        "10,abc,20",
        "10.5,20",
        "-10,20",
        "101,20"
    ])
)
def test_average_marks_invalid(s):

    with pytest.raises(ValueError):
        average_marks(s)


@given(st.one_of(st.none(), st.integers(), st.lists(st.integers())))
def test_average_marks_wrong_type(s):

    with pytest.raises(ValueError):
        average_marks(s)


# --------------------------------------------------
# 3. PARSE SRN - VALID INPUTS
# --------------------------------------------------

@given(
    year=st.integers(min_value=0, max_value=99),
    dept=st.text(
        alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        min_size=2,
        max_size=2
    ),
    number=st.integers(min_value=0, max_value=999)
)
def test_parse_srn_valid(year, dept, number):

    srn = f"PES1UG{year:02d}{dept}{number:03d}"

    result = parse_srn(srn)

    assert result == ("PES1", year, dept)


# --------------------------------------------------
# 4. PARSE SRN - INVALID INPUTS
# --------------------------------------------------

@given(
    suffix=st.text(
        alphabet="abcdefghijklmnopqrstuvwxyz",
        min_size=5,
        max_size=5
    )
)
def test_parse_srn_invalid_suffix(suffix):

    srn = "PES1UG23" + suffix

    with pytest.raises(ValueError):
        parse_srn(srn)


@given(
    year=st.text(
        alphabet="abcdefghijklmnopqrstuvwxyz",
        min_size=2,
        max_size=2
    )
)
def test_parse_srn_invalid_year(year):

    srn = "PES1UG" + year + "CS123"

    with pytest.raises(ValueError):
        parse_srn(srn)


@given(
    srn=st.text(
        alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        min_size=0,
        max_size=20
    )
)
def test_parse_srn_invalid_format(srn):

    if not (
        len(srn) == 13
        and srn.startswith("PES1UG")
        and srn[6:8].isdigit()
        and srn[8:10].isalpha()
        and srn[10:13].isdigit()
    ):
        with pytest.raises(ValueError):
            parse_srn(srn)


@given(st.one_of(st.none(), st.integers()))
def test_parse_srn_wrong_type(srn):

    with pytest.raises(ValueError):
        parse_srn(srn)


# --------------------------------------------------
# 5. SHORT NAME - VALID INPUTS
# --------------------------------------------------

@given(
    first=st.text(
        alphabet="abcdefghijklmnopqrstuvwxyz",
        min_size=1,
        max_size=15
    ),
    last=st.text(
        alphabet="abcdefghijklmnopqrstuvwxyz",
        min_size=1,
        max_size=15
    )
)
def test_short_name_valid(first, last):

    result = short_name(f"{first} {last}")

    expected = first[0].upper() + ". " + last.capitalize()

    assert result == expected


# --------------------------------------------------
# 6. SHORT NAME - INVALID INPUTS
# --------------------------------------------------

@given(
    name=st.sampled_from([
        "",
        " ",
        "ravi",
        "ravi kumar reddy",
        "ravi  kumar reddy",
        "ravi kumar reddy sharma"
    ])
)
def test_short_name_invalid(name):

    with pytest.raises(ValueError):
        short_name(name)


@given(st.one_of(st.none(), st.integers(), st.lists(st.text())))
def test_short_name_wrong_type(name):

    with pytest.raises(ValueError):
        short_name(name)
