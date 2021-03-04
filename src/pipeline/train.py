import click
from azureml.core import Workspace
from azureml.core.authentication import AzureCliAuthentication

# core
from src.pipeline.mlops.ml_workspace import workspace_required


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "-e",
    "--experiment",
    type=str,
    default=None,
    help="Experiment generated on Azure ML Service",
    show_default=True,
)
@click.option(
    "--epochs",
    type=str,
    default=None,
    help="number of epochs to train the model for",
    show_default=True,
)
@click.option(
    "--dataset-version",
    type=str,
    default=None,
    help="Specify version of the dataset.csv (dataset cloud)",
    show_default=True,
)
@click.option(
    "--cluster-cores",
    type=str,
    default=None,
    help="Total nodes will be the Cluster",
    show_default=True,
)
@workspace_required
def main(
    experiment: str, epochs: int, dataset_version: int, cluster_cores: int, ws=None
):
    """Run experiment 

        Resources used:

        - https://docs.microsoft.com/en-us/python/api/azureml-core
        /azureml.core.runconfig.runconfiguration?view=azure-ml-py

        - https://docs.microsoft.com/pt-br/python/api/azureml-core
        /azureml.core.compute.computetarget?view=azure-ml-py

        - https://docs.microsoft.com/en-us/python/api/azureml-core
        /azureml.core.compute.amlcompute(class)?view=azure-ml-py
    """

    click.secho("[ML SERVICE] - Running Train", fg="green")
