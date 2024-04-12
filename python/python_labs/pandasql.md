## pandasql

故事开始于一个叫做恬宝的小熊猫，她生活在一个美丽的熊猫家族中。尽管恬宝是一个可爱而调皮的小熊猫，但她总是渴望探索新的事物和技能。有一天，当她在家族图书馆里翻阅书籍时，她发现了一本关于数据处理和分析的书籍。

她了解到pandasql 是一个 Python 库，它允许你使用 SQL 语法来查询 Pandas DataFrame。这个库将 Pandas 和 SQL 结合起来，让你可以使用熟悉的 SQL 语法来操作 DataFrame，从而简化数据分析和处理的过程。

### 主要的优势
- SQL 语法：pandasql 允许你直接在 Python 中使用 SQL 语法来查询 DataFrame，包括 SELECT、JOIN、WHERE 等常见的 SQL 关键字。
- 无需转换：使用 pandasql，你无需将 DataFrame 转换成 SQL 数据库或执行任何额外的设置。它直接在内存中运行，处理速度快，使用方便。
- 灵活性：你可以在查询中使用 Python 变量和函数，这使得 pandasql 非常灵活，能够处理各种复杂的数据操作和分析任务。
- 与 Pandas 无缝集成：pandasql 与 Pandas 完美集成，你可以轻松地在 Pandas 数据处理流程中嵌入 SQL 查询，无需切换环境或学习新的工具。
- 适用于小型数据集：由于 pandasql 是在内存中运行的，它更适合处理小型数据集。对于大型数据集，建议使用专门的数据库系统。

使用 pandasql 可以简化数据分析和处理的过程，特别是对于熟悉 SQL 语法的用户来说，它提供了一种更直观的方式来操作 DataFrame。


### 安装

应用pip 进行安装：
```shell
pip install -U pandasql
```

是否需要添加`-U`取决于对应的执行环境是否需要用户授权。

### 实践

`pandasql`的核心是`sqldf`，可以将执行环境的locals()和globals()内存中的DataFrame进行注册。


```python
from pandasql import sqldf
from pandasql import load_meat, load_births
import pandas as pd

pysqldf = lambda q: sqldf(q, globals())
```

### 基本的操作


```python
# 创建一个示例 DataFrame

data = {
    'name': ['alice', 'bob', 'lugq'],
    'age': [25, 30, 32]
}
df = pd.DataFrame(data)
df.head()
```


### Dataframe注册

核心是`sqldf()` 这个函数，用于执行 SQL 查询并返回结果。它的核心作用是将 SQL 查询语句应用于 Pandas DataFrame，并返回符合查询条件的结果集。

接受两个参数：
- query 参数是一个包含 SQL 查询语句的字符串，它描述了你想要对 DataFrame 进行的操作，比如选择、过滤、聚合等。
- globals() 函数返回一个全局变量字典，其中包含了当前的全局变量。在这个上下文中，它用于指定数据源，告诉 pandasql 在哪个环境中执行 SQL 查询。

### SQL查询


```python
# 基本查询
query_df = pysqldf("select * from df")

print(query_df)
```

        name  age
    0  alice   25
    1    bob   30
    2   lugq   32



```python
# 筛选
query = "SELECT * FROM df WHERE Age > 28"
filter_df = pysqldf(query)

print(filter_df)
```

       name  age
    0   bob   30
    1  lugq   32



```python
# 使用聚合函数计算统计信息
query = "SELECT AVG(Age) AS AvgAge FROM df"
result = sqldf(query, globals())
print(result)
```

       AvgAge
    0    29.0



```python
# 组合多个操作
query = """
    SELECT name,age
    FROM df
    WHERE age > 25
    ORDER BY age DESC
"""
result = sqldf(query, globals())
print(result)
```

       name  age
    0  lugq   32
    1   bob   30


### 基于数据集的操作


