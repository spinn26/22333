import asyncio
import time
from pyppeteer import launch

def req(request):
    if request.url.startswith('https://auth.stealth') > -1:
        print(f"  URL: {request.url}")
        print(f"  {dir(request)}")

async def scraper():
    browser =await launch({"headless": False, })
    page = await browser.newPage()
    response = await page.goto('https://auth.stealthseminarapp.com/op/auth?client_id=f1a99865-da55-4bce-8ab4-5eabcab3f408&response_type=code%20id_token%20token&scope=openid%20email&redirect_uri=https://stealthseminarapp.com&nonce=7dc95397-b4c1-4340-9668-e59cf58b1ecc')
    
    # Set up the event listener for 'request'
    page.on('request', req)
    
    await page.type('input[name="login"]', 'admin@edu-maestros.com')
    await page.type('input[name="password"]', 'giNENtofe$')
    await page.click('button[type=submit]')
    await page.waitForNavigation()
    time.sleep(1000)
    await page.close()
    await browser.close()

asyncio.run(scraper())