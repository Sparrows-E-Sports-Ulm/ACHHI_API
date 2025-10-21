from fastapi.routing import APIRouter


route = APIRouter()

@route.get("/health")
def health_endpoint():
    return {"status": "healthy"}