```python
# Load sample dataset
meat = load_meat()
birth = load_births()

# get type of the dataset, it's just a `pandas.core.frame.DataFrame`, normal DF
print(type(meat))
```

    <class 'pandas.core.frame.DataFrame'>



```python
# try to use sql to query the df
meat_res = pysqldf("select * from meat limit 10")

# then just get the normal result
print(meat_res.head())

print("Get sql result type: ", type(meat_res))
```

                             date   beef   veal  ...  broilers  other_chicken turkey
    0  1944-01-01 00:00:00.000000  751.0   85.0  ...      None           None   None
    1  1944-02-01 00:00:00.000000  713.0   77.0  ...      None           None   None
    2  1944-03-01 00:00:00.000000  741.0   90.0  ...      None           None   None
    3  1944-04-01 00:00:00.000000  650.0   89.0  ...      None           None   None
    4  1944-05-01 00:00:00.000000  681.0  106.0  ...      None           None   None
    
    [5 rows x 8 columns]
    Get sql result type:  <class 'pandas.core.frame.DataFrame'>



```python
# with join logic
query = """
select m.date, m.beef, b.births
from meat m
join birth b where m.date = b.date
"""

join_res = pysqldf(query)

print(join_res.head())
```

                             date    beef  births
    0  1975-01-01 00:00:00.000000  2106.0  265775
    1  1975-02-01 00:00:00.000000  1845.0  241045
    2  1975-03-01 00:00:00.000000  1891.0  268849
    3  1975-04-01 00:00:00.000000  1895.0  247455
    4  1975-05-01 00:00:00.000000  1849.0  254545


### 核心逻辑
pandasql 的核心实现原理主要包括两个方面：语法解析和数据处理。

- 语法解析：
当你调用 sqldf() 函数并传入 SQL 查询语句时，pandasql 首先会对这个查询语句进行解析。它会将 SQL 查询语句转换成标准的 SQL 语法树或类似的内部表示形式，以便进行后续的处理和执行。
- 数据处理：
一旦 SQL 查询语句被解析成内部表示形式，pandasql 接下来会将这个查询应用于指定的 Pandas DataFrame。它会按照查询语句中的操作（比如选择、过滤、聚合等）来处理 DataFrame，并生成符合查询条件的结果集。
在数据处理阶段，pandasql 将 SQL 查询中的各种操作映射到相应的 Pandas 操作。例如，SELECT 语句会映射到 Pandas 的选择操作，WHERE 子句会映射到 Pandas 的过滤操作，GROUP BY 子句会映射到 Pandas 的分组操作等等。通过这种映射，pandasql 实现了将 SQL 查询语句转换成 Pandas 操作的过程。
最后，pandasql 将处理后的结果集转换成 Pandas DataFrame，并返回给调用者，以供进一步的处理或分析。

综上所述，pandasql 的核心实现原理是通过解析 SQL 查询语句并将其映射到 Pandas 操作来实现对 Pandas DataFrame 的处理。这种实现方式使得用户可以使用熟悉的 SQL 语法来操作 DataFrame，从而简化了数据处理和分析的过程。

### 故事的最后

最终，经过不断地学习和实践，恬宝成为了一位 pandasql 的高手，她能够使用它来处理各种复杂的数据并生成有用的分析结果。她的家族成员们对她的成就感到非常骄傲，而恬宝也因为掌握了这项新技能而感到非常满足和自豪。

从此以后，恬宝成为了家族中的数据分析专家，她用 pandasql 帮助家族解决了许多实际的问题，为家族的发展和繁荣做出了贡献。她的故事成为了家族中的传奇，激励着每一个家族成员不断探索和学习新的技能，为自己的梦想努力奋斗。


### 实践建议

如何想通过sql来对dataframe进行查询的话，而且数据量不是很大的情况下，可以考虑使用`pandasql`来使用熟悉的SQL来对数据进行查询和处理。

其实现在大部分的框架都希望通过支持SQL来简化数据处理流程，比如`SparkSQL`, `FlinkSQL`等。

