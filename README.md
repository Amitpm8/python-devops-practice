# Python DevOps Practice

Learning Python through real DevOps automation tools.

## Tools Built

### docker_monitor.py
Monitors running Docker containers and displays health status.

**What it does:**
- Lists all running containers
- Shows container ID, name, and uptime
- Displays HEALTHY or UNHEALTHY status for each

**Run it:**
```bash
python3 docker_monitor.py
```

**Example output:**

========================================
RUNNING CONTAINERS
db87b4a9cbf9 nginx Up 25 seconds
Total: 1 running
HEALTH STATUS
HEALTHY   → db87b4a9cbf9 nginx Up 25 seconds

## Concepts Learned
- Python functions with `def`
- subprocess module to run terminal commands
- f-strings for formatted output
- Error handling with returncode
- List manipulation with split() and strip()

## Stack
- Python 3
- Docker
- Linux/WSL2