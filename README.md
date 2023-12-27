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
