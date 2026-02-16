import datetime
from age_test_utils import run_age_program, assert_minimum_format, extract_current_year, extract_age

def test_06_birth_2005():
    out = run_age_program(2005)
    assert_minimum_format(out)

    got_year = extract_current_year(out)
    got_age = extract_age(out)

    expected_year = datetime.date.today().year
    expected_age = expected_year - 2005

    assert got_year == expected_year
    assert got_age == expected_age
