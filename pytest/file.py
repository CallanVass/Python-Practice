from main import *
import pytest
class TestCase:
    def will_not_run_as_a_test(self):
        print("This method won't run when pytest runs")

    def test_will_run(self):
        assert True

    def addNum(self, num1, num2):
        return num1 + num2
    
    def test_throw_example_error(self):
        result = self.addNum(5, 5)
        assert result == 10

    def test_will_pass(self):
        assert "hello" == "hello"

    def test_will_fail(self):
        assert "hello" == "world"

    def test_example_error(self):
        with pytest.raises(RuntimeError):
            throw_an_error()

test = TestCase()

test.test_will_run()
test.will_not_run_as_a_test()
test.test_throw_example_error()

test.test_will_fail()
test.test_will_pass()