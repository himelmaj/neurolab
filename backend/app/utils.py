

# common_parameters is a function that returns a dictionary with the parameters that are common to all endpoints
async def common_parameters(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}