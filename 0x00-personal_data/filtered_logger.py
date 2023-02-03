#!/usr/bin/env python3
"""
Main module
"""


import re


def filter_datuem(fields: list, redaction: str, message: str,
                  separator: str) -> str:
    """
    Returns an obfuscated string
    Args:
        fields (list): strings representing all fields to obfuscate
        redaction (str): what the field will be obfuscated
        message (str): the log line
        seperator (str): character seperating all fields in the log line
    """
    for field in fields:
        message = re.sub(field + '=.*?' + separator,
                         field + '=' + redaction + separator, message)
    return message
