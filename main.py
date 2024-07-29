from fastapi import FastAPI

app = FastAPI(
    title="Start to learn:)"
)

@app.get("/")
def hello():
    return 'Hellow world!'