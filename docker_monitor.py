import subprocess

def get_running_containers():
    result = subprocess.run(
        ["docker", "ps", "--format", "{{.ID}} {{.Names}} {{.Status}}"],
        capture_output=True,
        text=True
    )
    
    # if docker command failed, tell us why
    if result.returncode != 0:
        print(f"ERROR: {result.stderr.strip()}")
        return []
    
    output = result.stdout.strip()
    
    # if no containers running
    if output == "":
        return []
    
    return output.split("\n")

def display_containers(containers):
    print("=" * 40)
    print("   RUNNING CONTAINERS")
    print("=" * 40)
    
    if not containers:
        print("  No containers running")
        print("=" * 40)
        return
    
    for container in containers:
        print(f"  {container}")
    
    print("=" * 40)
    print(f"  Total: {len(containers)} running")
    print("\n  HEALTH STATUS")
    print("=" * 40)
    
    for container in containers:
        if "Up" in container:
            print(f"  HEALTHY   → {container}")
        else:
            print(f"  UNHEALTHY → {container}")

containers = get_running_containers()
display_containers(containers)