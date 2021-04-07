#!/usr/bin/env python
# coding: utf-8

# In[1]:


# get_ipython().run_line_magic('load_ext', 'autoreload')
# get_ipython().run_line_magic('autoreload', '2')
import time

from tabulate import tabulate

import cadCAD
cadCAD.__file__


# In[2]:


from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import Experiment
from cadCAD.engine import ExecutionMode, ExecutionContext
from cadCAD.engine import Executor

import pandas as pd


# In[3]:


system_params = {
    'add': [10]
}

initial_state = {
    'a': 0
}


# In[4]:


from numpy import random

def update_a(params, substep, state_history, previous_state, policy_input, **kwargs):
    return 'a', previous_state['a'] + params['add'] * random.rand()


# In[5]:


psubs = [
    {
        'policies': {},
        'variables': {
            'a': update_a
        }
    }
]


# In[6]:


# from cadCAD import configs
# del configs[:] # Clear any prior configs


# In[7]:


exp = Experiment()

sim_config = config_sim({
    "N": 3,
    "T": range(100),
    # "N": 1,
    # "T": range(2),
    "M": system_params
})
# print(sim_config)

exp.append_configs(
    initial_state = initial_state,
    partial_state_update_blocks = psubs,
    sim_configs = sim_config
)
# print(sim_config)


# In[8]:


exec_mode = ExecutionMode()
local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)

simulation = Executor(exec_context=local_mode_ctx, configs=exp.configs)

start_a = time.time()
raw_system_events, tensor_field, sessions = simulation.execute()
end_a = time.time()

time_a = end_a - start_a


# exec_mode.multi_proc
#
#
# # In[9]:
#
#
# sessions
#
#
# In[10]:


simulation_result = pd.DataFrame(raw_system_events)
simulation_result


# In[11]:


df = simulation_result.copy()


# In[12]:


a = df[df['run'] == 1].head()
print(tabulate(a, headers='keys', tablefmt='psql'))

# In[13]:


b = df[df['run'] == 2].head()
print(tabulate(b, headers='keys', tablefmt='psql'))

# In[14]:


c = df[df['run'] == 3].head()
print(tabulate(c, headers='keys', tablefmt='psql'))

#---

# In[15]:


system_params = {
    'add': [10,10,10]
}

initial_state = {
    'a': 0
}


# In[16]:

from numpy import random

def update_a(params, substep, state_history, previous_state, policy_input, **kwargs):
    return 'a', previous_state['a'] + params['add'] * random.rand()


# In[17]:


psubs = [
    {
        'policies': {},
        'variables': {
            'a': update_a
        }
    }
]


# In[18]:


# from cadCAD import configs
# del configs[:] # Clear any prior configs


# In[19]:


exp = Experiment()

sim_config = config_sim({
    "N": 3,
    "T": range(100),
    "M": system_params
})

exp.append_configs(
    initial_state = initial_state,
    partial_state_update_blocks = psubs,
    sim_configs = sim_config
)


# In[20]:


exec_mode = ExecutionMode()
local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)

simulation = Executor(exec_context=local_mode_ctx, configs=exp.configs)

start_b = time.time()
raw_system_events, tensor_field, sessions = simulation.execute()
end_b = time.time()

time_b = end_b - start_b

print()
print(abs(time_b - time_a))
print()
#
# print()
# print(time_a)
# print(time_b)

# In[21]:


sessions


# In[22]:


simulation_result = pd.DataFrame(raw_system_events)
simulation_result


# In[23]:


df = simulation_result.copy()


# In[24]:


d = df[df['run'] == 1].head()
print(tabulate(d, headers='keys', tablefmt='psql'))

# In[25]:


e = df[df['run'] == 2].head()
print(tabulate(e, headers='keys', tablefmt='psql'))

# In[26]:


f = df[df['run'] == 3].head()
print(tabulate(f, headers='keys', tablefmt='psql'))

# In[ ]:





# In[ ]:





# In[ ]:
