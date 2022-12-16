# Namespaces

At present, data is persisted to Linux shared memory ("/dev/shm"), then archived back to the application "save" directory as needed. Data is organized into namespaces, which are directories.

* **config**
  + System status flags.
  + App-deploy, build, install data.
  + GUI-construction data.
  + Static text.
  + Primitive type templates, if needed.
  + Experimental and prototype (not yet deployed) message metadata structures.
  + Obsoleted (no longer deployed) message metadata structures.

* **schema**
  + Message hierarchy metadata.
  + Record templates.
  + Topic, Plan, Broker, Channel, Request Type, Message format.

* harvest
  + Message response packets.
  + The messaging gateway writes response content to **harvest**.
  + Receivers pull content using a token = a unique key to harvest data.

* log
  + Detailed messaging system log.
  + Traces, warnings, errors.
  + The messaging system Wire Tap writes forensic info to **log**.

* monitor
  + Analytical messaging system state info and summaries.
  + The messaging system Wire Tap writes analytic info to **monitor**.




