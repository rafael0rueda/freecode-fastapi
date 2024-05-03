from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest
from app.main import app
from app import schemas
from app.config import settings
from app.database import get_db, Base
from app.main import app


SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    # Drop all the tables before running test
    Base.metadata.drop_all(bind=engine)
    # Create all the talbes before running test
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)


def test_root(client):
    res = client.get("/")
    print(res.json().get("messsage"))
    assert res.json().get("message") == "Welcome to my API!!"


def test_create_user(client):
    res = client.post("/users/", json={"email": "hola@gmail.com", "password": "pas123"})
    new_user = schemas.UserOut(**res.json())
    print(res.json())
    assert new_user.email == "hola@gmail.com"
    assert res.status_code == 201
