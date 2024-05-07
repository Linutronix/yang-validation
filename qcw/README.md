<!--
SPDX-FileCopyrightText: 2024 Linutronix GmbH
SPDX-License-Identifier: 0BSD
-->

# Maintenance Request 0366: IEEE 802.1Qcw REVISION REQUEST on allowing non-scheduled interfaces

See https://www.802-1.org/items/473

`ieee802-dot1q-psfp@2024-01-30.yang` and `ieee802-dot1q-sched@2024-01-30.yang`: New versions of the YANG model as suggested in the maintenance request.

`minimal-interface.json`: Minimal interface instance

`minimal-interface-fail-testcase.yaml`: Testcase that fails with the instance above with the published YANG model.

`minimal-interface-success-testcase.yaml`: Testcase that runs successfully with the suggested changes in the maintenance request.

`scheduled-interface.json`: Exemplary instance with scheduling configuration according to IEEE 802.1Qcw.

`scheduled-interface-before-testcase.yaml`: Successful testcase before the suggested change.

`scheduled-interface-after-testcase.yaml`: Successful testcase after the suggested change.

