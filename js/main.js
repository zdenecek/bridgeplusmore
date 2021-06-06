'use strict';
require('dotenv').config();
const Database = require("./database.js");
const BM = require("./bm.js");


(async () => {
        console.log('The script is running...');
    
    
        const db = new Database('boards.sqlite');
        await db.open();
    
        const bm = new BM();
        await bm.open();
    
        await new Promise((resolve, reject) => {
            db.db.all("SELECT * FROM boards", [], (err, rows) => {
                rows.forEach(element => {
                    console.log(element);
                });
                resolve();
            });
        });

        const res = await bm.createNewBoard({name: "Testovací rozdání 1"});
        
        console.log(await res.json());

        await bm.close();
        await db.close();

})().then(() => {
    console.log('The script is concluded...');
    process.exit(0);
});

