#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : chen
# @Time : 2024/6/14 9:56
# rules: 记录一下平常的规则也可以实现很好以及很快的算法 生成式规则

import random
from icecream import ic  # 用于调试打印

rules = """
复合句子 = 句子 , 连词 复合句子 | 句子
连词 = 而且 | 但是 | 不过
句子 = 主语 谓语 宾语
主语 = 你 | 我 | 他
谓语 = 玩 | 打 | 吃
宾语 = 皮球 | 香蕉 | 羽毛球 
"""


def generate_grammar_by_description(rules):
    # 按照行切割语法规则
    rule_list = [t.split("=") for t in rules.split('\n') if t.strip()]
    print(rule_list)
    grammar_list = [(t, ex.split('|')) for t, ex in rule_list]
    print(grammar_list)
    grammar = {t.strip(): [e.strip() for e in ex] for t, ex in grammar_list}
    print(grammar)
    return grammar


def generate_content_by_grammar(grammar, target="复合句子"):
    if target not in grammar: return target
    return "".join([generate_content_by_grammar(grammar, t) for t in random.choice(grammar[target]).split()])


if __name__ == "__main__":
    grammar = generate_grammar_by_description(rules)
    ic(generate_content_by_grammar(grammar, target="句子"))
    ic(generate_content_by_grammar(grammar, target="复合句子"))
