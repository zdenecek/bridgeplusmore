
async function login(browser) {
    console.log('logging in...');
    return 5;
}

console.log('The script is running...');

const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({headless: false});
    
    await (async (browser) => {
        const page = await browser.newPage();

        await page.screenshot({path: "screenshots/test.jpg"});
        await login(browser);

        console.log('The script is concluded...');
    })(browser).finally(async () => {
        await browser.close();
    })

    process.exit(0);
})();

