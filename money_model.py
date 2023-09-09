# Seaborrn data visualization tools.
# Numpy Has multi-dimensional arrays and matrices. Has a large collection of
# mathematical functions to operate on these arrays.
# Pandas data manipulation and analysis.

import mesa
import seaborn as sns
import numpy as np
import pandas as pd


'''
    - agents are entities that act in the model 
    - in this model are ind. that exchange money
    - A model is a visualized grid for all the agents
    - the scheduler controls the order in which agents are activated caused the agents to take their defined action
'''


class MoneyAgent(mesa.Agent):
    '''An agent with fixed wealth initally.'''

    def __init__(self, unique_id, model):
        # parameters to the parent class
        super().__init__(unique_id, model)

        # create the agent variable and set inital value
        self.wealth = 1

    def step(self):
        if self.wealth > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent is not None:
                other_agent.wealth += 1
                self.wealth -= 1
        # The agent's step will go here.
        # For demonstration purposes we will print the agent's unique_id
        print(
            f"Hi, I am an agent, you can call me {str(self.unique_id)}. I have {str(self.wealth)} in wealth")


class MoneyModel(mesa.Model):
    '''A model with some number of agents'''

    def __init__(self, N):
        self.num_agents = N
        # create scheduler and assign it to the model
        self.schedule = mesa.time.RandomActivation(self)  # random activation

        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            # the agent to the scheduler
            self.schedule.add(a)

    def step(self):
        """Advance the model by one step"""
        # The model's step will go here for now this will call the step method of each agent and print the agent's unique_id
        self.schedule.step()
