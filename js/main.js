'use strict';
require('dotenv').config();
const puppeteer = require('puppeteer');
const Database = require("./database.js");

console.log('The script is running...');

(async () => {

    const db = new Database('boards.sqlite');
    await db.open();
    db.close();
    return;
    const browser = await puppeteer.launch({ headless: process.env.HEADLESS });

    await (async (browser) => {
        const page = await browser.newPage();

        await login(page);

        await createNewBoard(page, "test88");

        
    })(browser).finally(async () => {
        await browser.close();
    })

})().finally(()=> {
    console.log('The script is concluded...');
    process.exit(0);
});


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
}

async function createNewBoard(page, name) {
    await page.setRequestInterception(true);

    const params = JSON.stringify({
        "COMMANDS": [
            {
                "COMMAND": "NewSingleDistribution",
                "Name": name,
            },
        ],
    });

    page.once("request", interceptedRequest => {

        interceptedRequest.continue({
            method: "POST",
            postData: params,
            headers: {
                ...interceptedRequest.headers(),
            }
        });
    });

    const response = await page.goto("https://bridgeplusserver.com/webapi.php?APIKEY=" + process.env.BM_APIKEY);

    return response;
}
