const sqlite3 = require('sqlite3').verbose();
const util = require('util');

module.exports = class Database {

    constructor(file) {
        this.filename = file;
    }

    async open() {
        await new Promise((resolve, reject) => {
            this.db = new sqlite3.Database(this.filename, (err) => {
                if (err) {
                    console.error(err.message);
                    reject(err);
                }
                console.log('Connected to a SQlite database at ' + this.filename);
                resolve(this.db);
            });
        })
    }


    close() {
        console.log('Closing the database connection...');
        this.db.close();
    }

}
