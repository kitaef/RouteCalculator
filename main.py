from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from core.config import settings
from db.base import Base, Route
from db.session import engine, get_db
from schemas import models
from utils import calculate_optimal_route, fetch_coordinates, build_graph


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_app():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_app()


@app.get('/')
def home():
    return {"msg":"Welcome to Route Finder!"}

@app.post("/api/routes", response_model=models.Route)
def upload_route(csv_file: UploadFile = File(...), db: Base = Depends(get_db)):
    try:
        points = fetch_coordinates(csv_file.file)
        graph = build_graph(points)
        optimal_route = calculate_optimal_route(graph)
        route = Route(points=optimal_route)
        db.add(route)
        db.commit()
        db.flush()
        db.refresh(route)
        return route
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/routes/{id}", response_model=models.Route)
def get_route_by_id(id: int, db: Base = Depends(get_db)):
    route = db.query(Route).filter(Route.id == id).first()
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")
    return route