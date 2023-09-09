#!/Users/brookelove/opt/miniconda3/envs/moneymodel01/bin/python

import matplotlib.pyplot as plt
import seaborn as sns

from money_model import MoneyModel


all_wealth = []
print("Money Model")
# Running the model 100 times with model executing 10 steps
for j in range(100):
    # Run the model
    model = MoneyModel(10)
    for i in range(10):
        model.step()

    for agent in model.schedule.agents:
        all_wealth.append(agent.wealth)

g = sns.histplot(all_wealth, discrete=True)
g.set(title="Wealth distribution", xlabel="wealth", ylabel="Number of Agents")

plt.show()
