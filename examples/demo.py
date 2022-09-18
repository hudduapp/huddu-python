from huddu import ApiClient


_huddu_client = ApiClient(
    "<project_id>",
    "<stream_name>"
)


while True:
    # something happened
    try:
        a==b
    except Exception as e:
        _huddu_client.report("errors", {
            "markdown": f"# Error occurred \n {e}"
        })
        print("Successfully logged error!")
