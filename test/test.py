# Gemini' API testing

import os

from doco.agents import GeminiAgent

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
doco_agent = GeminiAgent()

text = "The Grand Canyon is one of the most iconic natural wonders in the world. Carved by the Colorado River over millions of years, it stretches for 277 miles and reaches depths of over a mile. The canyon is home to a diverse ecosystem, with towering rock formations, lush forests, and a variety of wildlife. Visitors can explore the canyon by hiking, mule riding, or taking a helicopter tour. The Grand Canyon is a popular destination for outdoor enthusiasts and nature lovers alike, offering breathtaking views and a glimpse into the Earth's geological history."
result = mdoco_agentodel.invoke(text)

print(result)