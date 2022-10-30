# todo to run this example:
# pip install fastapi uvicorn
# run server: uvicorn integration_auth:app --reload
import os

from fastapi import FastAPI, Request

from huddu import IntegrationsClient

app = FastAPI()
hicl = IntegrationsClient("6992428770447761408")

secret = os.getenv("INTEGRATION_SECRET", "f40716787a5af765e115e85fb1ec3b0a")


@app.get("/auth")
async def authenticate(request: Request):
    code = request.query_params.get("code", None)

    if code:
        token_entry = hicl.Integrations.authorize(
            secret,
            code
        )
        print(token_entry)
        """
        Using the above token we can now access an account!
        """
        return "Successfully authenticated"
    else:
        return "Code query_param is required."
