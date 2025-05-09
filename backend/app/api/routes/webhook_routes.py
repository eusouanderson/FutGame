from fastapi import APIRouter, BackgroundTasks, Request, Response

from backend.app.api.webhook.deploy import run_deploy

router = APIRouter()


@router.post("/webhook")
async def webhook(request: Request, background_tasks: BackgroundTasks):

    print("✅ Webhook recebido. Iniciando atualização...")

    background_tasks.add_task(run_deploy)

    return Response(content="Deploy agendado", status_code=202)
