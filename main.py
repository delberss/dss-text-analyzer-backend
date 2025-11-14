from fastapi import FastAPI

app = FastAPI(title="Text Analyzer API")

@app.get("/first")
def health():
    return {"status": "Funcionando"}
