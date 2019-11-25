#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)  # Create the html. # A web server is called.  # Contains the loop and makes it running forever.
server = app.server

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# Lines below are for setting.
app.layout = html.Div(children=[  # "children" is the text
    html.H1(children='Hello Dash'),  # H1: Header

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),  # From here starts another Div

    dcc.Graph(
        id='example-graph',
        figure={  # FIGURE is a structure, a tree, that contains two important things: data and layout
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},  # 可通过选择type来做3D图线
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':  # Execute the dash.Dash(); “if __name__ == '__main__':” 必须要写，因为是个script
    app.run_server(debug=False)

