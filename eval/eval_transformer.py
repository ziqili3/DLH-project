#author Ziqi Li


from eICU_preprocessing.split_train_test import create_folder
from models.run_transformer import BaselineTransformer
from models.initialise_arguments import initialise_transformer_arguments
from models.final_experiment_scripts.best_hyperparameters import best_transformer


def eval_transformer():
    c = initialise_transformer_arguments()
    c['exp_name'] = 'Transformer'
    c['dataset'] = 'eICU'
    c = best_transformer(c)

    #store the output to output-test-transformer folder

    log_folder_path = create_folder('output/ziqi-experiments-test/', c.exp_name)
    transformer = BaselineTransformer(config=c,
                                      n_epochs=c.n_epochs,
                                      name=c.exp_name,
                                      base_dir=log_folder_path,
                                      explogger_kwargs={'folder_format': '%Y-%m-%d_%H%M%S{run_number}'})
    transformer.run_test()