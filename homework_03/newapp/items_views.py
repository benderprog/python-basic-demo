from fastapi import APIRouter



router = APIRouter(
    # prefix="/items",
    tags=["Items"]
)

@router.get("/items/")
def get_items():
    return {
        "data": [
            {id: 123, "name": "abc"},
            {id: 234, "name": "qwe"},
        ]
    }

@router.get("/items/{item_id}/")
def get_item(item_id: int):
    return {
        "data": {
            "id": item_id,
            "name": f"abc-{item_id}",
        }
    }



@router.post("/")
def create_item(data: dict):
    return {"data": data}