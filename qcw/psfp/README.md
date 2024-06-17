<!--
SPDX-FileCopyrightText: 2024 Linutronix GmbH
SPDX-License-Identifier: 0BSD
-->

`psfp/minimal-bridge.json`: Minimal bridge instance featuring essential PSFP components

`psfp/minimal-bridge-fail-testcase.yaml`: Testcase that fails with the instance above with the published YANG model.

`psfp/minimal-bridge-success-testcase.yaml`: Testcase that runs successfully with the suggested changes in the maintenance request.

`psfp/psfp-example.json`: Exemplary instance with PSFP configuration according to IEEE 802.1Qcw.

`psfp/psfp-example-before-testcase.yaml`: Successful testcase before the suggested change.

`psfp/psfp-example-after-testcase.yaml`: Successful testcase after the suggested change.

`psfp/too-many-flow-meters.json`: Exemplary instance with PSFP configuration with too many flow meter entries.

`psfp/too-many-flow-meters-unexpected-success-testcase.yaml`: Testcase before the suggested change, should fail due too many flow meter entries, but doesn't.

`psfp/too-many-flow-meters-expected-fail-testcase.yaml`: Testcase after the suggested change, does fail due too many flow meter entries as expected.
