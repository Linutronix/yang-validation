#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 Linutronix GmbH
# SPDX-License-Identifier: 0BSD

import sys
import yaml
import subprocess


def run_testcase(test):
    ## Find YAML modules
    yang_files = []

    for model in test["models"]:
        yang_files.append(model["file"])

    ## Run yanglint
    command = ["yanglint"] + yang_files + [test["instance"]]

    print(" ".join(command))

    result = subprocess.run(command)

    if result.returncode == 0:
        if test["expect_success"]:
            print("Successful as expected")
            return True
        else:
            print("Successful, but was not expected")
            return False
    else:
        if test["expect_success"]:
            print("Failed, but success was expected")
            return False
        else:
            print("Failed as expected")
            return True


def main():
    if len(sys.argv) != 2:
        print("Usage: ./validate.py <yaml_file>")
        sys.exit(1)

    yaml_file = sys.argv[1]

    with open(yaml_file, "r") as f:
        config = yaml.safe_load(f)

        successful = 0

        for test in config["tests"]:
            print(test["name"])

            if run_testcase(test):
                successful += 1

            print()

    print("{}/{} testcases successful".format(successful, len(config["tests"])))
    sys.exit(0 if successful == len(config["tests"]) else 1)


if __name__ == "__main__":
    main()
