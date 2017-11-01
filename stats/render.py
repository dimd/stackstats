import json

from jinja2 import Environment, PackageLoader
from tabulate import tabulate


def render_results(results, output_format):
    if output_format == 'json':
        output = json.dumps(results, indent=4)
    elif output_format == 'html':
        env = Environment(loader=PackageLoader('stats'))
        template = env.get_template('results.html.j2')
        output = template.render(results)
    else:
        output = tabulate([results.values()],
                          headers=results.keys())

    return output
