import os
import re
from playwright.sync_api import sync_playwright

HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"


def before_all(context):
    os.makedirs("evidencias", exist_ok=True)
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=HEADLESS)


def before_scenario(context, scenario):
    context.browser_context = context.browser.new_context()
    context.page = context.browser_context.new_page()


def after_step(context, step):
    if step.status == "failed":
        nome = re.sub(r"\W+", "_", step.name)
        context.page.screenshot(path=f"evidencias/falha_{nome}.png")


def after_scenario(context, scenario):
    context.browser_context.close()


def after_all(context):
    context.browser.close()
    context.playwright.stop()