"""
LinkedIn Auto-Apply Bot v2
===========================
- Searches directly on LinkedIn for Easy Apply jobs
- No scraped URLs needed
- Auto-applies to matching jobs
"""

import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# ── CONFIG ────────────────────────────────────────────────────
LINKEDIN_EMAIL = "kollivibhash@gmail.com"

SEARCH_QUERIES = [
    "Full Stack Developer",
    "Python Developer",
    "React Developer",
    "Data Analyst",
    "Software Engineer",
]

LOCATIONS = ["Hyderabad", "Bengaluru", "Remote"]

DEFAULT_ANSWERS = {
    "phone":            "7893279576",
    "first_name":       "Vibash",
    "last_name":        "Kolli",
    "city":             "Hyderabad",
    "notice_period":    "Immediate",
    "current_salary":   "0",
    "expected_salary":  "0",
    "years_experience": "0",
}

MAX_JOBS_PER_SEARCH = 10  # How many jobs to apply per search


# ── SETUP ─────────────────────────────────────────────────────
def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver


# ── LOGIN ─────────────────────────────────────────────────────
def login(driver, email, password):
    print("\n🔐 Logging into LinkedIn...")
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    driver.execute_script("document.cookie = 'lang=v=2&lang=en-us; path=/; domain=.linkedin.com'")
    driver.refresh()
    time.sleep(3)
    try:
        driver.find_element(By.ID, "username").send_keys(email)
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        time.sleep(5)

        if "feed" in driver.current_url or "mynetwork" in driver.current_url:
            print("✅ Logged in!")
            return True
        elif "checkpoint" in driver.current_url or "challenge" in driver.current_url:
            print("⚠️  LinkedIn wants verification!")
            print("Complete it in the browser then press Enter...")
            input()
            return True
        else:
            print("Complete login in browser if needed, then press Enter...")
            input()
            return True
    except Exception as e:
        print(f"Login error: {e}")
        return False


# ── FILL FORM ─────────────────────────────────────────────────
def fill_form(driver):
    try:
        inputs = driver.find_elements(By.CSS_SELECTOR,
            "input[type='text'], input[type='number'], input[type='tel'], textarea")
        for inp in inputs:
            try:
                if not inp.is_displayed():
                    continue
                val = inp.get_attribute("value") or ""
                if val.strip():
                    continue
                lid = inp.get_attribute("id") or ""
                label = ""
                try:
                    els = driver.find_elements(By.CSS_SELECTOR, f"label[for='{lid}']")
                    if els:
                        label = els[0].text.lower()
                except:
                    pass
                ph = (inp.get_attribute("placeholder") or "").lower()
                txt = label + " " + ph

                if any(w in txt for w in ["phone","mobile"]):
                    inp.clear(); inp.send_keys(DEFAULT_ANSWERS["phone"])
                elif "first" in txt:
                    inp.clear(); inp.send_keys(DEFAULT_ANSWERS["first_name"])
                elif "last" in txt:
                    inp.clear(); inp.send_keys(DEFAULT_ANSWERS["last_name"])
                elif any(w in txt for w in ["city","location"]):
                    inp.clear(); inp.send_keys(DEFAULT_ANSWERS["city"])
                elif any(w in txt for w in ["notice","availab","joining"]):
                    inp.clear(); inp.send_keys(DEFAULT_ANSWERS["notice_period"])
                elif any(w in txt for w in ["current salary","current ctc"]):
                    inp.clear(); inp.send_keys(DEFAULT_ANSWERS["current_salary"])
                elif any(w in txt for w in ["expected","desired"]):
                    inp.clear(); inp.send_keys(DEFAULT_ANSWERS["expected_salary"])
                elif any(w in txt for w in ["year","experience"]):
                    inp.clear(); inp.send_keys(DEFAULT_ANSWERS["years_experience"])
            except:
                pass

        # Handle dropdowns
        from selenium.webdriver.support.ui import Select
        for sel in driver.find_elements(By.TAG_NAME, "select"):
            try:
                s = Select(sel)
                opts = [o.text for o in s.options]
                if any("immediate" in o.lower() for o in opts):
                    s.select_by_visible_text(next(o for o in opts if "immediate" in o.lower()))
                elif any("yes" in o.lower() for o in opts):
                    s.select_by_visible_text(next(o for o in opts if "yes" in o.lower()))
                elif len(opts) > 1:
                    s.select_by_index(1)
            except:
                pass
    except:
        pass


