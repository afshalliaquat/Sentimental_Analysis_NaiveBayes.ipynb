<h1>📊 Sentiment Analysis using Logistic Regression</h1>

<h2>📖 Project Background</h2>

<p>
This project focuses on building a sentiment analysis model using classical machine learning techniques on textual data. The goal was to classify text into <strong>positive</strong> or <strong>negative</strong> sentiment based on its content. Starting from raw data, the complete NLP pipeline was implemented from exploratory data analysis to model evaluation.
</p>

<h3>🧹 Preprocessing & Vectorization</h3>
<p>
The text data was cleaned through preprocessing steps such as lowercasing, punctuation removal, stopword filtering, and tokenization. Two vectorization methods were applied to transform the textual data into numerical form:
</p>
<ul>
  <li><strong>Bag of Words (CountVectorizer)</strong></li>
  <li><strong>TF-IDF (Term Frequency–Inverse Document Frequency)</strong></li>
</ul>

<h3>🤖 Model Comparison</h3>
<p>
Multiple machine learning algorithms were tested using both vectorization techniques. After extensive comparison, <strong>Logistic Regression with CountVectorizer (BoW)</strong> stood out as the best-performing model.
</p>

<ul>
  <li>✅ Achieved <strong>90% accuracy</strong> and a high F1-score</li>
  <li>✅ Consistent performance across all sentiment classes</li>
  <li>✅ Performed well even <strong>without hyperparameter tuning</strong></li>
</ul>

<p>
Additionally, experimentation was conducted using TF-IDF with hyperparameter tuning via <code>GridSearchCV</code> and <code>RandomizedSearchCV</code>. Although the tuned TF-IDF models performed well, the untuned BoW model produced comparable results with less complexity.
</p>

<h3>🧠 Key Learnings</h3>
<p>
Through this project, the following skills and concepts were reinforced:
</p>
<ul>
  <li><em>NLP preprocessing</em> and text normalization techniques</li>
  <li>Comparing <strong>BoW</strong> vs. <strong>TF-IDF</strong> for feature extraction</li>
  <li>Evaluating models using classification metrics: <strong>accuracy, precision, recall, F1-score</strong></li>
  <li>Performing <strong>hyperparameter tuning</strong> with GridSearchCV and RandomizedSearchCV</li>
  <li>Choosing the right model for a <strong>real-world NLP application</strong></li>
</ul>

<p>
Overall, this project serves as a strong baseline for future work in sentiment analysis, showcasing how classical methods can still be effective with the right preprocessing and evaluation strategy.
</p>
