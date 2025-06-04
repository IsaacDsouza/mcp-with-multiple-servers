from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI,tls=True, tlsAllowInvalidCertificates=True)
db = client["mydb"]  # Replace with your DB name
users_collection = db["users"]
