#!/usr/bin/env python
from google.cloud import language_v1
import os


def analyze_sentiment(text: str) -> dict:
    """A function that perform sentiment analysis using google NL API"""
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './google_key.json'
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text,
                                    type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_sentiment(request={'document': document})
    sentiment = response.document_sentiment
    return sentiment
