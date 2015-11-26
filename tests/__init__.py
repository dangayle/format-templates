import unittest
import tempfile
import shutil
import os
import io
from format_templates.format_templates import replace_iter, find_iters, render


class TestFormatting(unittest.TestCase):

    def setUp(self):
        self.data = {
            "name": "World",
            "numbers": xrange(1,5),
            "nested": {
                "nested_a": xrange(1,5),
                "nested_b": xrange(6,11)
            },
            "nested2": [xrange(1,5), xrange(6,11)]
        }
        self.template = "Hello {name}. {{%numbers {numbers[i]} %}}"
        self.template2 = "{{%nested {{%nested_b {nested_b[i]} %}} %}}"


    def test_find_iters(self):
        self.assertEqual(['numbers'], find_iters(self.template))


    def test_find_nested_iters(self):
        """
        Expected to fail.
        """
        self.assertEqual(['nested','nested_b'], find_iters(self.template2))


    def test_replace_iter(self):
        template = "{{%numbers {numbers[i]} %}}"
        self.assertEqual('{numbers[0]}{numbers[1]}{numbers[2]}{numbers[3]}', 
            replace_iter(self.data['numbers'], 'numbers', template))


    def test_render(self):
        rendered_string = "Hello World. 1234"
        self.assertEqual(rendered_string, render(self.data, self.template))
        pass



class TestHTMLRender(unittest.TestCase):
    """
    Test render an html page.
    """

    test_dir = os.path.dirname(__file__)

    def model(self):
        from models.page1 import page        
        return page


    def render_template(self, model, template_name):
        """
        Open template file, replace placeholders with data from model
        """
        template_path = os.path.join(self.test_dir, 'templates/' + template_name + '.html')
        with io.open(template_path) as template:
            template_name = template.read()
            return render(model, template_name)


    def render_html(self, model):
        return self.render_template(model, model['template'])


    def test_render(self):
        test_html_path = os.path.join(self.test_dir, 'test.html')
        rendered_html = self.render_html(self.model())
        with io.open(test_html_path) as test_html:
            self.assertEqual(test_html.read(),rendered_html)






