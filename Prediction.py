#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from keras.models import load_model


# In[2]:


model = load_model("./static/my_perfect_model.h5")


# In[9]:
def get_pred(image):
    img = cv2.imread(image)
    img = cv2.resize(img,(100,100))
    img = np.array(img)
    img = img.reshape((1,100,100,3))
    pred = model.predict(img).argmax()
    return pred

# In[13]:





# In[ ]:





# In[ ]:





# In[ ]:




