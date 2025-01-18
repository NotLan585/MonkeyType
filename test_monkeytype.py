
from playwright.sync_api import sync_playwright

def type_away() -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://monkeytype.com/")
        page.wait_for_load_state("domcontentloaded")
        page.get_by_role("button", name="accept all").wait_for(state="visible")
        page.get_by_role("button", name="accept all").click()
        page.get_by_role("button", name="accept all").wait_for(state="hidden")
        page.locator("button[mode='words']").click()
        page.wait_for_timeout(1000)
        words = page.locator("#words").inner_text().split("\n")
        for word in words:
            page.type(selector="#words", text=f"{word} ")
        wpm = page.get_by_label('wpm').last.inner_text()
        return wpm

if __name__ == "__main__":
    result = type_away()
    print(f"\nYour computer can type:\n{result} WPM(Words Per Minute)")
