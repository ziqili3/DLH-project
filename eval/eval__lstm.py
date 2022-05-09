#author Ziqi Li

from eICU_preprocessing.split_train_test import create_folder
from models.run_lstm import BaselineLSTM
from models.initialise_arguments import initialise_lstm_arguments
from models.final_experiment_scripts.best_hyperparameters import best_lstm


def eval_lstm():
    c = initialise_lstm_arguments()
    c['exp_name'] = 'LSTM'
    c['dataset'] = 'eICU'
    c = best_lstm(c)

    #store the output to output-test-lstm folder

    log_folder_path = create_folder('output/ziqi-experiments-test/', c.exp_name)
    baseline_lstm = BaselineLSTM(config=c,
                                 n_epochs=c.n_epochs,
                                 name=c.exp_name,
                                 base_dir=log_folder_path,
                                 explogger_kwargs={'folder_format': '%Y-%m-%d_%H%M%S{run_number}'})
    baseline_lstm.run_test()