Create env

```bash
    conda create -n wineq python=3.7 -y
```

Activate env

```bash
    conda activate wineq
```

Create requirements file

Install requirements
```bash
    pip install -r requirements.txt
```

Create template files:
    template.py file
        * data folder
            - processed
                - test_WineQT.csv file
                - train_WineQT.csv file
            - raw
                - WineQT.csv file
        - notebooks folder
        - report folder
            - scores.json file
            - params.json file
        - src folder
            - get_data.py file
            - load_data.py file
            - spit_data.py file
            - train_evaluate.py file
            __init__.py file
        - test folder
            - __init__.py file
            - conftest.py file
            - test_config.py file
        - data given folder
            - WineQT.csv file
        - save models folder
            - model.joblib file

create params.yaml & dvc.yaml files

Download Dataset

https://drive.google.com/drive/folders/1xw0XX-WK74uxtFFLySbtnX-ODdmdK5Ec

```bash
    git init
```

```bash
    dvc init
```

```bash
    dvc add data_given/WineQT.csv
```

```bash
    git add . && git commit -m "first commit"
```

create new repository in github for winequality

```bash
    git remote add origin https://github.com/joeltho26/Wine_Quality.git
```

```bash
    git branch -M main
```

```bash
    git push -u origin main
```
dvc commands:

```bash
    dvc repro
    dvc params show
    dvc metrics show
    dvc metrics diff
    dvc params diff
```


create tox.ini file

```bash
    tox
```

rebuilding
```bash
    tox -r
```
create test

pytest command
```bash
    pytest -v
```

create setup file

setup command
```bash
    pip install -e .
```

for sharing with people [build my own package]
```bash
    python setup.py sdist bdist_wheel
```