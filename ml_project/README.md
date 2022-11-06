# Simple cookiecutter-template project

## Generate EDA report

#### 1. Enter virtual environment with specified requierements
```
python3 -m venv test_venv
source test_venv/bin/activate
pip install -r requierements.txt
```

#### 2. You can configure some report settings in `configs/profile.py` file

#### 3. Run the following code from `ml_project` directory:

```
./src/visualization/generate_report.py 
```
#### 4. Check your EDA Profiling report in `reports/` directory



## Train model

#### 1. **(Skip this step if you do it on previous usecase)** Enter virtual environment with specified requierements.
```
python3 -m venv test_venv
source test_venv/bin/activate
pip install -r requierements.txt
```

#### 2. You are ready to go. Just run the train pipeline with one of the sample configs or configure it by yourself. For example if you want to train model using `train_config_1.yaml` example. From `ml_project` directory run:
```
./src/models/train_model.py hydra.job.chdir=False -cn train_config_1
```

## Make predictions

#### 1. **(Skip this step if you do it on previous usecase)** Enter virtual environment with specified requierements
```
python3 -m venv test_venv
source test_venv/bin/activate
pip install -r requierements.txt
```
#### 2. To use artifacts from previous usecase: from `ml_project` directory run:
```
./src/models/predict_model.py hydra.job.chdir=False test_path=<path to you dataset> transformer_path=<path to feature transformer> prediction_path=<path to prediction to be saved> classifier_path=<path to your classifier>
```

For example to use artifacts from previous usecase you can run:
```
./src/models/predict_model.py hydra.job.chdir=False test_path=data/processed/test.csv transformer_path=models/transformer.dill prediction_path=data/processed/preds.csv classifier_path=models/classifier.dill

```

