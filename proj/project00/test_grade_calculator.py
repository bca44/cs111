from byu_pytest_utils import dialog, max_score

@max_score(50)
@dialog('test_files/input1.dialog.txt', 'grade_calculator.py')
def test_grade_1():
    ...

@max_score(50)
@dialog('test_files/input2.dialog.txt', 'grade_calculator.py')
def test_grade_2():
    ...