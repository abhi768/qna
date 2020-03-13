# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from flask import Config
import wikipedia as wk
from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount
import re, string, unicodedata

class QnABot(ActivityHandler):
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome to QnA!")
   
    async def on_message_activity(self, turn_context: TurnContext):
   # The actual call to the QnA Maker service.
       text = turn_context.activity.text.lower()
       if "hey,tell me about" in text:
            
            response_text = self._process_input(text)
            await turn_context.send_activity(MessageFactory.text(response_text))
       else:
            response = await self.qna_maker.get_answers(turn_context)
            if response and len(response) > 0:
                await turn_context.send_activity(MessageFactory.text(response[0].answer))
            else:
                await turn_context.send_activity("No QnA Maker answers were found.")
        
    
    def __init__(self, config: Config):
   	  self.qna_maker = QnAMaker(
     		 QnAMakerEndpoint(
         knowledge_base_id=config.QNA_KNOWLEDGEBASE_ID,
         endpoint_key=config.QNA_ENDPOINT_KEY,
         host=config.QNA_ENDPOINT_HOST,
   		)
		)
    
    def _process_input(self,query:str):
        
        reg_ex = re.search('hey,tell me about (.*)', query)
        try:
            if reg_ex:
                topic = reg_ex.group(1)
                wiki = wk.summary(topic, sentences = 3)
                return wiki
        except Exception as e:
                tx="No content has been found"
                return tx