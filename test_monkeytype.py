from playwright.sync_api import sync_playwright

def type_away() -> str:
    with sync_playwright() as p:
        # Create browser instance in headed mode
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        # Navigate to page
        page.goto("https://monkeytype.com/")
        # Wait for the Dom to fully load
        page.wait_for_load_state("domcontentloaded")
        # Wait for the Accept All button
        page.get_by_role("button", name="accept all").wait_for(state="visible")
        # Click Accept All
        page.get_by_role("button", name="accept all").click()
        # Wait for Accept All button to go away
        page.get_by_role("button", name="accept all").wait_for(state="hidden")
        # Click the Words typing test(This goes by amount of words not time)
        page.locator("button[mode='words']").click()
        # Wait 1 second for new text to show
        page.wait_for_timeout(1000)
        # Pull all words from typing test section
        words = page.locator("#words").inner_text().split("\n")
        # For word in words type the word into the typing test field
        for word in words:
            page.type(selector="#words", text=f"{word} ")
        # Pull the words per minute outcome
        wpm = page.get_by_label('wpm').last.inner_text()
        # Return words per minute outcome
        return wpm

if __name__ == "__main__":
    result = type_away()
    print(f"\nYour computer can type:\n{result} WPM(Words Per Minute)")
