from fastapi import FastAPI, Path, Query, Depends
from typing import Optional, List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

import models, schemas
import uvicorn
from database import local, engine
import utils
models.base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    try:
        db = local()
        yield db
    finally:
        db.close()



# inventory = {}


# @app.get('/get-item/{item_id}')  # Path Parameters
# def get_item(item_id:int = Path(None,
#                                 description = 'Id of the item you like to view',
#                                 gt = 0)):
#     return inventory[item_id]
# Path()To tell the user what the item_id is actually

# Query Parameters: Which is something comes after ? question mark with v.n = v


'''# @app.get('/get-by-name/{item_id}')  # Query Parameters
# def get_item(*, item_id: Optional[int], name: Optional[str]= None, test: Optional[int]):
    # item_id = path parameter
    # name = optional query parameter
    # test = mandatory query parameter
    # None Make Query parameter as optional'''


# @app.get('/get-by-name')
# def get_item(name: str = Query(None, title = 'Name',
#                                description = 'Name of the item') ):
#     for item_id in inventory:
#         if inventory[item_id].name == name:
#             return inventory[item_id]
#     return {'Data': 'Not Found'}

# Request Body & Post Method:


@app.post('/create-item')  # End Point
def create_item(item:schemas.Item,db:Session=Depends(get_db)):
    item_create = utils.create_data(db=db, item=item)
    return item_create

@app.get('/get-by-id')
def get_item(id:int, db:Session=Depends(get_db)):
    

# @app.put('/Update-item/{item_id}')  # End Point
# def update_item(item_id:int, item:UpdateItem):
#     if item_id not in inventory:
#         return {'Error': 'The Item does not exist'}
#
#     if item.name != None:
#         inventory[item_id].name = item.name
#
#     if item.price != None:
#         inventory[item_id].price = item.price
#
#     if item.brand != None:
#         inventory[item_id].brand = item.brand
#     return inventory[item_id]
#
# @app.delete('/delete-item/{item_id}')  # End Point
# def delete_item(item_id: int = Query(...,
#                                      description = 'Item to be delete', gt = 0)):
#     if item_id not in inventory:
#         return {'Error': 'ID does not exist.'}
#     del inventory[item_id]
#     return {'success':'item deleted'}
#
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
#     allow_credentials=True,
# )
#
# # Dependency
#
#
#
#
# @app.get("/")
# def main():
#     return RedirectResponse(url="/docs/")
#
#
# @app.get("/inventories/", response_model=List[schemas.Inventory])
# def show_inventories(db: Session = Depends(get_db)):
#     inventories = db.query(models.Inventory).all()
#     return inventories

#if __name__== "__main__":
    #uvicorn.run(app,port=5678)
