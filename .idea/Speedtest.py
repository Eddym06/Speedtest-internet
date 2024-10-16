from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import speedtest

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html") as f:
        return HTMLResponse(content=f.read())


@app.get("/medir_velocidad")
async def medir_velocidad():
    test = speedtest.Speedtest()
    download_bps = test.download()
    upload_bps = test.upload()

    # Convertir de bits por segundo (bps) a megabytes por segundo (MBps)
    download_mbps = download_bps / (1024 * 1024) / 8
    upload_mbps = upload_bps / (1024 * 1024) / 8

    return {"download": download_mbps, "upload": upload_mbps}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
