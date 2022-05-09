#author Ziqi Li 

from eICU_preprocessing.split_train_test import create_folder
from models.run_tpc import TPC
from models.initialise_arguments import initialise_tpc_arguments
from models.final_experiment_scripts.best_hyperparameters import best_tpc

def train_tpc():

    c = initialise_tpc_arguments()
    c['exp_name'] = 'TPC'
    c['dataset'] = 'eICU'
    c = best_tpc(c)

    #store the output to output-train-tpc folder
    log_folder_path = create_folder('output/ziqi-experiments-train/', c.exp_name)
    tpc = TPC(config=c,
              n_epochs=c.n_epochs,
              name=c.exp_name,
              base_dir=log_folder_path,
              explogger_kwargs={'folder_format': '%Y-%m-%d_%H%M%S{run_number}'})
    tpc.run()