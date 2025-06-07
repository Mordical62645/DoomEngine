# Doom-Inspired Raycasting Engine

A Python-based recreation of the classic Doom game's rendering engine using object-oriented programming principles. This project implements the revolutionary raycasting technique that provided the illusion of a 3D environment from 2D map data in the original game.

## Features

- **WAD File Integration**
  - Reads and parses the original DOOM1.WAD file
  - Extracts and utilizes authentic game assets (textures, sprites, map data)
  - Implements binary file handling and data structures

- **3D Rendering System**
  - Raycasting algorithm for pseudo-3D rendering
  - Binary Space Partitioning (BSP) for efficient rendering
  - Proper perspective correction and texture mapping
  - Sky rendering and floor/ceiling textures

- **Player Movement and Controls**
  - First-person camera controls
  - Smooth movement and rotation
  - Collision detection with walls
  - Proper player positioning and angle calculations

- **Visual Features**
  - Texture mapping on walls and surfaces
  - Sprite rendering with billboarding
  - Proper lighting and shading effects
  - Smooth frame rate and performance optimization

## Requirements

- Python 3.13.3
- Pygame (wrapper for C language SDL library)
- Numba
- Slade3 (for checking WAD contents)

## Project Structure

```
DoomEngine/
│
├── wad/
│   └── DOOM1.WAD
│
├── asset_data.py    # Handles loading and processing asset data from WAD
├── bsp.py          # Implements Binary Space Partitioning for map rendering
├── data_types.py   # Defines custom data structures for map elements and assets
├── main.py         # Entry point of the application and main game loop
├── map_renderer.py # Responsible for rendering map geometry like walls
├── player.py       # Manages player state, movement, and controls
├── seg_handler.py  # Handles 'segs' created by BSP partitioning
├── settings.py     # Contains project configuration settings
├── view_renderer.py # Implements the raycasting view rendering
├── wad_data.py     # Handles WAD file data structures and directory
└── wad_reader.py   # Performs low-level binary reading of the WAD file
```

## Key Topics Covered

- WAD File Structure and Parsing
- Binary File Reading
- Data Structures (Vertices & Linedefs)
- Binary Space Partitioning (BSP)
- Raycasting
- Field of View (FOV)
- Texture Mapping
- Sprite Rendering
- Collision Detection
- Performance Optimization Techniques

## OOP Areas Used

- Encapsulation
- Abstraction
- Composition

## How to Run

1. Ensure you have Python 3.13.3 installed
2. Install required dependencies:
   ```bash
   pip install pygame numba
   ```
3. Place DOOM1.WAD in the `wad/` directory
4. Run the main script:
   ```bash
   python main.py
   ```

## Controls

- W/A/S/D: Movement
- Left/Right Arrow Keys: Rotation

## Performance Optimization

The project uses several optimization techniques:
- Numba for performance-critical code sections
- BSP for efficient rendering
- Texture caching
- Efficient collision detection

## Limitations

- Focuses primarily on the rendering engine
- Uses the shareware DOOM1.WAD file
- Does not include game logic (enemies, weapons, etc.)
- Limited to basic movement and rendering features

## Acknowledgments

- Original Doom game by id Software
- Slade3 for WAD file inspection
- Pygame community for graphics support
- Numba for performance optimization
