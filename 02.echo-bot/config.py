#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "ed7d1372-1717-4af3-8ef0-f6a89c97f3f3")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "67c874df-ebf3-4c39-9661-77ba61968713")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://my-qna-bot12.azurewebsites.net/qnamaker")