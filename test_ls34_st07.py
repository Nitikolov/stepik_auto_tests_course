import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("\n^_^")
    yield
    print("\n:3")


@pytest.fixture()
def very_important_fixture():
    print("\n:)")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print("\n:-Р")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        print("start test 1")
        # какие-то проверки
        print("finish test 1")
        pass

    def test_second_smiling_faces(self, prepare_faces):
        print("start test 2")
        # какие-то проверки
        print("finish test 3")
        pass

