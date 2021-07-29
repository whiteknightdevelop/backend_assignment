// db = db.createCollection("currencies_db")()

db = db.getSiblingDB('currencies_db')
db.currencies_db.drop()

// db.currencies_db.insertMany([
//     {
//         "id": 1,
//         "name": "ddd1"
//     },
//     {
//         "id": 2,
//         "name": "ddd2"
//     },
//     {
//         "id": 3,
//         "name": "ddd3"
//     },
// ])