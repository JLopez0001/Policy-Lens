import inngest
from server.jobs.client import inngest_client

@inngest_client.create_function(
    fn_id="Innjest Document",
    trigger=inngest.TriggerEvent(event="policy/document"),
)

async def injest_document(ctx: inngest.Context):
    return {"inngest":"pdf"}

functions = [injest_document]