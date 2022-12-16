# Orchestration and Containers

Hot git tip of the day.. how to clone ONLY a single branch:

``` git clone git@bitbucket.org:ballofwax/bow_orch.git -b release/0.1 --single-branch```

## Why Not Docker

Docker, or something similar (see approaches used by Heroku and Cloud Foundry, for example) is "the right way" to containerize" apps. And we'll want to come back to that.

And to "do Docker right", we'll want to master Kubernetes too. And maybe Mesos.

I've had a bit of trouble getting Docker to do everything I wanted without a bit of tedium, so I've decided to leave it aside for now and focus on the more basic stuff.

For now, my attention is focused on auto-configuration of (*nix) accounts, Python virtual environments, and (very likely) run-time Linux instances: first as Digital Ocean "droplets", later as AWS EC2 (and probably other types of runtime) instances.

I am working on getting a handle on environment set up for Nginx and modSecurity before worrying too much about containerizing them. I kind of see that as packaging once I have the foundations in place.

## Linux accounts

A pattern I am working with is to define distinct Linux accounts for specified purposes. For example, I want to make sure I can deploy a development environment for the app(s) that is distinct from runtime app environments.

As noted above, using containers is becoming the standard way to do that. And I want to be mindful not to over-engineer the automated configuration of Linux accounts. But for my own purposes, I feel that I can learn and prototype faster when working directly with Linux.

I need to get a stronger feeling for how to handle components that typically reside in non-home directories. Again, I know Docker can handle it, but I want to make sure I know that I can handle it on my own terms first. This means getting familiar with how users and groups work in Linux, so that, for example, User A can execute a script that resides under account for User B.

I may be barking up entirely the wrong tree with some of this. But keep in mind that my target environment for all this is to be entirely web-based.  I would prefer to not deploy anything, or at least very little, to local hosts.  So I am not terribly concerned, for example, about being able to run under some generic user's account on their MacOS, iOS, Android, Windows or *nix device.

## Linux and other servers

I am interested in when it makes sense to deploy my components to distinct servers for smart separation of services. Deploying multiple instances of the core services for global performance improvements is important too, but I am already somewhat familiar with load balancing.  Separation of duties is an important part of my architectural vision.

The canonical use case is to host database servers separately from app servers, so I'll definitely work on that.  Work with discretely-mounted storage units too, whether Digital Ocean Spaces, or AWS EBS or S3 storage, for handling various types of files. The file management equation -- sharing storage between instances and so on -- is a different challenge from full-blown runtime server instances.

Intend that all web apps and web services be load-balanced within a node or cluster via Nginx.

Intend that multiple server instances align to common data storage, both static resources and dynamic storage, via robust CDN and write/read replica configurations, supported by a strong data service layer.

Intend that deployment of all instances and servers should be automated and monitored for faults and failures, with appropriate failover, disaster recovery and performance optimization.

## Security and encryption

Aware of the need to handle all aspects of security as a top priority. Intend this app (bow_orch) to provide framework for building out and deploying various apps, segregated appropriately -- as servers, as containerized or otherwise contained environments, and as services.

Won't list all of the Security-related items here, but some of the things to prepare for include:

- Configure Nginx to always work only with TLS, to re-route all HTTP to HTTPS

  - Come up with a framework for doing so in dev-test environment where I don't have real, verifiable certificates
  - It is easy enough to just not enable HTTPS. And I can generate self-signed certs.  But some browsers will reject those.

- Auto-configure management and monitoring of TLS certifications using something like certbot
- Route all web traffic through Nginx; avoid direct public links to app and service instances
- Compile Nginx with modSecurity.  Establish a strong Web Application Firewall (WAF)
- Know how to use reliable encryption-at-rest techniques such as openSSL or Frenet or GPG for example, with a good scheme in place for separating key storage and restricting access to keys
- Have a secure and working IAM framework, even a home-grown one not yet Okta- or OAuth- integrated or whatever with 3rd party authorizers and whatnot
- Use only fully secured/encrypted cookies

## Python-centric

In previous iterations, I did a lot of the build configuration in bash scripts. I'd prefer to do as much configuration work as I can via Python scripts, even if they have to make OS level calls. Python gives me better control over logging, access to my common functions. I also find it easier to read and debug.

After verifying and upgrading basic stuff (git, ssh, net-tools, ufw) the first step in my bootstrap installer should be to install/upgrade python3. This is the kind of thing than can be done in a server start-up script. Need to be mindful about not installing too many python packages at the system level, though.  Minimize what is done in bash.

Once python is installed and configured, then verify account and group set-ups as desired, then install venvs as needed under those accounts and install requirements.

See notes about deploying and configuring Nginx and Tornado apps.
