from byu_pytest_utils import max_score, dialog, test_files, this_folder, ensure_missing, visibility


def create_doubled_constants_file(source_file, output_file):
    """Reads the source file, doubles all constants, and saves the result to output_file."""
    with open(source_file, "r") as src:
        lines = src.readlines()

    with open(output_file, "w") as dest:
        for line in lines:
            parts = line.split("=")
            if len(parts) == 2 and parts[0].strip().isupper():
                try:
                    value = eval(parts[1].strip())
                    if isinstance(value, (int, float)):
                        doubled_value = value * 2
                        dest.write(f"{parts[0].strip()} = {doubled_value}\n")
                    else:
                        dest.write(line)
                except:
                    dest.write(line)
            else:
                dest.write(line)

    return output_file

@max_score(4)
@dialog(test_files / "test_1_person_35_tip.txt", this_folder / "homework0.py")
def test_1_person_35_tip():
    ...


@max_score(4)
@dialog(test_files / "test_3_person_80_tip.txt", this_folder / "homework0.py")
def test_3_person_80_tip():
    ...


@max_score(4)
@dialog(test_files / "test_4_person_35_tip.txt", this_folder / "homework0.py")
def test_4_person_35_tip():
    ...


@max_score(4)
@dialog(test_files / "test_7_person_80_tip.txt", this_folder / "homework0.py")
def test_7_person_80_tip():
    ...


@max_score(4)
@dialog(test_files / "test_8_person_80_tip.txt", this_folder / "homework0.py")
def test_8_person_80_tip():
    ...


@max_score(2)
@dialog(test_files / "test_10_person_35_tip.txt", this_folder / "homework0.py")
def test_10_person_35_tip():
    ...


@max_score(2)
@dialog(test_files / "test_11_person_10_tip.txt", this_folder / "homework0.py")
def test_11_person_10_tip():
    ...


@max_score(2)
@dialog(test_files / "test_12_person_80_tip.txt", this_folder / "homework0.py")
def test_12_person_80_tip():
    ...


@max_score(2)
@dialog(test_files / "test_13_person_80_tip.txt", this_folder / "homework0.py")
def test_13_person_80_tip():
    ...


@max_score(2)
@dialog(test_files / "test_14_person_10_tip.txt", this_folder / "homework0.py")
def test_14_person_10_tip():
    ...


@max_score(5)
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_15_person_35_tip.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_15_person_35_tip_doubled():
    ...


@max_score(5)
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_16_person_80_tip.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_16_person_80_tip_doubled():
    ...


@max_score(5)
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_17_person_10_tip.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_17_person_10_tip_doubled():
    ...


@max_score(5)
@ensure_missing(this_folder / 'homework0-doubled.py')
@dialog(test_files / "test_100_person_80_tip.txt", create_doubled_constants_file(this_folder / "homework0.py", this_folder / "homework0-doubled.py"))
def test_100_person_80_tip_doubled():
    ...


@max_score(0)
@ensure_missing(this_folder / 'homework0-doubled.py')
@visibility('hidden')
def test_doubled_clean():
    ...
