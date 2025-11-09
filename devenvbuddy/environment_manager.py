import subprocess 
import os

def start_environment(config):
    """Start the Docker environment defined in YAML config."""
    env_name = config.get("environment_name", "default_env")
    print(f" Starting environmewnt: {env_name}")
    
    # Create a temporary docker compose file from config (this will be generatewd dynamically later)
    compose_file = "docker_compose.yaml"
    
    # If a docker-compose file already exists, use it
    if not os.path.exists(compose_file):
        print("No docker-compose.yaml found. Please create one or add generation logic.")
        return
        
    try:
        subprocess.run(["docker", "compose", "-f", compose_file, "up", "-d"], check=true)
        print("f {env_name} started successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to start {env_name}.")
       
def stop_environment(config):
    """Stop and remove Docker containers."""
    env_name = config.get("environment_name", "default_env")
    print(f"Stopping environment: {env_name}")
    
    compose_file = "docker-compose.yaml"
    if not os.path.exists(compose_file)
        print("No docker-compose.yaml found.")
        return
        
    try:
        subprocess.run(["docker", "compose", "-f", compose_file, "down"], check=true)
        print("f {env_name} stopped and cleaned up.")
    except subprocess.CalledProcessError:
        print("fFailed to stop {env_name}.")
        
