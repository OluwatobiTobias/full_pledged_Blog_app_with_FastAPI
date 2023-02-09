
def start_application():
    import uvicorn
    from sys import argv

    port if len(port := argv) > 1 else (port := (0, 8000))
    uvicorn.run("server.app:app", host="0.0.0.0", port=int(port[1]), reload=True)
