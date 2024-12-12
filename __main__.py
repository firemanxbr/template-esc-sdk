""" Python Pulumi program"""

import pulumi
import pulumi_esc_sdk as esc
import os

access_token = os.getenv("PULUMI_ACCESS_TOKEN")
if not access_token:
    raise ValueError("PULUMI_ACCESS_TOKEN environment variable must be set.")

config = esc.Configuration(access_token=access_token)
client = esc.EscClient(config)
org = pulumi.get_organization()

env, values, yaml = client.open_and_read_environment(
    org, "cloudflare", "cloudflare"
)
account_id = values["cloudflare"]["account_id"]
