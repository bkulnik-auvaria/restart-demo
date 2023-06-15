# Migration

The company ABC Inc has reached out to you because they are unsatisfied with their current IT and hosting solution. They are currently operating two applications, two database and a fileserver ALL on a single physical host (but on distinct virtual machines). Their employees need to be able to connect to the server(s) but in general the server(s) should not be exposed to the internet. Also for administrative reasons, they need an active directory service. They are also using only Microsoft SQL Server for their databases.

There physical host has the following specifications:

| VM  | Server Role                       | vCPUs | Memory | Storage | OS      |
| --- | --------------------------------- | ----- | ------ | ------- | ------- |
| VM1 | App Server 1                      | 8     | 16 GB  | 500 GB  | Windows |
| VM2 | Database Server                   | 2     | 16 GB  | 200 GB  | Windows |
| VM3 | App Server 2 + Database           | 2     | 8 GB   | 300 GB  | Windows |
| VM4 | Fileserver                        | 8 GB  | 300 GB | Windows | Windows |
| VM5 | Active Director Domain Controller | 2     | 4 GB   | 60 GB   | Windows |


They want to move their Infrastructure to AWS and their main interests are:

- Low cost (total costs should not exceed 2000$ / month)
- Low maintenance: they don't want to spend time to manage servers
- High availability
- Security

They asked you for some guidance and to lead the migration to AWS.

- What would be a suitable architecture in this case?
- What would be the expected cost per month to operate this on AWS? (check out https://calculator.aws/)
- What would be the one-time cost of the migration? Think about how much time you have to effectively spend, so that you can perform the migration. Assume a realistic hourly-rate for the work (e.g. 100€/hour)
- What would be next steps after the migration?
  