# Layer Counter Plugin

A simple and useful QGIS plugin that provides real-time counting of layers loaded in the project and those selected in the layer panel through an integrated widget.

## Description

Layer Counter is a QGIS plugin that displays continuous information about layers present in your project through a dedicated panel widget. The plugin shows in real-time:

- **Total number of layers** loaded in the project
- **Number of selected layers** (highlighted in blue in the layer panel)

The information is displayed in a dedicated panel that can be docked anywhere in the QGIS interface and updates automatically when layers are added, removed, or selected.

## Features

✅ **Real-time updates**: Automatic counting updates when layers are added, removed, or selected  
✅ **Integrated widget**: Dockable panel that integrates seamlessly with the QGIS interface  
✅ **Accurate counting**: Counts only actual layers, excluding groups  
✅ **Distinction between loaded and selected**: Differentiates between layers present in the project and those currently selected  
✅ **Flexible positioning**: Panel can be docked on left, right, or bottom of QGIS interface  
✅ **Show/hide toggle**: Easy access through toolbar icon and menu entry  

## Installation

1. Download or clone this repository
2. Copy the `layer_counter` folder to the QGIS plugins directory:
   - **Windows**: `C:\Users\[username]\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`
   - **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
   - **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
3. Restart QGIS
4. Enable the plugin from **Plugins > Manage and Install Plugins**

## Usage

### Showing the Panel

**Method 1: Toolbar**
- Click the **Layer Counter** icon in the QGIS toolbar to show/hide the panel

**Method 2: Menu**
- Go to **Plugins > Layer Counter > Layer Counter** to toggle the panel visibility

### Panel Features

The Layer Counter panel displays:
```
Total layers: 5
Selected layers: 2
```

**Panel Management:**
- **Dock positioning**: Drag the panel to dock it on the left, right, or bottom of the QGIS interface
- **Auto-hide**: Close the panel by clicking the 'X' button; reopen it using the toolbar icon or menu
- **Real-time updates**: Counts update automatically as you work with layers

### Real-time Updates

The panel automatically updates when:
- New layers are added to the project
- Layers are removed from the project
- Layer selection changes in the layer panel
- Project is cleared or new project is loaded

## Practical Example

Imagine having this scenario in the layer panel:
- 📁 **Buildings Group**
  - 🏠 Residential buildings ✅ (checked and selected)
  - 🏢 Commercial buildings ✅ (checked but not selected)
- 🛣️ **Roads** ✅ (checked but not selected)
- 🌳 **Vegetation** ❌ (not checked, not selected)

**Plugin panel shows:**
- Total layers: **4** (doesn't count the group)
- Selected layers: **1** (only "Residential buildings" is highlighted)

*Updates happen instantly as you select/deselect layers!*

## System Requirements

- **QGIS**: version 3.28 or higher
- **Python**: 3.9 or higher
- **Operating System**: Windows, macOS, Linux

## Development

### Main Features

The plugin uses QGIS APIs for:
- `QgsProject.instance().mapLayers()` - Total layer counting
- `iface.layerTreeView().selectedLayers()` - Selected layer counting
- `QDockWidget` - Integrated panel interface
- Signal connections for real-time updates

### Architecture

**Version 1.2 Updates:**
- Transformed from popup dialog to integrated widget
- Added real-time update functionality through Qt signals
- Implemented dockable panel with flexible positioning
- Enhanced user experience with continuous monitoring

### Customization

The code is easily extensible to add features such as:
- Counting by layer type (vector, raster, WMS, etc.)
- Layer visibility status
- Results export functionality
- Custom styling and themes
- Additional layer statistics

## Version History

**v1.2** (Current)
- ✨ **NEW**: Widget embedded in dockable panel
- ✨ **NEW**: Real-time automatic updates
- ✨ **NEW**: Flexible panel positioning (left, right, bottom)
- ✨ **NEW**: Toggle show/hide functionality
- 🔧 Enhanced user interface with better integration

**v1.0**
- Initial release with popup dialog functionality

## Author

**GIS Team Eagleprojects S.p.A.**
- Email: gis@eagleprojects.it
- Date: 2025-07-30
- Repository: https://github.com/mpeppucci/LayerCounter

## License

This plugin is distributed under the **GNU General Public License v2.0**.

```
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
```

## Support

For bug reports, feature requests, or technical support:
- **Issues**: https://github.com/mpeppucci/LayerCounter/issues
- **Email**: gis@eagleprojects.it

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues on the GitHub repository.

**Happy mapping with QGIS! 🗺️**