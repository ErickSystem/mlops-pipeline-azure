import click
import os
from functools import wraps

from azureml.core import Workspace
from azureml.core.authentication import AzureCliAuthentication
from azureml.exceptions import WorkspaceException


def workspace_required(f):
    """ Connection with Workspace Azureml """

    @wraps(f)
    def workspace(*args, **kwargs):
        ws = None
        try:
            click.secho("[ML SERVICE] - Connection with workspace...", fg="green")
            cli_auth = AzureCliAuthentication()
            ws = Workspace.from_config(path=os.path.join(".azureml", "config.json"), auth=cli_auth)
            print(
                "\tWorkspace name: " + ws.name,
                "Azure region: " + ws.location,
                "Subscription id: " + ws.subscription_id,
                "Resource group: " + ws.resource_group,
                sep="\n\t",
            )
        except WorkspaceException:
            raise WorkspaceException("Failed connection with workspace")
        return f(*args, **kwargs, ws=ws)

    return workspace
