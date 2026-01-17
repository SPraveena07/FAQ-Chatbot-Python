FAQ Chatbot using Python
This project is a Retrieval-based FAQ Chatbot developed as part of my Python Internship Task 2. The chatbot is designed to understand user queries and provide the most relevant answer from a predefined set of Frequently Asked Questions (FAQs).

Features
Text Preprocessing: Uses NLTK library for tokenizing and cleaning user input.

Similarity Matching: Implements Cosine Similarity to find the closest match between the user's question and the FAQ database.

Automated Responses: Provides instant answers for topics like product returns, shipping times, and Python basics.

Technologies Used
Language: Python 3.x

Libraries: * nltk (Natural Language Toolkit)

math (for manual similarity calculations)

collections (for vectorization)

How It Works
Data Collection: A dictionary of questions and answers is maintained.

Preprocessing: User input is converted to lowercase and tokenized using nltk.word_tokenize.

Matching: The bot calculates the Cosine Similarity score for each question in the database.

Response: The answer with the highest similarity score is displayed to the user.

How to Run
Install dependencies:
Bash
pip install nltk

Run the application:
Bash
python app.py
