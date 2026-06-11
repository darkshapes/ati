---
name: ati
description: Standard parameter endpoint layer template for computer-led training
---

# Automated Training Inference


## Use When

- Limiting boilerplate and a single dependency is OK
- Making an entrypoint for Python model training
- Making an entrypoint for Python model inference

## Integrate

Use ATI for a project in one of the following ways:

```pyproject.toml
[dependencies]
...
"ati @ git+https://github.com/darkshapes/ati"
...
```

```py
>>> from ati import ATISettings                         # Import the template
>>> ati_set = ATISettings(steps=20,dtype="float16")     # Minimum arguments

>>> import torch
>>> import numpy as np
>>> ati_set_torch = ATISettings(steps=20,dtype=torch.float16)       # Framework agnostic
>>> ati_set_numpy = ATISettings(steps=20,dtype=np.dtype(np.float64))
```

```.env
steps=20
dtype="float16
```

```sh
<project_name>_ati_plug --steps 20 --dtype "float16"      # Replace <project_name> with the python project
```


## Parameter Options

```
abstain_threshold: float | None = None
additional_kwargs: dict[str, Any] | None = None
agent_prompt: str | None = None
alpha: float | None = None
attention_type: Any | None = None
cfg: float | None = None
checkpoint_path: str | None = None
colsample_bytree: float | None = None
column: str | None = None
condense_factor: int | None = None
cv: int | None = None
d_matrix_test: Any | None = None
dataset_path: str | None = None
dim_factor: int | None = None
disable_nullable: bool | None = None
early_stopping_rounds: int | None = None
eval_metric: list | None = None
export_model_path: str | None = None
feat_ext_path: str | None = None
feature_matrix: Any | None = None
gamma: str | None = None
gradient_accumulation: int | None = None
guider: str | None = None
inference_batch_size: int | None = None
inference_cfg: float | None = None
inference_steps: int | None = None
iterations: int | None = None
jit_type: bool | None = None
kernel: str | None = None
labels: Any | None = None
layers: int | None = None
load_from_cache_file: bool | None = None
load_onnx: bool | None = None
magnitude_sampling: bool | None = None
max_depth: int | None = None
max_rnd: int | None = None
method: str | None = None
mlp_activation: str | None = None
mlp_hidden_layers: int | None = None
mlp_max_iter: int | None = None
model_type: Any | None = None
n_components: float | None = None
negative_prompt: str | None = None
num_boost_round: int | None = None
num_features: int | None = None
number_folds: int | None = None
objective: str | None = None
pca: Any | None = None
positive_prompt: str | None = None
prompt: str | None = None
samples_path: str | None = None
scale_pos_weight: float | None = None
split: str | None = None
subsample: float | None = None
svm_c: int | None = None
system_prompt: str | None = None
t_eps: float | None = None
temperature: int | None = None
test_size: float | None = None
top_k: int | None = None
train_rounds: int | None = None
verbose_eval: int | None = None
wildcard_prompt: str | None = None
X_train_pca: Any | None = None
X_train: Any | None = None
y_test: Any | None = None
batch_size: int | None = None
condition_dimension: int | None = None
cooldown: int | None = None
dtype: str | Any
epochs: int | None = None
head_dimension: int | None = None
hidden_dimension: int | None = None
input_dimension: int | None = None
learning_rate: float | None = None
patch_size_2d: tuple[int, int] | None = None
patch_size: int | None = None
resolution: int | None = None
seed: int | None = 0
steps: int
time_dimension: int | None = None
warmup: int | None = None
```