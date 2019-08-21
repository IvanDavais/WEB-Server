import re

job_information = """ <p>职责：<br>1. 根据业务目标，负责开发应用于客户所需业务领域的机器学习模型；</p>
<p>2. 深度挖掘用户数据，负责数据挖掘、异常检测及预测分类等相关模型、算法的设计与开发；</p>
<p>3. 配合开发人员完成数据模型开发、上线运行；</p>
<p>任职要求：&nbsp;<br>1. 有2年以上数据分析挖掘相关的工作经验；熟悉基础数据挖掘模型，熟练使用SQL（或者SAS、R等）数据分析工具；</p>
<p>2. 至少熟练掌握以下一种编程语言（Java、Python、C++、Scala），熟悉Python Pandas，SkLearn等建模package者优先；熟悉TensorFlow、PyTorch等 深度学习框架工具者优先；<br>3. 统计学、数学、计算机等相关专业优先，机器学习、数据挖掘、数据可视化等研究方向优先；&nbsp;<br><br></p>
        """
ret = re.sub(r"<.*?>|&nbsp;|\n", "", job_information)

# ret = re.sub(r"<[^>]*>|&nbsp;|\n", "", job_information)
print(ret)
