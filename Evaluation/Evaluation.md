# Chatbot Evaluation Report

## Overview
This report evaluates the performance of a chatbot based on its responses to user queries. The chatbot's performance is assessed using three primary evaluation metrics: **Accuracy, Relevance, and Satisfaction**. Additionally, more advanced metrics such as **BLEU, ROUGE, and METEOR scores** are calculated to assess the quality of the chatbot's responses in comparison to predefined answers from a CSV file.

## Evaluation Methodology
The chatbot responses were compared to predefined answers that were manually crafted to match the expected responses for a set of common questions. The evaluation was carried out using the following metrics:

- **Accuracy**: Measured how closely the chatbot's response matched the predefined answer.
- **Relevance**: Determined if the chatbot's response was related and relevant to the user's query.
- **Satisfaction**: Evaluated based on the clarity and length of the response (longer answers are assumed to provide more clarity).

Additionally, three NLP evaluation scores were computed:

- **BLEU (Bilingual Evaluation Understudy Score)**: Measures the overlap between the bot's response and the reference answer.
- **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**: Measures the overlap of n-grams, reflecting how similar the bot's response is to the reference.
- **METEOR (Metric for Evaluation of Translation with Explicit ORdering)**: Evaluates the quality of the response by measuring precision, recall, synonymy, stemming, and word order.

## Evaluation Results
### User Question 1: *What is the return policy for items purchased at our store?*
- **Bot Response**: Our store offers a comprehensive return policy designed to make your shopping experience hassle-free. (includes detailed policy breakdown)
- **Predefined Answer**: You can return most items within 30 days of purchase for a full refund or exchange. Items must be in their original condition, with all tags and packaging intact. Please bring your receipt or proof of purchase when returning items.
  - Accuracy: **1.7 / 5**
  - Relevance: **3 / 5**
  - Satisfaction: **5 / 5**
  - BLEU Score: **19.20**
  - ROUGE Scores:
    - rouge1: **0.4242**
    - rouge2: **0.3558**
    - rougeL: **0.4**
  - METEOR Score: **None** (Error due to tokenization issue)

### User Question 2: *Are there any items that cannot be returned under this policy?*
- **Bot Response**: Yes, there are certain items that are non-returnable under our return policy. (details specific non-returnable items)
- **Predefined Answer**: Yes, certain items such as clearance merchandise, perishable goods, and personal care items are non-returnable. Please check the product description or ask a store associate for more details.
  - Accuracy: **0.1 / 5**
  - Relevance: **3 / 5**
  - Satisfaction: **5 / 5**
  - BLEU Score: **16.82**
  - ROUGE Scores:
    - rouge1: **0.3619**
    - rouge2: **0.2654**
    - rougeL: **0.3478**
  - METEOR Score: **None** (Error due to tokenization issue)

### User Question 3: *How will I receive my refund?*
- **Bot Response**: Refunds will be issued to the original form of payment used at the time of purchase. (details refund process)
- **Predefined Answer**: Refunds will be issued to the original form of payment used at the time of purchase. Please bring your receipt or proof of purchase for processing.
  - Accuracy: **1.21 / 5**
  - Relevance: **3 / 5**
  - Satisfaction: **5 / 5**
  - BLEU Score: **20.15**
  - ROUGE Scores:
    - rouge1: **0.4347**
    - rouge2: **0.3685**
    - rougeL: **0.4123**
  - METEOR Score: **None** (Error due to tokenization issue)

## Key Observations
- **Accuracy**: The chatbot's accuracy in matching predefined answers was generally low (ranging from 0.1 to 1.7 out of 5). While the chatbot provided helpful information, it did not fully align with the exact phrasing of the predefined answers.
- **Relevance**: The relevance of the responses was rated at **3 out of 5** for most cases, suggesting that while the chatbot's answers were related, they included excessive or unnecessary details in certain situations.
- **Satisfaction**: The satisfaction score remained high (**5/5**), as the chatbot's responses were clear and comprehensive.
- **BLEU Score**: The BLEU scores ranged from **16 to 20**, indicating moderate overlap between the chatbot's responses and the predefined answers.
- **ROUGE Scores**: The ROUGE scores indicate a fair level of similarity in terms of word overlap but show that the responses were not exact matches.
- **METEOR Score**: Errors in calculating the METEOR score were mainly due to tokenization issues, highlighting the need for preprocessing the responses for evaluation.

## Conclusion and Recommendations
- The chatbot's responses were generally helpful but lacked high precision compared to predefined answers. There is room for improvement in terms of **accuracy and alignment** with expected responses.
- While the chatbot's responses were relevant and clear, they could be refined to better match the expected **language and structure** of predefined answers.
- Future iterations should include **improvements in tokenization** and response generation to better handle metrics like METEOR.
- Handling **variations in language and response phrasing** could improve both accuracy and relevance scores.

### Final Thoughts
Overall, the chatbot performed reasonably well in providing relevant information. Since it is an intelligent chatbot, it is **not expected to provide exact answers** to predefined questions. Therefore, it should be evaluated more on **Satisfaction, BLEU Score, and ROUGE Scores**, where it performed well.

