import os

from bson.objectid import ObjectId
from pymongo import MongoClient

# client = MongoClient(os.getenv("MONGO_URI"))
# db = client[str(os.getenv("DB_NAME"))]

client = MongoClient("mongodb://mongo:27017/")
db = client['assignments']


class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    def save(self):
        db.users.insert_one(self.__dict__)

    @staticmethod
    def format_user(user):
        return {
            "id": str(user["_id"]),
            "name": user["username"],
            "role": user["role"],
        }

    @staticmethod
    def find_users():
        """Fecth all user"""
        return db.users.find()

    @staticmethod
    def get_user(id):
        """Fecth user deatils by ID"""
        return db.users.find_one({"_id": ObjectId(id)})

    @staticmethod
    def find_by_username(username):
        """Fecth user deatils by username"""
        return db.users.find_one({"username": username})

    @staticmethod
    def find_admins():
        """Fecth all the admins"""
        return db.users.find({"role": "admin"})

    @staticmethod
    def update_user(id, data):
        """Update user deatils by ID"""
        return db.users.update_one({"_id": ObjectId(id)}, {"$set": data})

    @staticmethod
    def delete_user(id):
        """Delete user by ID"""
        return db.users.delete_one({"_id": ObjectId(id)})


class Assignment:
    def __init__(self, user_id, task, admin):
        self.user_id = user_id
        self.task = task
        self.admin = admin
        self.status = "pending"  # default status

    def save(self):
        db.assignments.insert_one(self.__dict__)

    @staticmethod
    def find_by_admin(admin):
        """Fecth assigments assign to admin"""
        assignments = db.assignments.find({"admin": admin})
        return [Assignment.serialize(assignment) for assignment in assignments]

    @staticmethod
    def serialize(assignment):
        """Convert _id to string"""
        assignment["_id"] = str(assignment["_id"])
        return assignment

    @staticmethod
    def update_status(id, status):
        """Update the status of assignment"""
        db.assignments.update_one({"_id": ObjectId(id)}, {"$set": {"status": status}})
