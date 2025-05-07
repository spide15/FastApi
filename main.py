from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_available: bool = True

#Dummy
items = {
  "2": {
    "name": "Pen",
    "price": 9.99,
    "is_available": True},
  "3": {
    "name": "Pencil",
    "price": 5,
    "is_available": True
  },
  "4": {
    "name": "Eraser",
    "price": 2.5,
    "is_available": True
  },
  "5": {
    "name": "Ruler",
    "price": 15.75,
    "is_available": True
  },
  "6": {
    "name": "Marker",
    "price": 25,
    "is_available": True
  },
  "7": {
    "name": "Glue Stick",
    "price": 30,
    "is_available": True
  },
  "8": {
    "name": "Fevi Stick",
    "price": 30,
    "is_available": True
  }
}
items_keys=list(items.keys())
# items_keys=int(items.keys())
items_keys.sort()


current_id=items_keys[-1]
new_id=int(current_id)+1
# Get
@app.post("/items")
def create_item( item: Item):

    if new_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[new_id] = item
    return {"message": "Item created successfully", "item": item}

# Get all items
@app.get("/items/")
def read_all_items():
    return items

# Get by id
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]



# Update an existing item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"message": "Item updated successfully", "item": item}

# Delete
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted successfully"}