# ── APPLY TO JOB ──────────────────────────────────────────────
def apply_to_job(driver, job_card):
    try:
        # Click the job card
        job_card.click()
        time.sleep(3)

        # Find Easy Apply button in right panel
        easy_apply = None
        try:
            easy_apply = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,
                    ".jobs-apply-button--top-card, .jobs-s-apply button"))
            )
        except:
            pass

        if not easy_apply:
            buttons = driver.find_elements(By.TAG_NAME, "button")
            for btn in buttons:
                try:
                    if "easy apply" in btn.text.lower() and btn.is_displayed():
                        easy_apply = btn
                        break
                except:
                    pass

        if not easy_apply:
            return False

        # Get job title for display
        try:
            title = driver.find_element(By.CSS_SELECTOR, ".job-details-jobs-unified-top-card__job-title, h1").text
            company = driver.find_element(By.CSS_SELECTOR, ".job-details-jobs-unified-top-card__company-name, .topcard__org-name-link").text
            print(f"  📝 Applying: {title} @ {company}")
        except:
            print(f"  📝 Applying to job...")

        easy_apply.click()
        time.sleep(3)

        # Go through application pages
        for page in range(15):
            time.sleep(2)
            fill_form(driver)
            time.sleep(1)

            # Submit
            try:
                submit = driver.find_element(By.CSS_SELECTOR,
                    "button[aria-label*='Submit'], button[aria-label*='submit']")
                if submit.is_displayed():
                    submit.click()
                    time.sleep(2)
                    # Close confirmation
                    try:
                        driver.find_element(By.CSS_SELECTOR,
                            "button[aria-label*='Dismiss'], button[aria-label*='dismiss']").click()
                    except:
                        pass
                    print("  ✅ Applied!")
                    return True
            except:
                pass

            # Next page
            clicked = False
            for label in ["Continue to next step", "Next", "Review your application", "Review"]:
                try:
                    btn = driver.find_element(By.CSS_SELECTOR, f"button[aria-label*='{label}']")
                    if btn.is_displayed():
                        btn.click()
                        clicked = True
                        break
                except:
                    pass
            if not clicked:
                # Try any primary button
                try:
                    btns = driver.find_elements(By.CSS_SELECTOR, "button.artdeco-button--primary")
                    for btn in btns:
                        if btn.is_displayed() and "submit" not in btn.text.lower():
                            btn.click()
                            clicked = True
                            break
                except:
                    pass
            if not clicked:
                break

        # Close modal if stuck
        try:
            driver.find_element(By.CSS_SELECTOR,
                "button[aria-label='Dismiss'], button[aria-label='dismiss']").click()
            time.sleep(1)
            try:
                driver.find_element(By.CSS_SELECTOR,
                    "button[data-control-name='discard_application_confirm_btn']").click()
            except:
                pass
        except:
            pass
        return False

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


# ── SEARCH & APPLY ────────────────────────────────────────────
def search_and_apply(driver, query, location, max_jobs=10):
    print(f"\n🔍 Searching: '{query}' in '{location}'")

    # Build LinkedIn Easy Apply search URL
    query_encoded = query.replace(" ", "%20")
    location_encoded = location.replace(" ", "%20")
    url = f"https://www.linkedin.com/jobs/search/?keywords={query_encoded}&location={location_encoded}&f_AL=true&f_E=1%2C2&sortBy=DD"

    driver.get(url)
    time.sleep(4)

    applied = 0
    skipped = 0

    # Get job cards
    for attempt in range(3):
        try:
            job_cards = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                    ".job-card-container, .jobs-search-results__list-item"))
            )
            break
        except:
            time.sleep(3)
            job_cards = []

    if not job_cards:
        print("  No jobs found for this search")
        return 0, 0

    print(f"  Found {len(job_cards)} jobs — applying to up to {max_jobs}...")

    for i, card in enumerate(job_cards[:max_jobs]):
        try:
            driver.execute_script("arguments[0].scrollIntoView();", card)
            time.sleep(1)
            result = apply_to_job(driver, card)
            if result:
                applied += 1
            else:
                skipped += 1
            time.sleep(2)
        except Exception as e:
            skipped += 1
            continue

    return applied, skipped


# ── MAIN ──────────────────────────────────────────────────────
def main():
    print("=" * 55)
    print("  🤖 LinkedIn Auto-Apply Bot v2")
    print("  Vibash Kolli | Hyderabad")
    print("=" * 55)
    print("\nThis bot will:")
    print("  • Search LinkedIn directly for Easy Apply jobs")
    print("  • Auto-apply to matching jobs")
    print(f"  • Searches: {len(SEARCH_QUERIES) * len(LOCATIONS)} combinations")
    print(f"  • Max {MAX_JOBS_PER_SEARCH} applications per search")

    print(f"\nEnter your LinkedIn password (won't show on screen):")
    password = getpass.getpass("Password: ")

    print("\n🌐 Opening Chrome...")
    try:
        driver = setup_driver()
    except Exception as e:
        print(f"❌ Chrome error: {e}")
        return

    if not login(driver, LINKEDIN_EMAIL, password):
        driver.quit()
        return

    total_applied = 0
    total_skipped = 0

    for query in SEARCH_QUERIES:
        for location in LOCATIONS:
            applied, skipped = search_and_apply(driver, query, location, MAX_JOBS_PER_SEARCH)
            total_applied += applied
            total_skipped += skipped
            time.sleep(3)

    print("\n" + "=" * 55)
    print("  📊 FINAL SUMMARY")
    print("=" * 55)
    print(f"  ✅ Successfully Applied : {total_applied}")
    print(f"  ⏭️  Skipped              : {total_skipped}")
    print("=" * 55)

    input("\nPress Enter to close browser...")
    driver.quit()


if __name__ == "__main__":
    main()
