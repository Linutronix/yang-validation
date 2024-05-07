#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 Linutronix GmbH
# SPDX-License-Identifier: 0BSD

import sys
import yaml
import subprocess


def run_testcase(yaml_file):
    with open(yaml_file, "r") as f:
        config = yaml.safe_load(f)

    ## Find YAML modules
    yang_files = []

    for model in config["models"]:
        yang_files.append(model["file"])

    ## Run yanglint
    command = ["yanglint"] + yang_files + [config["instance"]]

    print(" ".join(command))

    result = subprocess.run(command)

    if result.returncode == 0:
        if config["expect_success"]:
            print("Successful as expected")
            return 0
        else:
            print("Successful, but was not expected")
            return 1
    else:
        if config["expect_success"]:
            print("Failed, but success was expected")
            return 1
        else:
            print("Failed as expected")
            return 0


def main():
    if len(sys.argv) != 2:
        print("Usage: ./validate.py <yaml_file>")
        sys.exit(1)

    yaml_file = sys.argv[1]

    result = run_testcase(yaml_file)
    sys.exit(result)


if __name__ == "__main__":
    main()
