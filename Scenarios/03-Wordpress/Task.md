# Wordpress (Compute, Network, Storage)

Create your own high-available, resilient blog using Wordpress and AWS.

- Make it scalable: use autoscaling and load balancing
- Make it redundant: use replicas (where necessary)
- Make it secure: apply principle of least privilege and network security guidelines
- Make it fast: Improve performance using caching methods

## Tasks

1. Read on the web about Wordpress and how to deploy it.[^1]. Also have a look at guides how to setup Wordpress on AWS[^2]
2. Draw an architecture diagram.
   1. VPC: Route-Tables, Subnets, NATs, IGW, etc.
   2. High-Availability: Load Balancers and Autoscaling
   3. Database
   4. Shared storage
   5. Performance through caching
3. Deploy everything to AWS
4. Deploy everything to AWS again, but this time make it with Infrastructure-as-Code tools (e.g. use Terraform, User-Data, Cloud-Init, Scripts, etc.) (_if you find the time_)



[^1]: See for example the official homepage [wordpress.org](https://wordpress.org/)
[^2]: Best practice guide can be found [here](https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/welcome.html). A reference architecture can be found [on the AWS documentation page as well](https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/reference-architecture.html).