import redis
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
jwt = JWTManager()

cache = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)