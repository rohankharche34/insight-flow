from fastapi import FastAPI

app = FastAPI(
        title="InsightFlow API",
        version="0.1.0",
)

@app.get("/")
def root():
    return {
            "message": "InsightFlow backend running"
    }
