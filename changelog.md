# Changelog

## 27/7/2026

### Added

#### IdeaCentre Server Evaluation

Documented the potential integration of an IdeaCentre system into Project Olympus as a future infrastructure node.

##### Purpose

Evaluate the IdeaCentre as a dedicated always-on server to expand Project Olympus infrastructure capabilities.

##### Potential Responsibilities

* Docker container hosting
* Infrastructure monitoring
* Backup services
* Internal service hosting
* CI/CD workloads
* Additional homelab utilities

##### Proposed Infrastructure Role

Host: IdeaCentre (pending deployment)

Platform: Ubuntu Server (planned)

##### Relationship to Existing Infrastructure

Potential future migration target for lightweight services currently hosted on Atlas:

* Homepage
* Uptime Kuma
* UpSnap
* Additional Docker services

##### Outcome

Project Olympus architecture has been expanded to include a potential dedicated server node, separating infrastructure services from existing lightweight hardware and allowing future scalability.

## 5/6/2026

### Completed

- Defined Olympus architecture
- Configured Atlas server role
- Configured Tailscale connectivity
- Enabled Wake-on-LAN on Hyperion
- Installed wakeonlan on Atlas
- Successfully woke Hyperion remotely

### Notes

Remote power management is now functional.

## 11/6/2026

### Added

#### UpSnap Deployment

Successfully deployed UpSnap on Atlas using Docker.

##### Purpose

Provide a web-based interface for remote power management within Project Olympus.

##### Features

* Wake-on-LAN management
* Device status monitoring
* Centralised power management dashboard
* Remote access through Tailscale

##### Infrastructure

Host: Atlas

Platform: Docker

##### Managed Devices

* Hyperion

### Homepage

- Deployed Homepage dashboard on Atlas
- Created central service portal
- Added Olympus infrastructure links
- Established foundation for service monitoring and management

##### Outcome

Project Olympus now includes a dedicated web interface for remotely managing infrastructure power states without requiring direct SSH access or manual script execution.

## 12/6/2026

### Added

- Deployed Uptime Kuma on Atlas using Docker
- Added monitoring foundation for Project Olympus
- Planned monitors for Atlas, Hyperion, Homepage, UpSnap, and internet connectivity

### Fixed

- Began troubleshooting Homepage and UpSnap service availability
