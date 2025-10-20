import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session", params=["chrome"])
def browser(request):
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True,channel=request.param)  
        context = browser.new_context(
            viewport={"width":1200, "height":720}
        )
        page = context.new_page()
        yield page
        context.close()
        browser.close()