<!--
SPDX-FileCopyrightText: 2024 Linutronix GmbH
SPDX-License-Identifier: 0BSD
-->

# YANG Validation

Collection of YANG instance files for automated validation against YANG models.

## Pipeline

[![Daily Validation](https://github.com/Linutronix/yang-validation/actions/workflows/validate.yml/badge.svg?branch=main&event=schedule)](https://github.com/Linutronix/yang-validation/actions/workflows/validate.yml)

All testcases are executed daily with the most recent master version of https://github.com/CESNET/libyang as well as the most recent main of https://github.com/YangModels/yang to get notified early about any upcoming issues.

## Structure
`models` is a submodule containing https://github.com/YangModels/yang

`scripts` contains a few Python scripts useful for validation

`.github/workflows` contains the instructions for the automated pipeline

`LICENSES` contains the relevant licenses for this repository, see the license section below.

All other directories contain the actual testcases (ending with `testcase.yaml`) and the corresponding instance files for these testcases.

## Contributions

If you find it useful to have YANG instance files automatically and regularly checked against YANG models, we are happy to accept your contribution to this repository.

## License
The scripts and testcases can be easily reused under the terms of the "BSD Zero Clause License". For the YANG models specific licenses may apply (see the corresponding `.license` files and also https://github.com/YangModels/yang?tab=readme-ov-file#license-notes).

The repository is [REUSE](https://reuse.software/) compliant which is checked by a corresponding pipeline: [![REUSE Compliance](https://github.com/Linutronix/yang-validation/actions/workflows/reuse.yml/badge.svg?event=push)](https://github.com/Linutronix/yang-validation/actions/workflows/reuse.yml)

