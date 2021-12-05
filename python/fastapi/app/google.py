from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter(
    tags=["google-login"]
)


@router.get("/login", response_class=HTMLResponse)
async def login():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
