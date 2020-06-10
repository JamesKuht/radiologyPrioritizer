#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# ## Worklist prioritization: Emergency Setting

# In[2]:


## First, read in the file of the current worklist with the probabilities that your two algorithms have
## generated for the two types of findings you're most concerned with:

worklist = pd.read_csv('probabilities.csv')


# In[3]:


worklist.head()


# In[7]:


##Calculate the amount of time it will take before each image is read by the radiologist, given the patient 
##arrival queue, assuming each image takes 6 minutes to read

worklist['time to read scan'] = np.arange(6, 6*(len(worklist)+1), 6)

worklist.head()


# In[8]:


##Implement a heuristic that uses the probabilities returned by your two algorithms to re-order the priority read 
##list, assuming that brain bleeds and aortic dissections are equally urgent

worklist['Max prob'] = worklist[["Brain_bleed_probability", "Aortic_dissection_probability"]].max(axis=1)

worklist.head()


# In[17]:


worklist_prioritized = worklist.sort_values("Max prob",ascending = False)

worklist_prioritized.head()


# In[20]:


##Calculate the time delta for each image between the initial and the re-ordered priority reads

worklist_prioritized['revised time to read scan'] = np.arange(6, 6*(len(worklist)+1),6)

worklist_prioritized.head()


# In[24]:


worklist_prioritized['time_delta'] = worklist_prioritized["revised time to read scan"] - worklist_prioritized["time to read scan"]

worklist_prioritized.head()


# In[34]:


##If your algorithm's goal was to have brain bleeds read 30 minutes faster, how did it do?

worklist_prioritized[((worklist_prioritized.time_delta <= -30)&(worklist_prioritized.Image_Type == 'head_ct'))]


    


# In[35]:


worklist_prioritized[((worklist_prioritized.time_delta <= -15)&(worklist_prioritized.Image_Type == 'chest_xray'))]


# In[ ]:




