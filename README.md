# Veeg Linux Setup

Complete redeploy of a customized linux development environment.
One-time install script to deploy a versioned instance of all dotconfigs and commands of note.

## Packages to install on a fresh machine

### fedora

```
dnf install git ruby
```

## Installation on fresh machine

* Ensure your SSH key is present in ~/.ssh
* Clone this repository into your home directory
* Run the ruby install script: ~/dotconfigs/install


### WSL specialization

Use wsl-open to handle opening files: https://github.com/4U6U57/wsl-open
