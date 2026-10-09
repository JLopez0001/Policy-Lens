import logging
import inngest

inngest_client = inngest.Inngest(
    app_id="Policy Lens",
    logger=logging.getLogger("uvicorn")
)