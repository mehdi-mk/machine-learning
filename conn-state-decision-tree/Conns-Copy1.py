#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
conns = pd.read_csv("conns_selected_ML_2022-11-30_10hr-19hr_1mil_intIPs.csv")
conns.head()


# In[4]:


y = conns[['state']]


# In[5]:


x = conns[conns.columns.drop('state').tolist()]


# In[6]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, stratify = y, random_state = 1234)


# In[8]:


x_train = pd.get_dummies(x_train)


# In[9]:


x_test = pd.get_dummies(x_test)


# In[10]:


from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(random_state = 1234)


# In[11]:


model = classifier.fit(x_train, y_train)


# In[17]:


from sklearn.model_selection import GridSearchCV
grid_param = {"criterion": ["gini", "entropy"],
              "splitter": ["best", "random"],
              "max_depth":range(2, 50, 1),
              "min_samples_leaf": range(1, 15, 1),
              "min_samples_split": range(2, 20, 1)
              }
grid_search = GridSearchCV(estimator = classifier, param_grid = grid_param, cv = 5, n_jobs = -1)
grid_search.fit(x_train, y_train)
print(grid_search.best_param_)

