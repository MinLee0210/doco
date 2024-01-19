# About Document Summarization with Deep Learning

## Introduction

Clearly, we can see that thanks to the advancement of the technology, the traffic of information becomes more remarkably astonishing. However, the advantage does raise a disturb phenomenon in which a person who need to do research or whose job relate to searching documents becomes drowned. A tool which is able to extract most important features from documents are actually in need. 

Automatic text summarization comes and save the day. Summarize is an act of convey important information from the original text(s). Automatic text summarization is the task of producing a concise and fluent summary while preserving key information content and overall meaning. The task is usually put into question since the action requires human knowledge and language adaptability. However, there are many researches have been raised and prove that, although the quality is not remarkable, but the capability is implement-able and develop-able. 

There are 2 main schools in this interesting field: 
1. Extractive approach: this approach is a technique for creating summaries of texts by selecting and combining existing sentences from the original document. These sentences are chosen based on their relevance and importance to the overall theme of the text. In other words, Extractive summarization picks out the most important pieces of information from each document and puts them together to create a concise overview of the entire topic. Here are some key features of extractive summarization:

+ Simple and efficient: It's relatively easy to implement and works well on short texts.
+ Preserves factual accuracy: The sentences are taken directly from the source text, so they are guaranteed to be factual.
+ Maintains coherence: By selecting sentences that are close together in the original text, the summary generally flows smoothly.
+ May lack originality: The summary may not contain any new insights or ideas, as it simply reflects the content of the original text.
+ Potentially misses key points: If important information is not contained in complete sentences, it may be missed by the summarization process.

2. Abstractive approach: this approach is a sophisticated approach to summarizing text that takes things a step further than its extractive counterpart. Instead of simply picking and choosing existing sentences, it delves deeper, understanding the main ideas and concepts of the original text, and then rephrases them in its own words, creating a concise and informative summary. Here are some key features of abstractive summarization:

+ Highly insightful: Can capture the main ideas and concepts beyond the surface level of the text, providing deeper understanding.
+ More concise: Often produces shorter summaries compared to extractive methods, focusing on the most essential information.
+ Original and creative: Generates new sentences and phrases, potentially expressing insights not explicitly stated in the source text.
+ More complex to implement: Requires advanced models and training techniques, typically involving deep learning methods like neural networks.
+ May introduce potential inaccuracies: The generated text, while creative, can deviate from the factual content of the original source.

Comparing to our daily life, we can see that we tend to do extractive summarize whenever a job requires the task. For instance, we have to do research for our companies. We want the research to be done as fast as possible but also be concise. Therefore, we would look up multiple available resources and search for the most valuable information. Practicing abstractive approach requires more than that. This is because of the fact that abstractive summarization methods cope with problems such as semantic representation, inference and natural language generation which are relatively harder than data-driven approaches such as sentence extraction.



## Methodologies

## Evaluation


## Reference
### Articles
```
    @misc{allahyari2017text,
        title={Text Summarization Techniques: A Brief Survey}, 
        author={Mehdi Allahyari and Seyedamin Pouriyeh and Mehdi Assefi and Saeid Safaei and Elizabeth D. Trippe and Juan B. Gutierrez and Krys Kochut},
        year={2017},
        eprint={1707.02268},
        archivePrefix={arXiv},
        primaryClass={cs.CL}
    }
```

### Blog
+ [Evaluation Metrics: Assessing the quality of NLG outputs - Devrim Çavuşoğlu](https://towardsdatascience.com/evaluation-metrics-assessing-the-quality-of-nlg-outputs-39749a115ff3)