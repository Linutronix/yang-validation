<!--
SPDX-FileCopyrightText: 2024 Linutronix GmbH
SPDX-License-Identifier: 0BSD
-->

# Scripts for YANG Validation

`collect_testcase.py`: Call without parameters in the root directory to collect all testcases and print them as JSON array. Used in the GitHub action to generate the corresponding jobs.

`validate.py <testcase>`: Call with a YAML testcase specification to run the testcase by parsing it and forwarding it to `yanglint`.
