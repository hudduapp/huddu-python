import uuid

from huddu import ApiClient

client = ApiClient("<integration_auth_token>")

project_id = "6979386863354290176"  # todo: replace as needed
stream_id = "6987388048929628160"  # todo: replace as needed
account_id = "6966809249058037760"  # todo: replace as needed
event_id = "6987851870576484352"  # todo: replace as needed
installation_id = "6987366675922460672"  # todo: replace as needed

# ACCOUNTS
# list installations
print(client.Accounts.list_installations())

# get account
print(client.Accounts.get(account_id))

# PROJECTS
# list projects
print(client.Projects.list(account_id))

# get project
print(client.Projects.get(project_id, account=account_id))

# STREAMS

# list streams
print(client.Streams.list(account=account_id, project=project_id))

# get stream
print(client.Streams.get(stream_id, account=account_id, project=project_id))

# create stream
print(client.Streams.create(project=project_id, account=account_id, name="new_stream"))

# list versions
print(
    client.Streams.list_versions(
        stream_id,
        account=account_id,
        project=project_id,
    )
)

# create stream version
print(
    client.Streams.create_version(
        stream_id,
        account=account_id,
        project=project_id,
        version=str(uuid.uuid4()),
    )
)

# EVENTS


# list events
print(client.Events.list(account=account_id, project=project_id, stream=stream_id))

# get event
print(
    client.Events.get(
        event_id, account=account_id, project=project_id, stream=stream_id
    )
)

# search events
print(
    client.Events.search(
        project=project_id,
        account=account_id,
        stream=stream_id,
        query={"data.example": {"$regex": "string "}},
    )
)

# create event
print(
    client.Events.create(
        account=account_id,
        project=project_id,
        stream=stream_id,
        data={"data": "[err] on line 100"},
    )
)

# batch create event
print(
    client.Events.create(
        account=account_id,
        project=project_id,
        stream=stream_id,
        batch=[{"data": "[err] on line 100"}, {"data": "[err] on line 100"}],
    )
)

# INSTALLATIONS

# list all installs
print(client.Installations.list())

# get a specific install
print(client.Installations.get(installation_id))

# update an install
print(client.Installations.update(installation_id, meta={
    "discord_webhooks_url": "https://discord.com"
}))
