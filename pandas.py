import pandas as pd
data_c = [
{'A': 5, 'B': 0, 'C': 3, 'D': 3},
{'A': 7, 'B': 9, 'C': 3, 'D': 5},
{'A': 2, 'B': 4, 'C': 7, 'D': 6}]

pd.DataFrame.from_dict(data_c, orient='columns')
