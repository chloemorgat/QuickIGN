# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QuickIGN
                                 A QGIS plugin
 QuickIGN
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-02-10
        copyright            : (C) 2021 by Chloe Morgat
        email                : chloe.morgat@ensg.eu
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
    """Load QuickIGN class from file QuickIGN.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .QuickIGN import QuickIGN
    return QuickIGN(iface)
