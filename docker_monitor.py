import subprocess

def get_running_containers():
    result = subprocess.run(
        ["docker", "ps", "--format", "{{.ID}} {{.Names}} {{.Status}}"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip().split("\n")

def display_containers(containers):
    print("=" * 40)
    print("   RUNNING CONTAINERS")
    print("=" * 40)
    
    if containers == [""]:
        print("No containers running")
        return
    
    for container in containers:
        print(f"  {container}")
    
    print("=" * 40)
    print(f"  Total: {len(containers)} running")

containers = get_running_containers()
display_containers(containers)

print("\n  HEALTH STATUS")
print("=" * 40)
for container in containers:
    if "Up" in container:
        print(f"  HEALTHY  → {container}")
    else:
        print(f"  UNHEALTHY → {container}")