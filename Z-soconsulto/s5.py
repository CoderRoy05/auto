from playwright.sync_api import sync_playwright
import random
import time

def generate_random_fingerprint():
    """
    Generates random browser fingerprint attributes.
    """
    # Random timezones and languages
    timezones = ["UTC", "America/New_York", "Europe/Paris", "Asia/Kolkata"]
    languages = ["en-US", "fr-FR", "es-ES", "hi-IN"]

    return {
        "timezone": random.choice(timezones),
        "language": random.choice(languages),
    }

def simulate_visitors_with_fingerprinting(number_of_visitors):
    """
    Simulate visitors with random fingerprints to mimic real user behavior.

    Args:
    - number_of_visitors: Number of visitors to simulate.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Define website pages
        pages = [
            'https://soconsulto.pages.dev/',
            'https://soconsulto.pages.dev/about/about',
            'https://soconsulto.pages.dev/blog/home',
            'https://soconsulto.pages.dev/c-u/contact_us',
            'https://soconsulto.pages.dev/Policy/Privacy_policy'
        ]

        # Define devices
        devices = [
            p.devices["iPhone 12"],
            p.devices["Galaxy S9+"],
            p.devices["iPad Pro 11"],
            p.devices["iPhone XR"],
            None,  # Default desktop device
        ]

        for i in range(number_of_visitors):
            try:
                # Generate random fingerprint
                fingerprint = generate_random_fingerprint()

                # Randomly select a device
                device = random.choice(devices)
                if device:
                    context = browser.new_context(**device)
                    device_name = device.get("name", "Unknown Device")
                else:
                    # Default desktop context
                    context = browser.new_context()

                # Override context properties for fingerprinting
                context.add_init_script(f"""
                    Object.defineProperty(navigator, 'language', {{get: () => '{fingerprint["language"]}'}});
                    Object.defineProperty(navigator, 'languages', {{get: () => ['{fingerprint["language"]}']}});
                    Intl.DateTimeFormat = (function(old) {{
                        return function(...args) {{
                            const format = old(...args);
                            Object.defineProperty(format, 'resolvedOptions', {{
                                value: () => ({{
                                    timeZone: '{fingerprint["timezone"]}',
                                    locale: '{fingerprint["language"]}',
                                    calendar: 'gregory',
                                    numberingSystem: 'latn',
                                    hourCycle: 'h12',
                                    hour12: true,
                                }})
                            }});
                            return format;
                        }};
                    }})(Intl.DateTimeFormat);
                """)

                # Open a new page
                page = context.new_page()

                # Navigate to random pages
                selected_pages = random.sample(pages, random.randint(1, len(pages)))
                for url in selected_pages:
                    page.goto(url)
                    time.sleep(random.uniform(2, 7))  # Mimic user delays

                # Close page and context
                page.close()
                context.close()
                print(f"Visitor {i + 1} simulated with fingerprint: {fingerprint} and device: {device_name}")

            except Exception as e:
                print(f"Error during simulation for visitor {i + 1}: {e}")

        browser.close()

# Simulate 20 visitors with random fingerprints
simulate_visitors_with_fingerprinting(20)



# shit from hacked dude abt upgrading fingerprint 