#!/usr/bin/env python3
"""
Module contenant la fonction list_all.
"""


def list_all(mongo_collection):
    """
    Liste tous les documents d'une collection.
    """
    cursor = mongo_collection.find()
    return cursor
