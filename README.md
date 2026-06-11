# Automated Training Interface

## About

ATI is a standard endpoint layer for computer-led training and inference parameters. Its objective is to abstract away the

## Integrate

Add to an existing Python project

```py
>>> from ati import ATISettings                         # Import the template
>>> ati_set = ATISettings(steps=20,dtype="float16")     # Minimum arguments

>>> import torch
>>> import numpy as np
>>> ati_set_torch = ATISettings(steps=20,dtype=torch.float16)       # Framework agnostic
>>> ati_set_numpy = ATISettings(steps=20,dtype=np.dtype(np.float64))
```

## From an Environment File

```.env
steps=20
dtype="float16
```

## CLI

```sh
template_ati_plug --steps 20 --dtype "float16"      # Same as above
```

To add an ati_plug to your project:

```sh
<your_project_name>_ati_plug --steps 20 --dtype "float16"      # Fill with your project's name
```

## "Agentic" Harness

Use autonomously via [`.agents/skills/ati/SKILL.md`](.agents/skills/ati/SKILL.md)
