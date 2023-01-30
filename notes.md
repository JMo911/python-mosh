pypi.org -> open source packages we can use
pip

- machine learning
  - write a program to scan an image and tell if it's a cat or a dog.. will get overly complex.. lots of rules.. if photo goes black & white or changes angles, it'll break...
  - cats dogs & horses.. once again will break and you need to rewrite
    build a model/engine and give it lots of data (millions of photos).. it finds patterns in the input data.. then it'll give us the correct answer X% of the time..
  - steps:
    1. import the data
    2. clean the data (remove dupes, irrelevant data types, etc)
    3. split the data into training/test sets.. ensure the model produces the right result..
    4. create a model - algorithm to analyze the data.. decision tress/neural networks/etc.. depends on the type of problem and your input data. (psychic learn)
    5. train the model
    6. make predictions (probably inaccurate at first)
    7. evaluate and improve.. fine tune params, or change algorithm.
  - libraries:
    - numpy -> multidimensional array
    - pandas -> data frame 2d data structure.. rows and columns..
    - matplotlib -> 2d plotting library for graphs and plots
    - scikit learn -> machine learning.. decision trees, neural networks, etc
  - jupyter:
    - frequently inspect the data
