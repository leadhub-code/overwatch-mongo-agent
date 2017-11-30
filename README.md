Overwatch MongoDB agent
=======================

[![CircleCI](https://circleci.com/gh/leadhub-code/overwatch-mongo-agent/tree/master.svg?style=svg&circle-token=2e9fdcd2eb3f29c848ef41078af719f03379b5f4)](https://circleci.com/gh/leadhub-code/overwatch-mongo-agent/tree/master)

Checks status of MongoDB instances and reports it to [Overwatch Hub](https://github.com/leadhub-code/overwatch-hub).

For description what is this all about see [the description of Overwatch monitoring](https://github.com/leadhub-code/overwatch-monitoring/blob/master/README.md).

TODO:

- connect to MongoDB instance
- check rs.status
- check serverStatus
- make sure this agent can detect network connectivity problems
- check that there is a primary node in a replica set


Feedback and contact
--------------------

- [open an issue](https://github.com/leadhub-code/overwatch-mongo-agent/issues/new) - even for a question or discussion
- contact me on [Twitter](https://twitter.com/messa_en) or via e-mail (see [my profile](https://github.com/messa))


Links
-----

MongoDB docs:

- [Operations Checklist](https://docs.mongodb.com/manual/administration/production-checklist-operations/)
- [Monitoring for MongoDB](https://docs.mongodb.com/manual/administration/monitoring/)
