from playwright.sync_api import Page
import random
import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

class login:
    def __init__(self,page):
        self.page=page
    def load_website(self):
        url="https://testsheepnz.github.io/BasicCalculator.html"
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")
        return self.page.url
    def addition(self):
        first_number_label = self.page.locator('text="First number"')
        first_number_input=self.page.locator('[data-testid="number1Field"]')
        second_number_input=self.page.locator("#number2Field")
        calculate_button=self.page.locator("#calculateButton")
        answer_box=self.page.locator("#numberAnswerField")
        first_value="34"
        second_value="44"
        first_number_label.scroll_into_view_if_needed()
        first_number_label.wait_for(state="visible",timeout=30000)
        first_number_input.fill(first_value)
        second_number_input.fill(second_value)
        calculate_button.click()
        value_added=answer_box.input_value()
        print(f"{value_added}")
        return value_added
    def subtract_clear(self):
        clear_button=self.page.locator("#clearButton")
        answer_box=self.page.locator("#numberAnswerField")
        clear_button.scroll_into_view_if_needed()
        clear_button.wait_for(state="visible",timeout=30000)
        clear_button.click()
        self.page.wait_for_timeout(1000)
        return answer_box
    def subtract(self):
        menu=self.page.locator("#selectOperationDropdown")
        first_number_input=self.page.locator('[data-testid="number1Field"]')
        second_number_input=self.page.locator("#number2Field")
        calculate_button=self.page.locator("#calculateButton")
        answer_box=self.page.locator("#numberAnswerField")
        first_number="80"
        second_number="44"
        menu.click()
        menu.select_option('1')
        self.page.wait_for_timeout(1000)
        first_number_input.clear()
        first_number_input.fill(first_number)
        self.page.wait_for_timeout(1000)
        second_number_input.clear()
        second_number_input.fill(second_number)
        self.page.wait_for_timeout(2000)
        calculate_button.click()
        self.page.wait_for_timeout(2000)
        value_subtracted=answer_box.input_value()
        print(f"{value_subtracted}")
        return value_subtracted
    def multiply(self):
        menu=self.page.locator("#selectOperationDropdown")
        first_number_input=self.page.locator('[data-testid="number1Field"]')
        second_number_input=self.page.locator("#number2Field")
        calculate_button=self.page.locator("#calculateButton")
        answer_box=self.page.locator("#numberAnswerField")
        first_multiplication_Value="340"
        second_multiplication_value="12"
        menu.click()
        menu.select_option('2')
        self.page.wait_for_timeout(1000)
        first_number_input.clear()
        second_number_input.clear()
        first_number_input.fill(first_multiplication_Value)
        second_number_input.fill(second_multiplication_value)
        calculate_button.click()
        self.page.wait_for_timeout(2000)
        value_multiplicated=answer_box.input_value()
        print(f"{value_multiplicated}")
        return value_multiplicated
    def division(self):
        menu=self.page.locator("#selectOperationDropdown")
        first_number_input=self.page.locator('[data-testid="number1Field"]')
        second_number_input=self.page.locator("#number2Field")
        calculate_button=self.page.locator("#calculateButton")
        answer_box=self.page.locator("#numberAnswerField")
        first_division_value="75"
        second_division_Value="5"
        menu.click()
        menu.select_option('3')
        self.page.wait_for_timeout(1000)
        first_number_input.clear()
        first_number_input.fill(first_division_value)
        second_number_input.clear()
        second_number_input.fill(second_division_Value)
        self.page.wait_for_timeout(2000)
        calculate_button.click()
        self.page.wait_for_timeout(2000)
        value_divided=answer_box.input_value()
        print(f"{value_divided}")
        return value_divided


        
























