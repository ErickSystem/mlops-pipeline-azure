# MLOPS PIPELINE AT AZURE ML SERVICE

Building a Pipeline of Machine Learning

## Created using Conda Env

- **Prerequisites**

    >[Install the conda Ubuntu 18.04 version to python 3.7](https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh)

    >[Install the conda Windows version to python 3.7](https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe)

    >[Install the conda MacOS version to python 3.7](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)


```bash
# reset environment conda, case it has already in your machine (OPTIONAL)
conda deactivate
conda remove -n mlops-pipeline-azure --all

# creating 
conda env create -f conda_dependencies.yml
conda activate mlops-pipeline-azure
```

## Using conda env with jupyter

```bash
ipython kernel install --user --name mlops-pipeline-azure --display-name "Python (mlops-pipeline-azure)"

# initialize jupyter
jupyter notebook --notebook-dir notebooks
```

## Run

### Create Workspace

```bash
create-workspace -n <workspace_name> -s <subscription_id> -r <resource_group> -l <location>
```

### Train Model

```bash
train -e tensorflow-nlp --epochs 20 --dataset-version 1 --cluster-cores 8
```