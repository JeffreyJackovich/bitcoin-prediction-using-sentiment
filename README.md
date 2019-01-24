Bitcoin Price Prediction using Sentiment Analysis  
=================================================================

### Jeffrey Jackovich
### October, 2018
<br><br>
# Contents
<div>
    <ul>1. <a href="https://github.com/JeffreyJackovich/bitcoin-prediction-with-sentiment#1-introduction">Introduction</a></ul>
    <ul><ul>1.1 Sentiment Analysis</ul></ul>
    <ul><ul>1.2 Twitter</ul></ul>
    <ul>2. <a href="https://github.com/JeffreyJackovich/bitcoin-prediction-with-sentiment#2-methodology">Methodology</a></ul>
      <ul><ul>2.1 Stock Price Dataset</ul></ul>
      <ul><ul>2.2 Technical Indicator</ul></ul>
      <ul><ul>2.3 Tweet source</ul></ul>
      <ul><ul>2.4 Tweet's Pre-Processing</ul></ul>
    <ul>3. <a href="https://github.com/JeffreyJackovich/bitcoin-prediction-with-sentiment#3-results">Results</a></ul>
   
</div>

## 1. Introduction:  

###  1.1  Sentiment Analysis

Sentiment Analysis refers to the use of text analysis and natural language
processing to identify and extract subjective information in textual contents.
There are two type of user-generated content available on the web - facts and
opinions. Facts are statements about topics and in the current scenario,
easily collectible from the Internet using search engines that index documents
based on topic keywords. Opinions are user specific statement exhibiting
positive or negative sentiments about a certain topic. Generally opinions are
hard to categorize using keywords. Various text analysis and machine learning
techniques are used to mine opinions from a document [1]

**Financial Markets**
     Public opinion regarding companies can be used to predict performance of their stocks in the financial markets. If people have a positive opinion about a product that a company A has launched, then the share prices of A are likely to go higher and vice versa. Public opinion can be used as an additional feature in existing models that try to predict market performances based on historical data. 
     
###  1.2  Twitter
Twitter is an online social networking and micro-blogging service that enables
users to create and read short messages, called "Tweets". It is a global forum
with the presence of eminent personalities from the field of entertainment,
industry and politics. From the perspective of Sentiment
Analysis, we discuss a few characteristics of Twitter:

## 2. Technologies:
Programming Language: Python
Libraries: Pandas, Matplotlib, Scikit-learn, TensorFlow
 
## 3. Methodology: 
I used Twitter's querysearch option for the phrase: 'bitcoin'.

### 3.1 Tweet data source:
<ul>b. <a href="https://github.com/Jefferson-Henrique/GetOldTweets-python">GetOldTweets-python</a></ul>

### 3.2 Tweet's Pre-Processing 
<ul><a href="https://github.com/JeffreyJackovich/bitcoin-prediction-with-sentiment/blob/master/tweet_pre-processing.ipynb">Tweets pre-processing</a></ul>


## References:

[1] Bo Pang and Lillian Lee. Opinion mining and sentiment analysis. _Foundations and trends in information retrieval_, 2(1-2):pages 1-135, 2008. 

[2] Empson, Rip. "Twitter Launches Clickable Stock Symbols, StockTwits' Howard Lindzon Says 'Hey, We Already Do That!'" TechCrunch, TechCrunch, 30 July 2012, techcrunch.com/2012/07/30/twitter-clickable-ticker-symbols/.

[3] Bollen, Johan, et al. "Twitter Mood Predicts the Stock Market." Twitter Mood Predicts the Stock Market., 14 Oct. 2010, pp. 1-8., arxiv.org/pdf/1010.3003.pdf.