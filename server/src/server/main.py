from fastapi import FastAPI
import inngest
import inngest.fast_api
from server.jobs.client import inngest_client
from server.jobs.inngest_functions import injest_document

app = FastAPI(title="Policy Lens")

inngest.fast_api.serve(app, inngest_client, [injest_document])