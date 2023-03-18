### JET template

> create JET template

Need pip

* `pip install rich`

Usage

```python
import pandas as pd
from journalsTemplate import JournalsTemplate

jet = journalsTemplate()

df = pd.read_csv()

# step 1 -> insert column
df = jet.insert_column(df)
# step 2 -> reset column
df = jet.reset_column(df, entity="Com")
# step 3 -> get standard templates
df = jet.get(df)
# step 4 -> convert date formate
df = jet.convert_date(df)
# step 5 -> convert number format
df = jet.convert_number(df)
# step 6 -> clear special symbols and limits string length
df = jet.convert_string(df)
# step 7 -> convert chinese to pinyin
df = jet.convert_chinese(df, py_type="lower")
# step 8 -> sort values
df = jet.sort(df)
# step 9 -> add Line Number
df = jet.add_number(df)
# step 10 -> add Financial Period
df = jet.add_month(df)
# step 11 -> add DC Indicator
df = jet.add_direction(df)
# step 12 -> add DC values
df = jet.add_dc(df)
# last, you can check the templates is correct or incorrect
jet.check(df)
```

Function

* `insert_column`:
  * 插入JET模板列

* `reset_column`: 
  * 重新指定column
* `get`:
  * 获取JET标准模板column
* `convert_date`:
  * 将日期格式转换为 `dd/mm/yyyy`
* `convert_number`:
  * 保留2位小数
* `convert_string`:
  * 去除特殊字符与保留前200字符
* `convert_chinese`:
  * 将汉字转换为拼音(默认大写,还有小写、首字母大写、缩写)
* `pivot`: 
  * 数据透视
  * Net 2 Zero
* `calculation_sum`:
  * 计算*debit*、*credit*、*amount*的加总
* `sort`:
  * 按照*Journal Number* 排序
* `add_number`:
  * 添加 *Line Number*
* `add_month`:
  * 添加 *Financial Period*
* `add_direction`:
  * 添加*DC Indicator*
* `add_dc`:
  * 添加*D C* values
* `get_last_account`:
  * 取末级科目
* `screen`:
  * 条件筛选(根据末级科目可筛选出需要的结果)
* `calculation_dc`:
  * 计算借贷方向
  * 调整借贷值的正负
* `write`:
  * 保存数据为txt格式,分隔符为|且编码为utf-16le
* `check`:
  * 检查借贷是否相等,amount是否为0
  * 检查 *Auto Manual or Interface*
  * 检查借贷是否存在负数
  * 检查 *Financial Period*
  * 检查 *Entity*
  * 检查 *Currency*、 *Currency EC*
