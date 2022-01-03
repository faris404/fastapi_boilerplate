from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from core.utils import templates
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/", response_class=HTMLResponse)
async def index(req: Request):
   logger.info('from user route')
   return templates.TemplateResponse('index.html',{'request':req})
