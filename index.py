import io
import re
from ast import literal_eval

def replace_iter(data, iter_name, string_object):
    '''
    Find html template tag to loop over, replace with exact number of items.
    '''

    regex = re.compile('({{%' + iter_name + '\s+(.*)\s+%}})')
    found_tags = re.search(regex, string_object)
    new_tags = []
    for i in range(len(data)):
        new_tags.append(found_tags.group(2).replace('[i]', '[' + str(i) + ']'))
    return string_object.replace(found_tags.group(1), ''.join(new_tags))


def get_data():
    '''
    kludge until I build the next part
    '''
    with io.open('data/page1.py', encoding="utf-8") as tem:
        data = tem.read()
        data = literal_eval(data)
        return data


page_data = get_data()

with io.open('templates/template.html', encoding="utf-8") as tem:
    template = tem.read()
    template = replace_iter(page_data['excerpts'], 'excerpts', template)
    template = replace_iter(page_data['tags'], 'tags', template)

    print template.format(**page_data)
