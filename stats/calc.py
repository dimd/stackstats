from __future__ import division
from collections import Counter
from operator import itemgetter

import fetch


def get_accepted_answers(answers):
    return [a
            for a in answers
            if a['is_accepted']]


def get_avg_score(answers):
    scores = [a['score'] for a in answers]
    return round(sum(scores) / len(answers), 1)


def get_avg_answers_per_question(answers):
    counter = Counter()

    for a in answers:
        counter[a['question_id']] += 1

    return round(sum(counter.values()) / len(counter), 1)


def get_top_ten_comments_count(answers):
    """Get the number of comments for the top ten answers"""
    top_ten = sorted(answers, key=itemgetter('score'), reverse=True)[:10]
    result = {}
    for a in top_ten:
        answer_id = a['answer_id']
        result[answer_id] = len(fetch.get_comment(answer_id))

    return result
