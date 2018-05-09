# PaddlePaddle AI 产业应用赛——汽车大师问答摘要与推理 --- 评审环节

欢迎参加[科赛网](https://www.kesci.com)和百度联合举办的[PaddlePaddle AI 产业应用赛——汽车大师问答摘要与推理](https://www.kesci.com/apps/home/competition/5aec0eb10739c42faa203931)。我们提供此次比赛的评审脚本，供选手在K-Lab内对个人的模型进行 **验证(validation)**。

## 算法介绍

评测用到的核心算法为[ROUGE](https://en.wikipedia.org/wiki/ROUGE_(metric))，即：Recall-Oriented Understudy for Gisting Evaluation，具体用到的指标为ROUGE_L，即：Longest Common Subsequence ([LCS](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)) based statistics。

测评函数详见`qichedashi.py`

## 代码使用

请按照如下步骤完成模型验证。
* 在K-Lab内打开创建的比赛项目

* 在Code Cell内执行下面的指令：
```
%%bash
cd /home/kesci/work
git clone https://github.com/Kesci/qichedashi_evaluation.git
```
* 完成仓库的clone之后，请在Code Cell内执行下面的命令，完成validation。
```
%%bash
cd /home/kesci/work/qichedashi_evaluation/
python3 qichedashi.py /path/to/submit/file /path/to/validation/file
```
