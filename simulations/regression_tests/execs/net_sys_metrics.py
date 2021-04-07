from pprint import pprint

import pandas as pd
from tabulate import tabulate

from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from simulations.regression_tests.experiments import combo_exp
from simulations.regression_tests.models import config_multi_1, param_sweep
# print()
# pprint([c.__dict__['user_id'] for c in config_multi_1.combo_exp.configs])
# print()
# pprint([c.__dict__['user_id'] for c in config_multi_1.multi_exp.configs])
# from simulations.regression_tests.models.config_multi_1 import multi_exp

exec_mode = ExecutionMode()

local_proc_ctx = ExecutionContext(context=exec_mode.local_mode)
run = Executor(exec_context=local_proc_ctx, configs=combo_exp.configs)

# print()
# pprint(config_multi_1.multi_exp.configs)
# print()
# pprint(config_multi_1.combo_exp.configs)

raw_result, tensor_fields, sessions = run.execute()
result = pd.DataFrame(raw_result)
# print(tabulate(tensor_fields[0], headers='keys', tablefmt='psql'))
# # pprint(sessions)
print(tabulate(result, headers='keys', tablefmt='psql'))

# pprint([config.__dict__ for config in config_multi_1.combo_exp.configs])