import uvicorn
from wsgiref import simple_server
from falcon_api.main import app as falcon_app
from fastapi_api.main import app as fastapi_app


def main(fast: bool = True):
    if fast:
        uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)
    else:
        httpd = simple_server.make_server('127.0.0.1', 8001, falcon_app)
        httpd.serve_forever()


if __name__ == '__main__':
    main(0)
