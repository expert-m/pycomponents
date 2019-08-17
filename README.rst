============
pycomponents
============


Install
-------

From pip, run::

    $ pip3 install -U git+https://github.com/expert-m/pycomponents.git


Usage
-----
Example::

    import os
    import random
    import string
    import webbrowser

    from pycomponents import TextComponent
    from pycomponents.html import (
        B, Body, BR, Button, Code, Div, EscapeCharacter, File, H1, H2, Head, HR, Html, HtmlComment, Jinja2, Meta, P, Pre,
        Progress, Style, Table, TD, Title, TR,
    )


    class Spoiler(TextComponent):
        def __init__(self, *args, **kwargs):
            self.text = kwargs.pop('text', 'Spoiler')
            self.rand_id = self._generate_random_id()
            super().__init__(*args, **kwargs)

        @staticmethod
        def _generate_random_id():
            letters = string.ascii_lowercase
            random_str = ''.join(random.choice(letters) for i in range(10))
            return f'collapse-{random_str}'

        def render(self):
            return Div(**self.kwargs, child=[
                P(
                    Button(
                        self.text,
                        class_='btn btn-primary',
                        type_='button',
                        data_toggle='collapse',
                        data_target=f'#{self.rand_id}',
                        aria_expanded='false',
                        aria_controls='collapseExample',
                    ),
                ),
                Div(class_='collapse', id=self.rand_id, child=[
                    Div(class_='card card-body', child=self.render_component(self.child)),
                ]),
            ])


    class TodoList(TextComponent):
        todos = [
            {'text': 'Create library', 'done': True},
            {'text': 'Publish on GitHub  ', 'done': False},
            {'text': 'Publish my package on PyPI  ', 'done': False},
        ]

        def render(self):
            todos = []
            completed_count = 0

            for todo in self.todos:
                if todo['done']:
                    completed_count += 1

                todos.append([
                    Div(class_='card', child=[
                        Div(todo['text'], class_='card-body'),
                    ]),
                    BR(),
                ])

            return Div([
                B('Tasks:'),
                Div(todos),
                BR(),
                BR(),
                B('Progress:'),
                Progress(style={'width': '100%'}, max=len(todos), value=completed_count),
            ])


    class HtmlPage(TextComponent):
        def render(self):
            return Html([
                HtmlComment('Test example'),
                Head([
                    Title('Hello'),
                    Meta(charset='utf-8'),
                    Meta(name='viewport', content='width=device-width, initial-scale=1, shrink-to-fit=no'),
                    Style(href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'),
                ]),
                Body([
                    Div(style={'color': 'black'}, class_='container', child=[
                        Div(class_=['row', 'justify-content-center'], child=[
                            Div(class_='col-md-8', child=[
                                HR(),
                                H1('PyComponents', class_='text-center'),
                                HR(),
                                H2('Example'),
                                BR(),
                                Spoiler(Pre(Code(EscapeCharacter(File('./main.py')))), text='Code'),
                                HR(),
                                H2('Some table'),
                                BR(),
                                Table(class_='table', child=[
                                    TR([
                                        TD('Test 1'),
                                        TD('Test 2'),
                                        TD('Test 3'),
                                    ]),
                                    TR([
                                        TD('Test 4'),
                                        TD('Test 5'),
                                        TD('Test 6'),
                                    ]),
                                ]),
                                HR(),
                                H2('Jinja2'),
                                BR(),
                                Jinja2(
                                    '<b>Name:</b> {{ user_name }}<br/><b>Site:</b> {{ site }}',
                                    user_name='Michael',
                                    site='https://sulyak.info'
                                ),
                                HR(),
                                H2('TODO'),
                                BR(),
                                TodoList(),
                            ]),
                        ]),
                    ]),
                    """
                    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
                    """,
                ])
            ])


    def main():
        component = HtmlPage()
        component.init({})
        data = component.get()
        # data = HTMLBeautifier.beautify(data, 4)
        # print(data)

        with open('./index.html', 'w') as file:
            file.write(data)

        webbrowser.open_new_tab(f'{os.getcwd()}/index.html')


    if __name__ == '__main__':
        main()


Links
-----

pycomponents is licensed under the MIT license.
