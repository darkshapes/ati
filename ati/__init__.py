# SPDX-License-Identifier: MPL-2.0 AND LicenseRef-Commons-Clause-License-Condition-1.0
# <!-- // /*  d a r k s h a pes */ -->

from typing import Any
import pydantic_settings as pyds


class ATISettings(pyds.BaseSettings):
    # Base
    steps: int
    dtype: str | Any
    seed: int | None = 0
    learning_rate: float | None = None
    cooldown: int | None = None
    warmup: int | None = None
    epochs: int | None = None

    # Dimensions
    batch_size: int | None = None
    condition_dimension: int | None = None
    head_dimension: int | None = None
    hidden_dimension: int | None = None
    input_dimension: int | None = None
    patch_size_2d: tuple[int, int] | None = None
    patch_size: int | None = None
    resolution: int | None = None
    time_dimension: int | None = None

    # Layers
    iterations: int | None = None
    layers: int | None = None
    mlp_activation: str | None = None
    mlp_hidden_layers: int | None = None

    # Paths
    checkpoint_path: str | None = None
    dataset_path: str | None = None
    export_model_path: str | None = None
    feat_ext_path: str | None = None
    samples_path: str | None = None

    # Factoring
    condense_factor: int | None = None
    dim_factor: int | None = None

    # Datasets
    column: str | None = None
    split: str | None = None
    X_train: Any | None = None
    y_test: Any | None = None

    # XGB
    alpha: float | None = None
    colsample_bytree: float | None = None
    early_stopping_rounds: int | None = None
    max_rnd: int | None = None
    n_components: float | None = None
    num_boost_round: int | None = None
    subsample: float | None = None
    test_size: float | None = None
    train_rounds: int | None = None
    d_matrix_test: Any | None = None
    feature_matrix: Any | None = None
    pca: Any | None = None
    X_train_pca: Any | None = None
    max_depth: int | None = None
    objective: str | None = None

    # Evaluation
    eval_metric: list | None = None
    verbose_eval: int | None = None

    # Inference
    inference_batch_size: int | None = None
    inference_steps: int | None = None
    inference_cfg: float | None = None
    prompt: str | None = None
    system_prompt: str | None = None
    positive_prompt: str | None = None
    negative_prompt: str | None = None
    wildcard_prompt: str | None = None
    agent_prompt: str | None = None

    # misc toggle
    disable_nullable: bool | None = None
    jit_type: bool | None = None
    load_from_cache_file: bool | None = None
    load_onnx: bool | None = None
    magnitude_sampling: bool | None = None

    # misc int
    cv: int | None = None
    gradient_accumulation: int | None = None
    mlp_max_iter: int | None = None
    num_features: int | None = None
    number_folds: int | None = None
    svm_c: int | None = None
    temperature: int | None = None
    top_k: int | None = None

    # misc float
    abstain_threshold: float | None = None
    scale_pos_weight: float | None = None
    t_eps: float | None = None
    cfg: float | None = None

    # misc string
    gamma: str | None = None
    kernel: str | None = None
    method: str | None = None
    guider: str | None = None

    # misc
    labels: Any | None = None
    model_type: Any | None = None
    attention_type: Any | None = None

    additional_kwargs: dict[str, Any] | None = None


def main(**kwargs):
    ati_settings = ATISettings(**kwargs)
    return ati_settings


if __name__ == "__main__":
    main()
