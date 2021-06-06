const puppeteer = require('puppeteer');

module.exports = class BM {

    async open() {
        console.log('Opening B+M...');
        this.browser = await puppeteer.launch({ headless: process.env.HEADLESS === "TRUE"  });
        this.page = await this.browser.newPage();
        await this.login();
    }

    async close()
    {
        console.log('Closing B+M...');
        await this.browser.close();
    }


    async login() {

        const page = this.page;

        console.log('logging in to B+M...');
        await page.goto('https://bridgeplusserver.com/');

        await page.type("#email", process.env.BM_EMAIL);
        await page.type("#pwd", process.env.BM_PASSWORD)

        await page.click("#terms");

        await Promise.all([
            page.keyboard.press('Enter'),
            page.waitForNavigation(),
        ])
    }


    async createNewBoard({name}) {

        const page = this.page;
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

        await page.setRequestInterception(false);


        return response;
    }

}
