# %%
import numpy as np

from hdsemg_force_regression.hyser import hyser as hy
from hdsemg_force_regression.protocol import protocol

# %%
# LIF

# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #

# GAINS

GAIN_PER_VOLT_LIST = [
    05.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0,
]

# ALPHAS

ALPHA_LIST = [0.1, 10.0**-1.5, 0.01]
NUM_ALPHAS = len(ALPHA_LIST)
ALPHA_LABELS = ['aminus1', 'amiddle', 'aminus2']
assert len(ALPHA_LABELS) == NUM_ALPHAS

# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #

X_INIT = 0.0
X_RESET = 0.5      # Kubanek: 0.5 (i.e., -65.0mV in his units)
TAUPRE_S = 0.010      # Kubanek: 10ms
TREFR_S = 0.002    # Kubanek:  2ms; Elisa: do not go above 2ms.
# ADD THE OPTIMAL VALUES I FOUND IN THE IWASI 2023 PAPER
TAUPOST_S = 0.250  # 0.500

# SIMULATION

DT_SIM_S = 1.0 / hy.FS_HDSEMG
DT_MONITORS_PRE_S = DT_SIM_S  # pre-synaptic
DT_MONITORS_POST_S = 1.0 / hy.FS_FORCE  # DT_SIM_S  # post-synaptic
REPORT_STDSTREAM = 'stdout'
REPORT_PERIOD_S = 5.0

# REGRESSION

DOWNSAMP = 1

# %%
# protocol.protocol_on_single_subject(idx_subject=0)

for idx_alpha in range(NUM_ALPHAS):

    alpha = ALPHA_LIST[idx_alpha]
    alpha_label = ALPHA_LABELS[idx_alpha]

    for gain_per_volt in GAIN_PER_VOLT_LIST:

        print("\n----------------------------------------------------------\n")
        print("\n----------------------------------------------------------\n")
        print("\n----------------------------------------------------------\n")
        print("\n----------------------------------------------------------\n")
        print("\n")
        print(f"\nCURRENT GAIN:\t{gain_per_volt :02.0f}/V\n")
        print('\n', gain_per_volt, '\n')
        print("\n")
        print("\n----------------------------------------------------------\n")
        print("\n----------------------------------------------------------\n")
        print("\n----------------------------------------------------------\n")
        print("\n----------------------------------------------------------\n")

        RESULTSFILE_PATH = \
            f"./retest_{alpha_label}_gain_{gain_per_volt :02.0f}.pkl"

        protocol.regression_experiment_on_every_subject(

            results_dict_dst_filepath=RESULTSFILE_PATH,

            gain_per_volt=gain_per_volt,
            x_init=X_INIT,
            x_reset=X_RESET,
            taupre_s=TAUPRE_S,
            trefr_s=TREFR_S,
            taupost_s=TAUPOST_S,
            dt_sim_s=DT_SIM_S,
            dt_monitors_pre_s=DT_MONITORS_PRE_S,
            dt_monitor_post_s=DT_MONITORS_POST_S,
            report_stdstream=REPORT_STDSTREAM,
            report_period_s=REPORT_PERIOD_S,

            downsamp=DOWNSAMP,
            alpha=alpha,
        )
