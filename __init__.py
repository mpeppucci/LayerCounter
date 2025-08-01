# -*- coding: utf-8 -*-
"""
/***************************************************************************
 layer_counter
                                 A QGIS plugin
 Plugin that count layer loaded in the layer panel.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-07-30
        copyright            : (C) 2025 by Eagleprojects S.p.A.
        email                : gis@eagleprojects.it
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load layer_counter class from file layer_counter.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .layer_counter import layer_counter
    return layer_counter(iface)
