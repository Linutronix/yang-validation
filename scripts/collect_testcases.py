#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 Linutronix GmbH
# SPDX-License-Identifier: 0BSD

import os
import json

excluded = ["models", ".github"]


def collect_yaml_files(directory):
    yaml_files = []
    for base_directory in os.scandir(directory):
        if any(
            base_directory.name == exclude_directory for exclude_directory in excluded
        ):
            continue

        for root, dirs, files in os.walk(base_directory):
            for file in files:
                if file.endswith("testcase.yaml") or file.endswith("testcase.yml"):
                    yaml_files.append(os.path.join(root, file))

    return yaml_files


if __name__ == "__main__":
    yaml_files = collect_yaml_files(".")
    json_array = json.dumps(yaml_files)
    print(json_array)
