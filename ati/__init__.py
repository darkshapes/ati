# SPDX-License-Identifier: MPL-2.0 AND LicenseRef-Commons-Clause-License-Condition-1.0
# <!-- // /*  d a r k s h a pes */ -->

from typing import Any
import pydantic_settings as pyds


class ATISettings(pyds.BaseSettings):
    # Training
    steps: int
    data_type: str | Any
    seed: int | None = 0
    epochs: int | None = None
    learning_rate: float | None = None
    warmup: int | None = None
    cooldown: int | None = None
    gradient_accumulation: int | None = None
    batch_size: int | None = None

    # Architecture
    input_dimension: int | None = None
    hidden_dimension: int | None = None
    condition_dimension: int | None = None
    head_dimension: int | None = None
    time_dimension: int | None = None
    patch_size: int | None = None
    patch_size_2d: tuple[int, int] | None = None
    resolution: int | None = None
    layers: int | None = None
    iterations: int | None = None
    condense_factor: int | None = None
    dimension_factor: int | None = None
    attention_type: Any | None = None
    model_type: Any | None = None

    # MLP
    mlp_activation: str | None = None
    mlp_hidden_layers: int | None = None
    mlp_max_iterations: int | None = None

    # Data
    dataset_path: str | None = None
    column: str | None = None
    split: str | None = None
    test_size: float | None = None
    train_features: Any | None = None
    test_labels: Any | None = None
    labels: Any | None = None
    number_features: int | None = None
    load_from_cache_file: bool | None = None

    # Classical ML
    method: str | None = None
    cross_validation: int | None = None
    number_folds: int | None = None
    scale_positive_weight: float | None = None
    abstain_threshold: float | None = None

    # SVM
    kernel: str | None = None
    gamma: str | None = None
    support_vector_machine_cost: int | None = None

    # PCA
    number_components: float | None = None
    principal_component_analysis: Any | None = None
    train_features_reduced: Any | None = None

    # XGBoost
    objective: str | None = None
    alpha: float | None = None
    colsample_bytree: float | None = None
    subsample: float | None = None
    max_depth: int | None = None
    max_random: int | None = None
    number_boost_round: int | None = None
    train_rounds: int | None = None
    early_stopping_rounds: int | None = None
    eval_metric: list | None = None
    verbose_eval: int | None = None
    feature_matrix: Any | None = None
    test_matrix: Any | None = None

    # Inference
    inference_batch_size: int | None = None
    inference_steps: int | None = None
    inference_guidance_scale: float | None = None
    guidance_scale: float | None = None
    guider: str | None = None
    temperature: int | None = None
    top_k: int | None = None
    time_epsilon: float | None = None
    magnitude_sampling: bool | None = None

    # Prompting
    prompt: str | None = None
    system_prompt: str | None = None
    positive_prompt: str | None = None
    negative_prompt: str | None = None
    wildcard_prompt: str | None = None
    agent_prompt: str | None = None

    # Paths
    checkpoint_path: str | None = None
    export_model_path: str | None = None
    feature_extractor_path: str | None = None
    samples_path: str | None = None

    # Runtime
    just_in_time: bool | None = None
    load_onnx: bool | None = None
    disable_nullable: bool | None = None

    additional_kwargs: dict[str, Any] | None = None


def main(**kwargs):
    ati_settings = ATISettings(**kwargs)
    return ati_settings


if __name__ == "__main__":
    main()
