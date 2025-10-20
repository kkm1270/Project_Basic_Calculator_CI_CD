from playwright.sync_api import sync_playwright
from playw_page_1 import login

def test_case_1(browser):
    expected_url="https://testsheepnz.github.io/BasicCalculator.html"
    case_1=login(browser)
    current_url=case_1.load_website()
    assert current_url == expected_url,"Login Page Title is not Visible."
def test_case_2(browser):
    first_Value="34"
    second_value="44"
    total_addition=str(int(first_Value) + int(second_value))
    case_2=login(browser)
    result=case_2.addition()
    assert result == total_addition, "Calculate heading is not visible"
def test_case_3(browser):
    case_3=login(browser)
    answer_box_Value=case_3.subtract_clear()
    current_value=answer_box_Value.input_value()
    print(f"Current Value in Answer Box is:'{current_value}'")
    assert current_value == "", "Answer box not cleared."
def test_case_4(browser):
    first_value="80"
    second_value="44"
    subtracted_value=str(int(first_value) - int(second_value))
    case_4=login(browser)
    result=case_4.subtract()
    assert result == subtracted_value, "Subtraction not happened."
def test_case_5(browser):
    first_Value="340"
    second_Value="12"
    multiplicated_value=str(int(first_Value) * int(second_Value))
    case_5=login(browser)
    answer_box=case_5.multiply()
    assert answer_box == multiplicated_value, "Multiplication not Happened."
def test_case_6(browser):
    first_value="75"
    second_value="5"
    divided_value=str(int(int(first_value) / int(second_value)))
    case_6=login(browser)
    result_of_division=case_6.division()
    assert result_of_division == divided_value, "Division not Happened."













