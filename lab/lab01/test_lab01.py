from byu_pytest_utils import max_score, dialog, test_files, this_folder

@max_score(5)
@dialog(test_files / 'test_good_input1.dialog.txt', this_folder / 'lab01.py')
def test_good_input_1():
    pass

@max_score(5)
@dialog(test_files / 'test_good_input2.dialog.txt', this_folder / 'lab01.py')
def test_good_input_2():
    pass

@max_score(5)
@dialog(test_files / 'test_good_input3.dialog.txt', this_folder / 'lab01.py')
def test_good_input_3():
    pass

@max_score(2.5)
@dialog(test_files / 'test_bad_input1.dialog.txt', this_folder / 'lab01.py')
def test_bad_input_1():
    pass

@max_score(2.5)
@dialog(test_files / 'test_bad_input2.dialog.txt', this_folder / 'lab01.py')
def test_bad_input_2():
    pass
