import os

from databricks.sdk import AccountClient

a = AccountClient()

workspace_id = os.environ["TEST_WORKSPACE_ID"]

all = a.workspace_assignment.list(workspace_id=workspace_id)
