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

Create template file

Download Dataset

https://drive.google.com/drive/folders/1xw0XX-WK74uxtFFLySbtnX-ODdmdK5Ec

git init

dvc init

dvc add data_given/WineQT.csv

git add . && git commit -m "first commit"

create new repository in github for winequality

git remote add origin https://github.com/joeltho26/Wine_Quality.git

git branch -M main

git push -u origin main