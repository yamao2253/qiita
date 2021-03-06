# -*- coding: utf-8 -*-

import sys

# 1. それぞれのリストをfor文で回して要素を取り出し比較する 
def cmp_for_for(src_list, tag_list):
    matched_list = []
    for tag in tag_list:
        for src in src_list:
            if tag == src:
                matched_list.append(tag)

    return matched_list

# 2. 1つのリストはfor文、もう1つはfilter関数で要素を取り出して比較する
def cmp_for_filter(src_list, tag_list):
    matched_list = []
    for tag in tag_list:
        matched_list+=filter(lambda str: str == tag, src_list)

    return matched_list

# 3. リストを集合型(set)に変換して論理積をとる。その結果をリストに変換する
def cmp_set_list(src_list, tag_list):
    src_set = set(src_list)
    tag_set = set(tag_list)
    return list(src_set & tag_set)

# 4. 内包表記で、for+filter っぽく記述
def cmp_list_comprehension(src_list, tag_list):
    return [tag for tag in tag_list if tag in src_list] 

# 5. 集合型のintersection関数を使う
def cmp_set_intersection(src_list, tag_list):
    src_set = set(src_list)
    tag_set = set(tag_list)
    return list(src_set.intersection(tag_set))


src_list=['taniguchi', 'matsushita', 'koyama', 'asama', 
          'marui', 'igarashi', 'kubo', 'kondo']

# 実行時の引数をtag_listとする
argvs=sys.argv
argc=len(argvs)
tag_list=argvs[1:]


print "# 1. それぞれのリストをfor文で回して要素を取り出し比較する"
matched_list = cmp_for_for(src_list, tag_list)
print matched_list , "\n"
if len(matched_list) == 0:
    print "No match!"

print "# 2. 1つのリストはfor文、もう1つはfilter関数で要素を取り出して比較する"
matched_list = cmp_for_filter(src_list, tag_list)
print matched_list , "\n"
if len(matched_list) == 0:
    print "No match!"

print "# 3. リストを集合型(set)に変換して論理積をとる。その結果をリストに変換する"
matched_list = cmp_set_list(src_list, tag_list)
print matched_list , "\n"
if len(matched_list) == 0:
    print "No match!"

print "# 4. 内包表記で、for+filter っぽく記述"
matched_list = cmp_list_comprehension(src_list, tag_list)
print matched_list , "\n"
if len(matched_list) == 0:
    print "No match!"

print "# 5. 集合型のintersection関数を使う"
matched_list = cmp_set_intersection(src_list, tag_list)
print matched_list , "\n"
if len(matched_list) == 0:
    print "No match!"


