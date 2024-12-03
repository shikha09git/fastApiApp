from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb+srv://user1:test7257@cluster1.rw8ni.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1")
db = client["student_db"]
students_collection = db["students"]
