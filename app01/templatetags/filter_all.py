#Author:Santi

from django import template
from django.utils.safestring import mark_safe
register = template.Library()
@register.simple_tag()
def filter_all(arg_dict,k):
    if k == 'article_type_id':
        n1 = arg_dict['article_type_id']
        n2 = arg_dict['category_id']
        if n1 == 0:
            ret = '<a class="active" href="article-0-%s.html">全部</a>' % n2
        else:
            ret = '<a href="article-0-%s.html">全部</a>' % n2
    elif k == 'category_id':
        n1 = arg_dict['article_type_id']
        n2 = arg_dict['category_id']
        if n2 == 0:
            ret = '<a class="active" href="article-%s-0.html">全部</a>' % n1
        else:
            ret = '<a href="article-%s-0.html">全部</a>' % n1
    return mark_safe(ret)

@register.simple_tag()
def filter_article_type_list(arg1,arg_dict):
    ret = []
    for row in arg1:
        if row.id == arg_dict['article_type_id']:
            ret.append('<a class="active" href="article-%s-%s.html">%s</a>' % (row.id,arg_dict['category_id'],row.caption))
        else:
            ret.append('<a href="article-%s-%s.html">%s</a>' % (row.id,arg_dict['category_id'],row.caption))
    return mark_safe(''.join(ret))


@register.simple_tag()
def filter_category_list(arg1,arg_dict):
    ret = []
    for row in arg1:
        if row.id == arg_dict['category_id']:
            ret.append('<a class="active" href="article-%s-%s.html">%s</a>' % (arg_dict['article_type_id'],row.id,row.caption))
        else:
            ret.append('<a href="article-%s-%s.html">%s</a>' % (
            arg_dict['article_type_id'], row.id, row.caption))

    return mark_safe(''.join(ret))