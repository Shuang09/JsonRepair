# data process

## 数据污染目标：
- 受污染后的文件格式不正确，无法通过jsonlaods()
- 受污染的文件命名和其母本一样
- 污染后的文件可以用str读出来
- target_input: 格式正确的json文件 ->污染 -> input_json
- json_valid: 格式正确的json文件 ->污染 -> json_pollute


##文件读取代码：
- 假设读取json-valid 文件
- 目的是：Vectorize the data. 即首先将文件夹内所有文件target_texts.append；再以char读出字典，后续sort,每一个char都可用向量表示。例如 target_characters = set(a, b, c) -> a[1,0,0]
```python
target_data_path = "./json-valid"
target_texts = []
target_characters = set()
target_files = os.listdir(target_data_path)
for target_file in target_files:
    if not os.path.isdir(target_file):
        with open(target_data_path +"/" + target_file,'r') as target_f:
            target_data = target_f.read()
            target_texts.append(target_data)
            for char in target_data:
                if char not in target_characters:
                    target_characters .add(char)
```


> 如果要符合手敲的习惯，还需要考虑键盘中挨得比较近的键作替换。或者其他研究成果给出的容易被替换的字符对。

1. `json_check(string)` 函数检查`string`是否是合法的json文件
    * 合法的json文件，返回 `(1, string)`
    * 非法的json文件，返回 `(0, string)`

```shell
>>> from JsonPollute import json_check
>>> simple = '{"key":1}'
>>> json_check(simple)
(1, '{"key":1}')
```

2. `JsonPollute`类用于生成被污染的json文件
    1. 实例
        * 传入的`string`必须是合法的json文件
        * 传入的`pollute_rate`可以是(0,1)的浮点数，也可以是大于等于1的整数
    2. 污染
        * `JsonPollute.pollute()`返回被标注的污染后的字符串
        * 传参`cw`设置四种污染类型的比例，默认各种污染类型出现的概率均等

```shell
>>>from JsonPollute import JsonPollute
>>>simple = '{"key":1}'
>>>jsp = JsonPollute(simple, pollute_rate=3)
>>>jsp.pollute([0, 1, 1, 1])
(0, '{k""ey:1}')
```

# 以 byte 为单位进行污染

> 实现和意义有待讨论。byte序列变动后的数目必须是8的整数倍，且要讨论某个字节在变动后是否依旧是‘可显示字符’。
> 纯byte层面的变动似乎在网络通信的“可靠传输”中被解决。
