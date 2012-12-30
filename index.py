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


def find_iters(string_object):
    '''
    Find all the iterable template tags.
    '''

    regex = re.compile('{{%(.*)\s+.*\s+%}}')
    found_tags = re.findall(regex, string_object)
    return found_tags


def model():
    '''
    kludge until I build the data part
    '''

    with io.open('data/page1.py', encoding="utf-8") as tem:
        data = tem.read()
        data = literal_eval(data)
        return data


def view(page_data, template):
    '''
    Open template file, replace placeholders with data
    '''

    with io.open('templates/' + template + '.html', encoding="utf-8") as tem:
        template = tem.read()

        iterables = find_iters(template)
        for item in iterables:
            template = replace_iter(page_data[item], item, template)
        return template.format(**page_data)


def main():
    page_data = model()
    print(view(page_data, 'template'))

if __name__ == "__main__" : main()
