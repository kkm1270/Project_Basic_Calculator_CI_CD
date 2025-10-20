# from playwright.sync_api import Page
# import pytest
# from playwright.sync_api import sync_playwright

# class login:
#     def __init__(self,page):
#         self.page=page
#         self.url="https://practicetestautomation.com/practice-test-login/"
#         self.current_url= page.url
#         self.username="#username"
#         self.password="#password"
#         self.login_button="#submit"
#         self.title=("text=Test login")
#         self.home=("text=Practice")
#         self.courses=("text=Courses")
#         self.course=("text=Selenium WebDriver: Selenium Automation Testing with Python")
#         self.blog =("text=Blog")
#         self.next=("text=Next")
#         self.contacts=("text=Contact")
#         self.first_name="#wpforms-161-field_0"
#         self.second_name="#wpforms-161-field_0-last"
#         self.email=self.page.get_by_label("Email")
#         self.message=self.page.get_by_label("Message")
#         self.submit="wpforms-submit-161"
#         self.captcha_error="#wpforms-error"

#     def load_website(self):
#         self.page.goto(self.url,timeout=10000)
#         self.page.wait_for_timeout(2000)
#     def website_title(self):
#         title_found=self.page.title()
#         print(title_found)
#         return self.page.is_visible(self.title,timeout=10000)
#     def login_website(self):
#         self.page.locator("#username").scroll_into_view_if_needed()
#         self.page.fill(self.username,"student",timeout=10000)
#         self.page.fill(self.password,"Password123",timeout=10000)
#         self.page.locator("#submit").scroll_into_view_if_needed()
#         self.page.wait_for_timeout(2000)
#         self.page.click(self.login_button,timeout=10000)
#         self.page.wait_for_timeout(2000)
#     def home_page(self):
#         self.page.click(self.home,timeout=2000)
#         self.page.wait_for_timeout(2000)
#     def courses_page(self):
#          self.page.locator(self.courses).nth(0).click(timeout=3000)
#          with self.page.context.expect_page() as new_page_info:
#             self.page.locator(self.course).scroll_into_view_if_needed()
#             self.page.click(self.course)
#             self.page.wait_for_timeout(5000)
#             new_page=new_page_info.value
#             new_page.wait_for_timeout(20000)
#             new_page.close()
#             self.page.bring_to_front()
#             self.page.wait_for_timeout(2000)
#             print("Navigated back to the page:",self.page.url)
#             return self.page.url
#     def blog_page(self):
#         self.page.locator(self.courses).nth(1).scroll_into_view_if_needed(timeout=2000)
#         self.page.click(self.blog,timeout=2000)
#         self.page.locator(self.next).scroll_into_view_if_needed(timeout=2000)
#         self.page.click(self.next,timeout=2000)
#         self.page.wait_for_timeout(5000)
#         print("The Opened Page is:",self.page.url)
#         return self.page.url
#     def contact(self):
#         self.page.locator(self.courses).nth(2).scroll_into_view_if_needed(timeout=2000)
#         self.page.click(self.contacts, timeout=5000)
#         return self.page.url
#     def details(self):
#         self.page.locator(self.first_name).scroll_into_view_if_needed(timeout=10000)
#         self.page.fill(self.first_name,"test",timeout=3000)
#         self.page.fill(self.second_name,"test",timeout=2000)
#         self.page.locator(self.email).scroll_into_view_if_needed()
#         self.page.fill(self.email,"test@gmail.com",timeout=2000)
#         #self.page.locator(self.message).scroll_into_view_if_needed()
#         self.page.fill(self.message,"When people eat too much spicy foods the walls of the stomach may be damange in severe cases painful wound may be develop which is called ulcer.",timeout=2000)
#         self.page.locator(self.submit).scroll_into_view_if_needed(timeout=1000)
#         self.page.click(self.submit,timeout=2000)
#         return self.page.locator(self.captcha_error).is_visible()
