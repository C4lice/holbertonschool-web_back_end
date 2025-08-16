#!/usr/bin/env python3
"""
Module containing the function schools_by_topics.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Finds all schools having a specific topic.
    """
    cursor = mongo_collection.find({'topics': topic})
    return cursor
