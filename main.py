import dlt
from dlt.sources.helpers import requests
from dlt.sources.helpers.rest_client.client import RESTClient
from dlt.sources.helpers.rest_client.paginators import JSONResponseCursorPaginator

stealth_seminar_client = RESTClient(
    base_url="https://api.stealthseminarapp.com",
    paginator=JSONResponseCursorPaginator(
        cursor_path="after_key.email",
        cursor_param="after"
    )    
)

@dlt.resource(write_disposition="merge", primary_key="email")
def get_webinar_stats():
    data = []
    response = stealth_seminar_client.paginate(
        "/stats/77433d93-8856-4453-8599-996185afa623/registered-emails",
        method="GET",
        headers={
            "authorization": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNpZy1ycy0wIn0.eyJzdWIiOiI2OTdmMzFiMC1lMmM5LTQyZDMtOTRmYS03ZDhmYTE3MjM3NjIiLCJlbWFpbCI6ImFkbWluQGVkdS1tYWVzdHJvcy5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibm9uY2UiOiI3ZGM5NTM5Ny1iNGMxLTQzNDAtOTY2OC1lNTljZjU4YjFlY2MiLCJhdF9oYXNoIjoiMS0yUm01MnMtWjdIWU13SkRseEgwdyIsImNfaGFzaCI6IjdFNV9CQ1cwSERPbEFkanZMZ3R6bUEiLCJhdWQiOiJmMWE5OTg2NS1kYTU1LTRiY2UtOGFiNC01ZWFiY2FiM2Y0MDgiLCJleHAiOjE3NTg1NTgxMDAsImlhdCI6MTc1ODU1NDUwMCwiaXNzIjoiaHR0cHM6Ly9hdXRoLnN0ZWFsdGhzZW1pbmFyYXBwLmNvbSJ9.YI71aWz3W3xmMNyMzsFQ24QMOIScMGy9visUPvlgouK1S0ZF9elrMi8m1dfCEBTUHkPMgvhjs6GvaJ7_lKy2z4R_ggCWnRjWaDf50p-crgI0PxuV6oQKnOdpsEQcSWRPLDaot03iEEgwbvwHcW5gBo6beKU3lbnzi-ds5CKSj4s9Pi-CidXx1yypKAHUvrgJ3ATFMspi6v-rbLXOfEJlNkKQBDc96yDL2qo1R8SGdQwh06IuYyVpbVjK57XXgsNeLfK1HjoZbfuZYW2_6EgRT8BWQ3Pxdvb7oCIVMD_u1D0bLbCc8rBVT6lr7MvurATFB4VQCtH6-oGLQtJG-LNYTw",
        },
        params={
            "emailFilter": "registered",
            "filter": "date",
            "start_date": "2025-09-21",
        },
    )
    for page in response:
        print(dir(page))
        data.append(page)
        yield page

pipeline = dlt.pipeline(
    pipeline_name="webinar_stats",
    destination="postgres",
    dataset_name="data",
)

# Run the pipeline
load_info = pipeline.run(get_webinar_stats(), table_name="webinar_stats")
print(load_info)