import re
ret = re.search(r"\d+", "阅读次数为9999")
print(ret.group())

# 注意： search只返回达到正则条件的第一个数
ret1 =re.search(r"\d+", "阅读次数为9999，点赞次数为：100")
print(ret1.group())
