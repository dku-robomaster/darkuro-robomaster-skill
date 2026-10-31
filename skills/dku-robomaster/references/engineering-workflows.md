# Engineering workflows

## Onboarding
Read division-roles. Establish the member's task and tools. Explain one subsystem at a time, then propose one measurable exercise. Match tasks to actual available equipment; do not assume ownership based on a recruitment document. End with expected behavior, evidence to collect and a next step.

## Mechanical design
Establish load, range of motion, speed, packaging, weight, power, maintenance and fabrication constraints. Compare concepts using torque/load estimates and assumptions. Reserve referee modules, batteries, cables, guards and service access in CAD early. Check current robot-specific and installation requirements from original diagrams before declaring compliance. Treat shared CAD and video as artifacts to inspect, not facts inferred from filenames.

## Electronic control
Trace battery → distribution/referee power path → controller/driver → actuator, and sensor → controller → feedback loop. Confirm model, pinout, voltage, current, polarity, grounds and logic levels before recommending connections. Prefer a minimal observable bench test before whole-robot integration. Distinguish command, feedback, enable/stop behavior and fault recovery.

## Computer vision and operator display
Distinguish industrial-camera acquisition on a robot's onboard computer from the official operator video path. Trace camera → onboard perception → estimated target/aim command → embedded control. A client overlay can carry drawing/state data without streaming the industrial-camera video. If mapping target boxes between cameras, account for calibration, viewpoints and latency. Verify current protocol and allowed links before specifying an implementation or promising video transport.

## Procurement
Confirm need, actual inventory, competition eligibility/discount approval, stock, actual quote date, limits, compatibility, lead time and warranty. Treat a budget spreadsheet as a draft. Verify official restrictions on sold versus season-loaned referee modules before recommending purchase. Give a comparison or proposed order; do not place orders or submit applications without authorization.

## Debugging
Ask for the concrete symptom, model, wiring/version, reproduction steps and logs. State hypotheses separately from evidence. Change one relevant variable at a time and define expected observations. Do not invent measured values. If the question concerns a high-energy electrical, rotating or pneumatic system, identify the specific test setup and necessary isolation for that action rather than adding generic warnings.

## Open-source evaluation
Record author, publication date, license, reproducible CAD/code/BOM, hardware and firmware versions, known defects and verification status. Do not equate downloadable files with a working system. Compare the design against current construction and redesign requirements. Confirm attribution and modification obligations before redistributing.

## Planning and status
Separate confirmed facts, proposals, decisions and tasks. Record owner, acceptance criterion, dependency, date and evidence. Use current team records rather than treating a previous conversation as shared mutable memory.
