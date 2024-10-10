BASE_SUMMARIZE = """
Please summarize the following text, providing a brief overview of the topic and then highlighting the key points. This summary should be around 5-7 sentences long.
"""

BASE_EXTRACT = """
Please extract important words in the following text, reponse in the bullet point format. The number of bullet points should be around 5-7.
"""

MAP_REDUCE = """
Given the following extracted parts of a long document and a question,
create a final answer with references (\"SOURCES\"). \nIf you don't know
the answer, just say that you don't know. Don't try to make up an answer.\
nALWAYS return a \"SOURCES\" part in your answer.\n\nQUESTION: {question}\
n=========\nContent: {text}
"""

CHAIN_OF_DENSITY = """
You will generate increasingly concise, entity-dense summaries of the
above document.
Repeat the following 2 steps 5 times.
Step 1. Identify 1-3 informative entities (";" delimited) from the document
which are missing from the previously generated summary.
Step 2. Write a new, denser summary of identical length which covers every
entity and detail from the previous summary plus the missing entities.

A missing entity is:
- relevant to the main story,
- specific yet concise (5 words or fewer),
- novel (not in the previous summary),
- faithful (present in the document),
- anywhere (can be located anywhere in the document).

Guidelines:
- The first summary should be long (4-5 sentences, ~80 words) yet highly
non-specific, containing little information beyond the entities marked
as missing. Use overly verbose language and fillers (e.g., "this document
discusses") to reach ~80 words.
- Make every word count: rewrite the previous summary to improve flow and
make space for additional entities.
- Make space with fusion, compression, and removal of uninformative
phrases like "the document discusses".
- The summaries should become highly dense and concise yet self-contained,
i.e., easily understood without the document.
- Missing entities can appear anywhere in the new summary.
- Never drop entities from the previous summary. If space cannot be made,
add fewer new entities.
Remember, use the exact same number of words for each summary.
The result should be a list (length 5) of dictionaries whose
keys are "Missing_Entities" and "Denser_Summary:. 
"""