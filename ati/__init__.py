# SPDX-License-Identifier: MPL-2.0 AND LicenseRef-Commons-Clause-License-Condition-1.0
# <!-- // /*  d a r k s h a pes */ -->

from typing import Any
import pydantic_settings as pyds


class ATISettings(pyds.BaseSettings):
    # Base
    steps: int
    dtype: str | Any
    seed: int | None = 0
    cooldown: int | None = None
    epochs: int | None = None
    learning_rate: float | None = None
    warmup: int | None = None

    # Dimensions
    attention_head_dimension: int | None = None
    axes_dimension: list | None = None
    batch_size: int | None = None
    condition_dimension: int | None = None
    context_in_dimension: int | None = None
    head_dimension: int | None = None
    height: int | None = None
    hidden_dimension: int | None = None
    in_channels: int | None = None
    input_dimension: int | None = None
    patch_size_2d: tuple[int, int] | None = None
    patch_size: int | None = None
    resolution: int | None = None
    speaker_embedding_dimension: int | None = None
    text_embedding_dimension: int | None = None
    time_dimension: int | None = None
    vector_in_dimension: int | None = None
    width: int | None = None

    # Layers
    depth: int | None = None
    iterations: int | None = None
    layers: int | None = None
    mlp_activation: str | None = None
    mlp_hidden_layers: int | None = None
    depth_single_blocks: int | None = None

    # Paths
    checkpoint_path: str | None = None
    dataset_path: str | None = None
    export_model_path: str | None = None
    feat_ext_path: str | None = None
    samples_path: str | None = None

    # Factoring
    condense_factor: int | None = None
    dimension_factor: int | None = None

    # Datasets
    column: str | None = None
    split: str | None = None
    X_train: Any | None = None
    y_test: Any | None = None

    # XGB
    alpha: float | None = None
    colsample_bytree: float | None = None
    d_matrix_test: Any | None = None
    early_stopping_rounds: int | None = None
    feature_matrix: Any | None = None
    max_depth: int | None = None
    max_rnd: int | None = None
    n_components: float | None = None
    num_boost_round: int | None = None
    objective: str | None = None
    pca: Any | None = None
    subsample: float | None = None
    test_size: float | None = None
    train_rounds: int | None = None
    X_train_pca: Any | None = None

    # Evaluation
    eval_metric: list | None = None
    verbose_eval: int | None = None

    # Inference
    agent_prompt: str | None = None
    inference_batch_size: int | None = None
    inference_cfg: float | None = None
    inference_steps: int | None = None
    negative_prompt: str | None = None
    positive_prompt: str | None = None
    prompt: str | None = None
    system_prompt: str | None = None
    wildcard_prompt: str | None = None

    # misc toggle
    disable_nullable: bool | None = None
    guidance_embed: bool | None = None
    jit_type: bool | None = None
    load_from_cache_file: bool | None = None
    load_onnx: bool | None = None
    magnitude_sampling: bool | None = None
    qkv_bias: bool | None = None
    shift: bool | None = None

    # misc int
    block_length: int | None = None
    cv: int | None = None
    gradient_accumulation: int | None = None
    mask_id: int | None = None
    max_position_embeddings: int | None = None
    max_position: int | None = None
    max_text_length: int | None = None
    mlp_max_iter: int | None = None
    num_attention_heads: int | None = None
    num_features: int | None = None
    number_folds: int | None = None
    svm_c: int | None = None
    temperature: int | None = None
    top_k: int | None = None

    # misc float
    abstain_threshold: float | None = None
    cfg: float | None = None
    mlp_ratio: float | None = None
    rope_theta: float | None = None
    scale_pos_weight: float | None = None
    t_eps: float | None = None

    # misc string
    cfg_type: str | None = None
    gamma: str | None = None
    guider: str | None = None
    kernel: str | None = None
    method: str | None = None
    remasking_strategy: str | None = None
    scheduler_type: str | None = None

    # misc
    additional_kwargs: dict[str, Any] | None = None
    attention_type: Any | None = None
    labels: Any | None = None
    model_type: Any | None = None


def main(**kwargs):
    ati_settings = ATISettings(**kwargs)
    return ati_settings


if __name__ == "__main__":
    main()
