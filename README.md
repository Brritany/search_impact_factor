![PyPI - Version](https://img.shields.io/pypi/v/search-impact-factor)
![PyPI - License](https://img.shields.io/pypi/l/search-impact-factor)
![PyPI - Status](https://img.shields.io/pypi/status/search-impact-factor)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/search-impact-factor)
![PyPI - Download](https://img.shields.io/pypi/dm/search-impact-factor)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/search-impact-factor)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/search-impact-factor)
[![Downloads](https://static.pepy.tech/badge/search-impact-factor)](https://pepy.tech/project/search-impact-factor)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Brritany/search_impact_factor/Pylint)
[![Colab](https://img.shields.io/badge/Colab-Example-orange)](https://github.com/Brritany/search_impact_factor/blob/main/example.ipynb)

# Search Impact Factor

這個 Python 包提供了查詢 2023, 2022 年 Impact Factor 的功能

## Use Colab example code to realize search impact factor
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Brritany/search_impact_factor/blob/main/example.ipynb)

## Use `pip` to install package

```bash
pip install search-impact-factor
```

## Import package
```bash
from search_impact_factor import search_impact_factor as sif
```

## load_database: `default：2023`

```bash
sif.load_database(year="2023")
```

## query_database: 查詢數據庫。這個函數接受一個字典作為查詢條件，並返回1個或多個符合查詢結果的字典

```bash
query_dict = {"ISSN": "0007-9235"}
query_result = sif.query_database(query_dict)
```

## 使用 query_if_score: 查詢數據庫IF區間。這個函數接受兩個數字作為查詢條件，並返回一個DataFrame，包含兩數字之間的所有期刊

```bash
min_score = 150
max_score = 300
query_result_df = sif.query_if_score(min_score, max_score)

query_result_df.head()
```

### Update log

`0.0.11` Add GitHub link, re-do README.md

`0.0.1`  First edition
