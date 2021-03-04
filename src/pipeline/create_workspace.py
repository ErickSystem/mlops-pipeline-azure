import click
from azureml.core import Workspace
from argparse import ArgumentParser
from azureml.core.authentication import AzureCliAuthentication


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "-n", "--name", type=str, help="Name of workspace",
)
@click.option(
    "-s", "--subscription_id", type=str, help="Subscription that user it is logged",
)
@click.option(
    "-r", "--resource_group", type=str, help="Resource Group required to organize the resources on Azure",
)
@click.option(
    "-l", "--location", type=str, default="eastus2", help="Location hosted all resources", show_default=True,
)
def main(name: str, subscription_id: str, resource_group: str, location: str):
    """Create Workspace on Azure ML Service

        - https://docs.microsoft.com/pt-br/azure/machine-learning
        /how-to-manage-workspace?tab=python&tabs=python#create-multi-tenant
    """
    print(location)
    click.secho("[ML SERVICE] - Creating Workspace...", fg="green")

    cli_auth = AzureCliAuthentication()
    ws = Workspace.create(
        name=name,
        subscription_id=subscription_id,
        resource_group=resource_group,
        create_resource_group=True,
        location=location,
        auth=cli_auth,
    )

    ws.write_config(".azureml")
    print(
        "\tWorkspace name: " + ws.name,
        "Azure region: " + ws.location,
        "Subscription id: " + ws.subscription_id,
        "Resource group: " + ws.resource_group,
        sep="\n\t",
    )
