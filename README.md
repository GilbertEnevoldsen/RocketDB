# RocketDB

RocketDB is a work-in-progress database manager that supports both remote and local databases.

# Goal

The goal is to build a python based database manager, with both an api and a tool. To allow for both local and remote databases.
RocketDB will also have a web-gui for managing your databases in an easy and manageable way.
Databases build with RocketDB will be scaleable, secure and with opportunity to switch between web and local storage anytime.

# Example code

```
import rocketdb

db = rocketdb.Database()

db.create_subbase(id="Shop")
db.create_table(id="Orders", fields=["customer", "item", "quantity"], location="Shop")

orders = [
    {"customer": "Sean Burton", "item": "Jeans", "quantity": 1},
    {"customer": "Lewis Carson", "item": "Shirt", "quantity": 3},
    {"customer": "Sean Burton", "item": "Socks", "quantity": 2},
    {"customer": "George Wilson", "item": "Suit", "quantity": 1}
]

for order in orders:
    db.insert(record=order, location="Shop/Orders")

for record in db.get_where(match={"customer": "Sean Burton"}, location="Shop/Orders"):
    print(record["quantity"])

db.write_where(match={"customer": "Lewis Carson", "item": "Shirt"}, data={"quantity": 2}, location="Shop/Orders")
```