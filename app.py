import nltk
import math
from collections import Counter

# 1. Collect FAQs (கமா பிழைகள் இல்லாமல் சரிசெய்யப்பட்டது)
faq_data = {
    "hello": "Hi there! How can I help you today?",
    "what is your name": "I am your FAQ Assistant bot.",
    "how to return product": "You can return products within 30 days.",
    "shipping time": "It usually takes 3-5 business days.",
    "python topics": "The 5 key topics are: 1. Variables, 2. Loops, 3. Functions, 4. Lists, 5. Classes.",
    "bye": "Goodbye! Have a great day!" # கடைசி வரிக்கு கமா தேவையில்லை, ஆனால் முந்தைய வரிகளுக்கு வேண்டும்
}

# 2. Preprocess the text using NLTK
def get_tokens(text):
    return nltk.word_tokenize(text.lower())

# 3. Match user questions using Cosine Similarity
def calculate_cosine_similarity(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    return float(numerator) / denominator if denominator else 0.0

def get_response(user_input):
    user_tokens = get_tokens(user_input)
    user_vec = Counter(user_tokens)
    
    best_score = -1
    best_match = ""

    for question in faq_data.keys():
        question_tokens = get_tokens(question)
        question_vec = Counter(question_tokens)
        score = calculate_cosine_similarity(user_vec, question_vec)
        
        if score > best_score:
            best_score = score
            best_match = question

    # 4. Display the best matching answer
    if best_score < 0.2:
        return "I'm sorry, I don't understand. Please ask about returns, shipping, or python topics."
    else:
        return faq_data[best_match]

print("\n" + "="*40)
print("FAQ BOT IS ONLINE! (Type 'exit' to stop)")
print("="*40 + "\n")

while True:
    user_query = input("You: ")
    if user_query.lower() in ['exit', 'quit', 'bye']:
        print("Bot: Goodbye!")
        break
    
    if not user_query.strip():
        continue

    print("Bot:", get_response(user_query))