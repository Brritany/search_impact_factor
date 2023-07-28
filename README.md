# Search Impact Factor

這個 Python 包提供了查詢 2023 年 Impact Factor 的功能

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

`0.0.1` first edition
