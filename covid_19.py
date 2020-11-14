import covsirphy as cs
from pprint import pprint
# Download datasets
data_loader = cs.DataLoader("input")
jhu_data = data_loader.jhu()
population_data = data_loader.population()
# Check records
snl = cs.Scenario(jhu_data, population_data, country="China")
a = 1
for line in snl.records().Date:
    print(line)
    a += 1
