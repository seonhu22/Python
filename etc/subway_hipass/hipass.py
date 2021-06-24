import string
import random
import pandas as pd

MAX_LEN = 8

random_id = string.ascii_letters + string.digits

id = []
for i in range(100000):
    result = ""
    for i in range(MAX_LEN):
        if i == 4:
            result += "-"
        result += random.choice(random_id)
    id.append(result)

id_data = pd.DataFrame(id)
