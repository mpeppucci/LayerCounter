# Layer Counter Plugin

A simple and useful QGIS plugin to count layers loaded in the project and those selected in the layer panel.

## Description

Layer Counter is a QGIS plugin that provides quick information about layers present in your project. With a simple click, you can view:

- **Total number of layers** loaded in the project
- **Number of selected layers** (highlighted in blue in the layer panel)

## Features

✅ **Accurate counting**: Counts only actual layers, excluding groups  
✅ **Distinction between loaded and selected**: Differentiates between layers present in the project and those currently selected  
✅ **Simple interface**: An icon in the toolbar and an entry in the Plugin menu  
✅ **Informative popup**: Results displayed in a clear dialog window  

## Installation

1. Download or clone this repository
2. Copy the `layer_counter` folder to the QGIS plugins directory:
   - **Windows**: `C:\Users\[username]\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`
   - **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
   - **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
3. Restart QGIS
4. Enable the plugin from **Plugins > Manage and Install Plugins**

## Usage

### Method 1: Toolbar
- Click the **Layer Counter** icon in the QGIS toolbar

### Method 2: Menu
- Go to **Plugins > Layer counter > Layer Counter**

### Result
A dialog window will appear with the information:
```
Layers in project: 5
Selected layers in project: 2
```

## Practical Example

Imagine having this scenario in the layer panel:
- 📁 **Buildings Group**
  - 🏠 Residential buildings ✅ (checked and selected)
  - 🏢 Commercial buildings ✅ (checked but not selected)
- 🛣️ **Roads** ✅ (checked but not selected)
- 🌳 **Vegetation** ❌ (not checked, not selected)

**Plugin result:**
- Layers in project: **4** (doesn't count the group)
- Selected layers in project: **1** (only "Residential buildings" is highlighted)

## System Requirements

- **QGIS**: version 3.28 or higher
- **Python**: 3.9 or higher
- **Operating System**: Windows, macOS, Linux

## Plugin Structure

```
layer_counter/
├── __init__.py              # Plugin initialization
├── layer_counter.py         # Main plugin logic
├── layer_counter_dialog.py  # Dialog class (if needed)
├── metadata.txt             # Plugin metadata
├── icon.png                 # Plugin icon
├── README.md               # This file
└── resources.py            # Compiled Qt resources
```

## Development

### Main Features

The plugin uses QGIS APIs for:
- `QgsProject.instance().mapLayers()` - Total layer counting
- `iface.layerTreeView().selectedLayers()` - Selected layer counting
- `QMessageBox` - Results display

### Customization

The code is easily extensible to add features such as:
- Counting by layer type (vector, raster)
- Results export
- Status bar integration
- Real-time automatic counting

## Author

**Eagleprojects S.p.A.**
- Email: gis@eagleprojects.it
- Date: 2025-07-30

## License

This plugin is distributed under the **GNU General Public License v2.0**.

```
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
```

## Support

For bug reports, feature requests, or technical support, contact:
- Email: gis@eagleprojects.it

## Changelog

### v0.1 (2025-07-30)
- ✨ First release
- ✅ Total layer counting in project
- ✅ Selected layer counting in panel
- ✅ Toolbar and menu interface
- ✅ Informative popup with results

---

**Happy mapping with QGIS! 🗺️**