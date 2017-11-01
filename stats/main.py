from collections import OrderedDict

import click

from calc import (get_accepted_answers,
                  get_avg_score,
                  get_avg_answers_per_question,
                  get_top_ten_comments_count)
import fetch
import render


output_formats = [
    'json',
    'html',
    'tabular'
]


@click.command()
@click.option('--since', required=True)
@click.option('--until', required=True)
@click.option('--output-format',
              default='json',
              type=click.Choice(output_formats))
def main(since, until, output_format):
    answers = fetch.get_answers(since, until)

    accepted_answers = get_accepted_answers(answers)
    results = OrderedDict([
        ('total_accepted_answers', len(accepted_answers)),
        ('accepted_answers_average_score', get_avg_score(accepted_answers)),
        ('average_answer_per_question', get_avg_answers_per_question(answers)),
        ('top_ten_answers_comment_count', get_top_ten_comments_count(answers)),
    ])

    # For demo purposes. Use logging framework in production.
    print(render.render_results(results, output_format))
