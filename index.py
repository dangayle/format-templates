import io
import re


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

    # print found_tags[0][0]
    # return(string_object.replace(found_tags.group(0), ''.join(new_tags)))


with io.open('templates/template.html', encoding="utf-8") as tem:
    template = tem.read()

    excerpts = [
        {
        'title': 'Alpha',
        'permalink': "alpha",
        'node': 'greekletters',
        'date': 'today',
        'author': 'Dan',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
        },
        {
        'title': 'Beta',
        'permalink': "beta",
        'node': 'greekletters',
        'date': 'today',
        'author': 'Dan',
        'content': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        },
        {
        'title': 'Gamma',
        'permalink': "alpha",
        'node': 'greekletters',
        'date': 'today',
        'author': 'Dan',
        'content': 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
        },
        {
        'title': 'Delta',
        'permalink': "beta",
        'node': 'greekletters',
        'date': 'today',
        'author': 'Dan',
        'content': 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        }

    ]

    page_data = {
        'name': 'Dan',
        'excerpts': excerpts
    }

    template = replace_iter(excerpts, 'excerpts', template)

    # print template
    print template.format(**page_data)
