from fastapi import FastAPI

app =FastAPI()

@app.get("/") #This is HTTP method GET with URL /
def read_root():
    return {"message": "Hello and Good morning!"}

@app.get("/users")
def get_users():
    return ["Ram", "Shyam", "Hanuman"]

@app.post("/users")
def create_user():
    return {"message": "User successfully created"}

@app.get("/")
def home():
    return {"message": "Home Page"}

@app.get("/about")
def about():
    return {"message": "About Page"}

@app.get("/projects")
def projects():
    return {"message": "Projects Page"}