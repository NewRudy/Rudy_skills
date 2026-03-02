# Docker Janitor

A specialized skill for managing Docker Desktop storage, optimizing disk usage on the C: drive, and maintaining a lean container environment.

## Usage
- "Clean up my Docker history images and cache."
- "Show me what's taking up space in Docker."
- "My C drive is full because of Docker, help!"
- "How do I move Docker Desktop data to another drive?"

## Core Commands

### 1. Analysis
- **Check Usage**: `docker system df` (Shows space used by images, containers, and volumes).
- **Detailed Scan**: `docker images -a` (Lists all images including intermediate layers).

### 2. Cleanup (The "Janitor" Mode)
- **Standard Prune**: `docker system prune -f`
    - Removes stopped containers, unused networks, and dangling images.
- **Deep Clean (Recommended for C: drive relief)**: `docker system prune -a --volumes -f`
    - Removes *all* unused images (not just dangling ones) and unused volumes.
- **Build Cache Only**: `docker builder prune -f`
    - Specifically targets the cache that builds up during `docker build`.

## Advanced Optimization

### 3. Relocate Docker Data (WSL2)
If your C: drive is still tight, move the `ext4.vhdx` to another drive (e.g., D:):
1. Shutdown Docker Desktop.
2. `wsl --export docker-desktop-data D:\docker-desktop-data.tar`
3. `wsl --unregister docker-desktop-data`
4. `wsl --import docker-desktop-data D:\DockerData D:\docker-desktop-data.tar --version 2`
5. Restart Docker Desktop.

### 4. Compact VHDX (Windows Pro/Enterprise)
If you deleted files but the `.vhdx` file size didn't shrink:
- Run PowerShell as Admin:
  ```powershell
  Optimize-VHD -Path "$env:LOCALAPPDATA\Docker\wsl\data\ext4.vhdx" -Mode Full
  ```

## Principles
- **Safety First**: Never prune volumes without the `--volumes` flag unless explicitly requested, as volumes contain persistent data.
- **Automation**: Run `docker-janitor` whenever C: drive free space falls below 10%.
