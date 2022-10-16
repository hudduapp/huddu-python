from huddu import ApiClient


_huddu_client = ApiClient(
    "<project_id>",
    "<stream_name>"
)


for i in range(0,5):
    try:
        a==b
    except Exception as e:
        _huddu_client.report(f"# Error occurred \n {e}")
        print("Successfully logged error!")
-