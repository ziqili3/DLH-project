# CS598 Final Project
writer: Ziqi Li, Ruikang Zhao
email: ziqili3@illinois.edu, zuikang2@illinois.edu

## Citation to original paper
as given be the original author, the citation is :
```bibtex
@inproceedings{rocheteau2021,
author = {Rocheteau, Emma and Li\`{o}, Pietro and Hyland, Stephanie},
title = {Temporal Pointwise Convolutional Networks for Length of Stay Prediction in the Intensive Care Unit},
year = {2021},
isbn = {9781450383592},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3450439.3451860},
doi = {10.1145/3450439.3451860},
booktitle = {Proceedings of the Conference on Health, Inference, and Learning},
pages = {58–68},
numpages = {11},
keywords = {intensive care unit, length of stay, temporal convolution, mortality, patient outcome prediction},
location = {Virtual Event, USA},
series = {CHIL '21}
}
```

## Link to the original paper's repo
https://github.com/EmmaRocheteau/TPC-LoS-prediction


## Dependencies

The dependencies needed are all listed in requirements.txt.
```shell
numpy==1.18.1
pandas==0.24.2
scipy==1.4.1
torch==1.5.0
trixi==0.1.2.2
scikit-learn==0.20.2
captum==0.2.0
shap==0.35.0
```
Keep in mind that the version of python should be python3 and higher than 3.6.

### Data download instruction

Data used here is eICU dataset provided by pyhsionet, 
official link is :https://physionet.org/content/eicu-crd/2.0/.

For one to be able to download eICU data from pyhsionet, the user account needed to have credential, training report uploaded and agreement signed.

### Preprocessing

Before data preprocessing, it is needed to set-up eICU dataset. 

Follow the instructions: https://eicu-crd.mit.edu/tutorials/install_eicu_locally/ to ensure the correct connection configuration.

Also, we found out that the build-db code from https://github.com/MIT-LCP/eicu-code may be helpful.

Replace the eICU_path in paths.json to the path to eICU dataset(on my PC it is '/Users/liziqi/sp22/cs598DLH/project/DLH-project/eICU_data_preprocessed/'), and do the same for eICU_preprocessing/create_all_tables.sql using find and replace for '/Users/liziqi/sp22/cs598DLH/project/DLH-project/eICU_data_preprocessed/'. Leave the extra '/' at the end.
```shell
#in the project root directory, do:
psql 'dbname=eicu user=eicu options=--search_path=eicu'

#in psql console, do:
\i eICU_preprocessing/create_all_tables.sql

#in project root directory, do:
python3 -m eICU_preprocessing.run_all_preprocessing
```


### Training

For training, simply run the following commands to train tpc,lstm and transformer from baseline models.
```shell
#in project root directory, do:

#to train tpc model
python3 ./train/train_tpc.py

#to train lstm model
python3 ./train/train_lstm.py

#to train transformer model
python3 ./train/train_transformer.py

#to train mean_median model
python3 ./train/train_mean_median.py

```

Note that all the models are trained based on the best model provided by author, if one want to train from just baseline model or any other pretrained model, minor changes should be made, just change the "config" parameter in model initialization step would be ok.

### Evaluation
For testing, simply run the following commands 
```shell
#in project root directory, do:

#to eval tpc model
python3 ./eval/eval_tpc.py

#to eval lstm model
python3 ./eval/eval_lstm.py

#to eval transformer model
python3 ./eval/eval_transformer.py
```


### Results

The result is not comming out yet, but we believe it would support our claim stated in final report.