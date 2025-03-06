import pytest
from byu_pytest_utils import max_score, with_import, run_python_script, this_folder, test_files, run_python_script, ensure_missing


@max_score(2)
@with_import("admissions", "check_row_types")
def test_check_row_types(check_row_types):
    assert not check_row_types([])
    assert not check_row_types([1, 2, 3, 4, 5, 6, 7])
    assert check_row_types([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
    assert not check_row_types([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert not check_row_types([1, 2, 3, 4, 5, 6, 7, 8])
    assert not check_row_types(["1", "2", "3", "4", "5", "6", "7", "8"])
    assert not check_row_types([""])


# Run the student file
@pytest.fixture(scope="module")
@ensure_missing(this_folder / "student_scores.csv")
@ensure_missing(this_folder / "chosen_students.csv")
@ensure_missing(this_folder / "outliers.csv")
@ensure_missing(this_folder / "chosen_improved.csv")
@ensure_missing(this_folder / "better_improved.csv")
@ensure_missing(this_folder / "composite_chosen.csv")
def run_program():
    script = this_folder / "admissions.py"
    try:
        run_python_script(script)
    except Exception as e:
        return e


def compare_files(observed_file, expected_file):
    with open(observed_file, 'r') as observed, open(expected_file, 'r') as expected:
        assert observed.read() == expected.read()


# Compare the output files to the expected files
@max_score(8)
def test_student_scores(run_program):
    if run_program != None: # check to see if the fixture returned any errors before trying to compare files
        raise run_program
    compare_files(this_folder / "student_scores.csv", test_files / "student_scores.key.csv")


@max_score(8)
def test_chosen_students(run_program):
    if run_program != None:
        raise run_program
    compare_files(this_folder / "chosen_students.csv", test_files / "chosen_students.key.csv")


@max_score(8)
def test_outliers(run_program):
    if run_program != None:
        raise run_program
    compare_files(this_folder / "outliers.csv", test_files / "outliers.key.csv")


@max_score(8)
def test_chosen_improved(run_program):
    if run_program != None:
        raise run_program
    compare_files(this_folder / "chosen_improved.csv", test_files / "chosen_improved.key.csv")


@max_score(8)
def test_better_improved(run_program):
    if run_program != None:
        raise run_program
    compare_files(this_folder / "better_improved.csv", test_files / "better_improved.key.csv")


@max_score(8)
def test_composite_chosen(run_program):
    if run_program != None:
        raise run_program
    compare_files(this_folder / "composite_chosen.csv", test_files / "composite_chosen.key.csv")

