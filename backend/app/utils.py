from fastapi_pagination import Page
from fastapi import Query


Page = Page.with_custom_options(
    size=Query(10, ge=1, le=50),
) 

# common_parameters is a function that returns a dictionary with the parameters that are common to all endpoints
async def common_parameters(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}