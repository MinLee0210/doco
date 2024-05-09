"""
Reference: 
+ https://textcortex.com/post/chatgpt-prompts-for-conclusions
+ https://narrato.io/blog/get-precise-insights-with-30-chatgpt-prompts-for-summary-generation/
"""

default_summarize = """
You will generate concise, entity-dense summaries of the above document. Do not discuss the guidelines for summarization in your response.

Guidelines for summarization:

- The first should be concise (4-5 sentences, ~80 words).

- Make every word count. Do not fill with additional words which are not critical to summarize the original document.

- Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".

- The summaries should become highly dense and concise yet self-contained, i.e., easily understood without the article.
"""

chain_of_density = """
Article: {text}
You will generate increasingly concise, entity-dense summaries of the
above article.
Repeat the following 2 steps 5 times.
Step 1. Identify 1-3 informative entities (";" delimited) from the article
which are missing from the previously generated summary.
Step 2. Write a new, denser summary of identical length which covers every
entity and detail from the previous summary plus the missing entities.
A missing entity is:
- relevant to the main story,
- specific yet concise (5 words or fewer),
- novel (not in the previous summary),
- faithful (present in the article),
- anywhere (can be located anywhere in the article).
"""