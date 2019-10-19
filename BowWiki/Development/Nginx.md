# Nginx and modSecurity

## Why

I have found Nginx to be easy to understand and configure. It seems to work great with Python-Tornado-launched apps and services, which is my favorite app framework.  And I've been able to get it working pretty quickly with both certbot/letsencrypt and with Apache modSecurity.

There are a number of good courses available on Udemy that explain the basic concepts in a clear and useful way. And the documentation is pretty good too.

## Installing them

Nginx has to be compiled if including modSecurity.  See python deployment script for bow_orch on how I did this.

May want to consider using a simpler install in "dev-test" environments where I am not actually connecting to the Internet and may not even be using TLS.  If doing the simple way, then can just apt-get or yum install it.

As of this writing, modSecurity and its rules have to be downloaded from Spider Labs.  modSecurity is from Apache originally. It helps to implement "OWASP" style rules for web apps and services.

## Learning about OWASP

I've started out by copying in all possible rules provided by Spider Labs, including the Experimental ones. No doubt learning more about OWASP will be helpful, but I figured I'll just start with the "maximum" set.  There are Udemy courses on OWASP too.

OWASP = Open Web Application Security Project

Places to start with OWASP:

- [Wikipedia: OWASP](https://en.wikipedia.org/wiki/OWASP)
- [OWASP Guide Project](https://www.owasp.org/index.php/OWASP_Guide_Project)
- [OWASP App Security Verification Standard](https://www.owasp.org/index.php/Category:OWASP_Application_Security_Verification_Standard_Project)

## modSecurity

This is an open source Web Application Firewall (WAF). Originally released for Apache's httpd server, it now integrates with IIS and Nginx too. Rules configured under "modSec" are referred to as "SecRules".  The latest iteration is called ``libmodsecurity`` (ModSecurity v3.0) with API connectors for Nginx and Apache httpd.

modSecurity provides a framework for installing OWASP rules for a web application.

SpiderLabs is owned by TrustWave, the company that has re-licensed modSecurity.  The Spider Labs wiki includes details on how to install and configure modSecurity with Nginx.

- [Wikipedia: modSecurity](https://en.wikipedia.org/wiki/ModSecurity)
- [SpiderLabs: modSecurity wiki](https://github.com/SpiderLabs/ModSecurity/wiki)

## Penetration and Performance Testing

The OWASP community provides the ZAP tool and test app called __Webgoat__, which demonstrates all the things NOT to do.  In other words, it exhibits all the weaknesses of an insecure web app.

Explore the Kali Linux community to learn about many sophisticated tools and techniques relating to penetration testing and other network security issues.

For basic and easy-to-use performance testing, the Siege tool is quite nice. It would not be terrible to integrate regular Siege-based tests into a deployment and support process.

## Tornado and Twisted

I have become a "fan" of Tornado and prefer it over Flask for reasons I can't quite elaborate.  Based on everything I've read, it provides a more robust framework for "serious" web apps or web services than Flask does.  I find it easy to use and quite sensible.  It is based on the Twisted networking framework, which handles a great deal of the "non-blocking" work for you without requiring an advanced degree in either computer science or physics. :-)

I can stand up and unit test an application using Tornado without having to install or configure Nginx or Apache httpd or IIS or WebSphere or tomcat or anything like that.

Then when I have it in relatively good shape, it is fairly painless to spin up multiple instances on "bespoke" ports and put them behind a (highly secured) Nginx "app server" (load balancer) that can use standard ports.  I have not yet tried to manage a cluster in this way, nor have I tried to deploy across large geographical zones or internationally.  I expect there are ways to manage that using Nginx alone, or at that point I'll probably need to consider AWS services more carefully.
