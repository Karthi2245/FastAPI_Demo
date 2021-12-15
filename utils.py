from sqlalchemy.orm import Session
import models

import schemas



def create_data(db:Session,item:schemas.Item):
    data = models.Inventory(name = item.name, price = item.price, brand = item.brand)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data