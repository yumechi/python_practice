from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


# 両方を並立させることもできる
@app.post("/files/")
async def create_file(
    file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...)
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }