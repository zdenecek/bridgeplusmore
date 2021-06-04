require('dotenv').config();
const puppeteer = require('puppeteer');
const querystring = require('querystring');

console.log('The script is running...');

(async () => {
    const browser = await puppeteer.launch({ headless: false });

    await (async (browser) => {
        const page = await browser.newPage();

        await login(page);

        console.log('The script is concluded...');
    })(browser).finally(async () => {
        await browser.close();
    })

    process.exit(0);
})();


async function login(page) {
    console.log('logging in...');
    await page.goto('https://bridgeplusserver.com/');


    await page.type("#email", process.env.BM_EMAIL);
    await page.type("#pwd", process.env.BM_PASSWORD)

    await page.click("#terms");

    await Promise.all([
        page.keyboard.press('Enter'),
        page.waitForNavigation()
    ])
    await page.screenshot({ path: "screenshots/test.jpg" });
}

async function createNewBoard(page) {
    await page.setRequestInterception(true);

    page.once("request", interceptedRequest => {
        interceptedRequest.continue({
            method: "POST",
            postData: " ",
            headers: {
                ...interceptedRequest.headers(),
                "Content-Type": "application/x-www-form-urlencoded"
            }
        });
    });

    const response = await page.goto("https://postman-echo.com/post");

    console.log({
        url: response.url(),
        statusCode: response.status(),
        body: await response.text()
    });

}
