#!/bin/bash
# SPDX-FileCopyrightText: 2024 Linutronix GmbH
# SPDX-License-Identifier: 0BSD

TEMP_FILE=$(mktemp)

cp README.md $TEMP_FILE


cat << EOF >> $TEMP_FILE

# Validation

[https://github.com/Linutronix/yang-validation](https://github.com/Linutronix/yang-validation)

* Contains testcases that trigger all the mentioned problems as well as sched and psfp examples that work before and after the proposed change

* Testcases are automatically executed (Github Actions) when adding/changing testcases

* Also executed daily to be notified early about changes in [https://github.com/YangModels/yang](https://github.com/YangModels/yang)

* Maybe also useful for other scenarios → Open to ideas & contributions!


EOF

pandoc \
  --metadata title="Maintenance Request 0366: IEEE 802.1Qcw REVISION REQUEST on allowing non-scheduled interfaces" \
  --metadata author="Florian Kauer (Linutronix)" \
  --metadata author="Tobias Deiminger (Linutronix)" \
  --metadata date="June 18, 2024" \
  --metadata aspectratio="169" \
  --metadata section-titles="false" \
  --metadata fontsize="8pt" \
  -f markdown -t beamer $TEMP_FILE -V theme:Boadilla --slide-level 2 -o maintenance-request-0366.pdf
