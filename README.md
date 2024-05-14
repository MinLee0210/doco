<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/MinLee0210/DoCo.git">
    <img src="static/logo/CD.png" alt="Logo" width="120" height="120">
  </a>

<h3 align="center">DoCo-Document Compressor</h3>

  <p align="center">
    The project aims to develop an AI platform for extracting weighted features from documents by summarizing and gathering strong relational words.
    <br/>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>📃 Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#directory-structures">Directory Structures</a></li>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#gallery">Gallery</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgments</a></li>
  </ol>
</details>

<div id='about-the-project'><h2>👀 About the project </h2></div>
We are developing an advanced system using Large Language Models (LLMs) to automatically summarize various types of documents, including reports, news articles, and meeting transcripts. This project aims to help professionals quickly access key insights, trends, and significant events from extensive textual data, facilitating informed decision-making and improving efficiency across different fields.

Project Features:

+ **Context-Aware Summarization**: Capture and highlight relevant information.
+ **Platform Integration**: Seamlessly integrate with existing data platforms.
+ **Sophisticated Sentiment Analysis**: Accurately gauge sentiment in the text.

<div id='getting-started'><h2>😚 Getting started </h2></div>
<div id=''><h2>📊 CURRENT STATUS</h2></div>
<h3>⏳ ON DEVELOPMENT</h3>

We apologize for any inconvenience caused as our project undergoes essential updates. During this period, you may experience disruptions or limited access to our services. We appreciate your patience and understanding as we work to enhance our system. Thank you for your continued support.


<div id='directory-structures'><h3>📁 Directory Structures<h3></div>

```
  | controller    # where we write functions and prompts
    | apiv1       => Use HuggingFace's API Inference.
    | apiv2       => Use LangChain along with HuggingFacePipeline to summarize the task. 
  | models        # models, if it is neccessary to be downloaded, it would be stored here. 
    | v1
    | doco        => Use LangChain along with HuggingFacePipeline to summarize the task. 
  | notebooks     # we store demonstrations, explanations, documents, Jupyter notebooks, ...
  | static        # where we store images: logo, results, ...
  | views         # for UI
  .gitignore
  app.py
  TODO
  config.py
  README.md
```

<div id='installation'> <h3>🤓 Installation</h3></div>

1. Cloning the project
```
  git clone https://github.com/MinLe0210/Doco
  cd Doco
  pip install -r requirements.txt
```
2. Run streamlit app
```
  streamlit run app.py # to run the app
```

<div id='roadmap'><h2>🎯 Roadmap</h2></div>

- [x] Automated Summarization and Extraction: Automatically summarize documents and extract important features.

- [ ] Sophisticated Sentiment Analysis: Analyze documents to accurately gauge sentiment.

- [ ] Real-Time Question Answering: Implement Retrieval-Augmented Generation (RAG) for real-time question-answering tasks.

<div id='gallery'><h2>Gallery</h2></div>

An example of how the agent works
<p align="center">
  <img src="static/result_text_00.png" width="45%" />
  &nbsp; &nbsp; &nbsp; &nbsp;
  <img src="static/result_text_01.png" width="45%" /> 
</p>

<div id='contact'><h2>📨 Contact me</h2></div>
Don't hesitate to contact me via: 

+ Gmail: minh.leduc.0210@gmail.com

+ Linkedin: https://www.linkedin.com/in/minh-le-duc-a62863172/

+ Github: https://github.com/MinLee0210/DoCo.git
