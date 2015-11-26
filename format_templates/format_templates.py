from __future__ import print_function
import io
import os
import re
import sys
from ast import literal_eval
import logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


def replace_iter(variable, variable_name, template_string):
    """
    Find html template tag to loop over, replace with exact number of items.
    """

    # {{% + variable + any number of spaces + MATCH + any number of spaces + %}}
    pattern = re.compile('({{%' + variable_name + '\s+(.*?)\s+%}})')
    tags = re.search(pattern, template_string)
    # logger.debug("found matching tags: {}".format(tags.groups()))

    # create list of new strings to append to template
    new_tags = []
    for i, _ in enumerate(variable):
        new_tags.append(tags.group(2).replace('[i]', '[' + str(i) + ']'))
        
    # logger.debug(new_tags)

    return template_string.replace(tags.group(1), ''.join(new_tags))


def find_iters(template_string):
    """
    Find all the iterable template tags within template string.

    Template tag is same name as iterable

    TODO: Test failing because this can't/doesn't find nested tags
    {{%excerpts <li><h2>{excerpts[i][title]}</h2><p>{excerpts[i][content]}</p></li> %}}
    """

    # {{% match + any number of spaces + whatever + any number of spaces + %}}
    pattern = re.compile('{{%(.*?)\s+.*\s+%}}')
    tags = re.findall(pattern, template_string)
    
    return tags


def render(model, template):
    """
    Render the template using Python's built-in string formatting 
    functionality after expanding any iterable loops in the template
    """

    iterables = find_iters(template)
    for variable_name in iterables:
        template = replace_iter(model[variable_name], variable_name, template)
    
    return template.format(**model)
