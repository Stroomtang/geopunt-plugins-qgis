# -*- coding: utf-8 -*-
"""
/***************************************************************************
geometryHelper
                                A QGIS plugin
"Tool om geopunt in QGIS te gebruiken"
                            -------------------
        begin                : 2013-12-05
        copyright            : (C) 2013 by Kay Warrie
        email                : kaywarrie@gmail.com
***************************************************************************/

/***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************/
"""
from PyQt4.QtCore import *
from qgis.core import *
from PyQt4.QtGui import QFileDialog, QColor
from qgis.gui import QgsVertexMarker
import os

class geometryHelper:
    def __init__(self , iface ):
      self.iface = iface
      self.canvas = iface.mapCanvas()
      self.adreslayerid = ''
      self.poilayerid = ''
        
    def prjPtToMapCrs( self, xy , fromCRS=4326 ):
      point = QgsPoint( xy[0], xy[1] )
      fromCrs = QgsCoordinateReferenceSystem(fromCRS)
      toCrs = self.iface.mapCanvas().mapRenderer().destinationCrs()
      xform = QgsCoordinateTransform( fromCrs, toCrs )
      return   xform.transform( point )
    
    def prjPtFromMapCrs( self, xy , toCRS=31370 ):
      point = QgsPoint( xy[0], xy[1] )
      toCrs = QgsCoordinateReferenceSystem(toCRS)
      fromCrs = self.iface.mapCanvas().mapRenderer().destinationCrs()
      xform = QgsCoordinateTransform( fromCrs, toCrs )
      return   xform.transform( point )
      
    def zoomtoRec(self, xyMin, xyMax , crs=None):
      """zoom to rectangle from 2 points with given crs, default= mapCRS"""
      if crs is None:
          crs = self.iface.mapCanvas().mapRenderer().destinationCrs()
          
      maxpoint = QgsPoint(xyMax[0], xyMax[1])
      minpoint = QgsPoint(xyMin[0], xyMin[1])
      
      pmaxpoint = self.prjPtToMapCrs(maxpoint, crs)
      pminpoint = self.prjPtToMapCrs(minpoint, crs)
      
      # Create a rectangle to cover the new extent
      rect = QgsRectangle( pmaxpoint, pminpoint )
  
      # Set the extent to our new rectangle
      self.iface.mapCanvas().setExtent(rect)
      # Refresh the map
      self.iface.mapCanvas().refresh()
    
    def zoomtoRec2(self, bounds, crs=None):
        "zoom to rectangle from a list containing: [xmin,ymin,xmax,ymax] with given crs, default= mapCRS"
        if not bounds or len(bounds) != 4:
            return
        if crs is None:
            crs = self.iface.mapCanvas().mapRenderer().destinationCrs()
            
        maxpoint = QgsPoint( bounds[0], bounds[1])
        minpoint = QgsPoint( bounds[2], bounds[3])
        
        pmaxpoint = self.prjPtToMapCrs(maxpoint, crs)
        pminpoint = self.prjPtToMapCrs(minpoint, crs)
      
        # Create a rectangle to cover the new extent
        rect = QgsRectangle( pmaxpoint, pminpoint )
    
        # Set the extent to our new rectangle
        self.iface.mapCanvas().setExtent(rect)
        # Refresh the map
        self.iface.mapCanvas().refresh()

    def save_adres_point(self, point, address, typeAddress='', layername="Geopunt_adres", saveToFile=False, sender=None):
        attributes = [QgsField("adres", QVariant.String), QgsField("type", QVariant.String)]
        mapcrs = self.canvas.mapRenderer().destinationCrs()
        
        if not QgsMapLayerRegistry.instance().mapLayer(self.adreslayerid):
            self.adreslayer = QgsVectorLayer("Point", layername, "memory")
            self.adresProvider = self.adreslayer.dataProvider()
            self.adresProvider.addAttributes(attributes)
            self.adreslayer.updateFields()

        # add a feature
        fields= self.adreslayer.pendingFields()
        fet = QgsFeature(fields)

        #set geometry and project from mapCRS
        xform = QgsCoordinateTransform( mapcrs, self.adreslayer.crs() )
        prjPoint = xform.transform( point )
        fet.setGeometry(QgsGeometry.fromPoint(prjPoint))

        #populate fields
        fet['adres'] = address
        fet['type'] = typeAddress
        self.adresProvider.addFeatures([ fet ])
        ""
        # update layer's extent when new features have been added
        # because change of extent in provider is not propagated to the layer
        self.adreslayer.updateExtents()
            
        if saveToFile and not QgsMapLayerRegistry.instance().mapLayer(self.adreslayerid): 
          save = self._saveToFile( sender )
          if save:
            fpath, flType = save                
            error = QgsVectorFileWriter.writeAsVectorFormat(self.adreslayer, fpath, "utf-8", None, flType)
            if error == QgsVectorFileWriter.NoError:
              self.adreslayer = QgsVectorLayer( fpath, layername, "ogr")
              self.adresProvider = self.adreslayer.dataProvider()
            else: 
              del self.adreslayer, self.adresProvider 
              return
          else: 
            del self.adreslayer, self.adresProvider 
            return
          
        #  set id, add to map, Labels on, refresh
        self.adreslayerid = self.adreslayer.id()
        QgsMapLayerRegistry.instance().addMapLayer(self.adreslayer)
        
        #labels
        palyr = QgsPalLayerSettings() 
        palyr.readFromLayer( self.adreslayer ) 
        palyr.enabled = True 
        palyr.fieldName = 'adres' 
        palyr.placement= QgsPalLayerSettings.Free 
        palyr.setDataDefinedProperty(QgsPalLayerSettings.Size,True,True,'8','') 
        palyr.writeToLayer( self.adreslayer ) 
        
        self.canvas.refresh()
        
    def save_pois_points(self, points, layername="Geopunt_poi", saveToFile=None, sender=None):
        mapcrs = self.canvas.mapRenderer().destinationCrs()
        attributes = [  QgsField("id", QVariant.Int),
            QgsField("thema", QVariant.String),
            QgsField("category", QVariant.String),
            QgsField("type", QVariant.String),
            QgsField("name", QVariant.String),
            QgsField("adres", QVariant.String),
            QgsField("link", QVariant.String),
            QgsField("lastupdate", QVariant.String, "DateTime"),
            QgsField("owner", QVariant.String)  ]
    
        if not QgsMapLayerRegistry.instance().mapLayer(self.poilayerid) :
            self.poilayer = QgsVectorLayer("Point", layername, "memory")
            self.poiProvider = self.poilayer.dataProvider()
            self.poiProvider.addAttributes(attributes)
            self.poilayer.updateFields()    
        
        fields=self.poilayer.pendingFields()
        
        for point in points:
            pt = QgsPoint( point['location']['points'][0]['Point']['coordinates'][0], 
                           point['location']['points'][0]['Point']['coordinates'][1]  )
            poiId = point["id"]
            if "categories" in point and len(point["categories"]) > 0: theme =     point["categories"][0]['value']
            else: theme = ''
            if "categories" in  point and len(point["categories"]) > 1: category = point["categories"][1]['value']
            else: category = ''
            if "categories" in  point and len(point["categories"]) > 2: poiType =  point["categories"][2]['value']
            else: poiType = ''
            name = point["labels"][0]["value"]
            adres = point['location']['address']["value"].replace("<br />",", ").replace("<br/>",", ")
            if "links" in point: link = point["links"][0]['href']
            else: link = ""
            tijd =  point["updated"] 
            if "authors" in point: owner = point["authors"][0]["value"]
            else: owner= ""

            # add a feature
            fet = QgsFeature(fields)

            #set geometry
            fromCrs = QgsCoordinateReferenceSystem(4326)
            xform = QgsCoordinateTransform( fromCrs, self.poilayer.crs() )
            prjPt = xform.transform( pt )
            fet.setGeometry(QgsGeometry.fromPoint(prjPt))
      
            fet['id'] = int( poiId )
            fet['thema'] = theme
            fet['category'] = category
            fet['type'] = poiType
            fet['name'] = name
            fet['adres'] = adres
            fet['link'] = link
            fet['lastupdate'] = tijd
            fet['owner'] = owner
      
            self.poiProvider.addFeatures([ fet ])
            self.poilayer.updateExtents()
    
        if saveToFile and not QgsMapLayerRegistry.instance().mapLayer(self.poilayerid):
            save = self._saveToFile( sender )
            if save:
              fpath, flType = save
              error = QgsVectorFileWriter.writeAsVectorFormat(self.poilayer, fpath, "utf-8", None, flType, )
              if error == QgsVectorFileWriter.NoError:
                  self.poilayer = QgsVectorLayer( fpath , layername, "ogr")
                  self.poiProvider = self.poilayer.dataProvider()
              else: 
                  del self.poilayer, self.poiProvider 
                  return 
            else:
              del self.poilayer, self.poiProvider 
              return 

        # add Labels
        palyr = QgsPalLayerSettings() 
        palyr.readFromLayer( self.poilayer ) 
        palyr.enabled = True 
        palyr.fieldName = 'name' 
        palyr.placement= QgsPalLayerSettings.Free 
        palyr.setDataDefinedProperty(QgsPalLayerSettings.Size,True,True,'8','') 
        palyr.writeToLayer( self.poilayer ) 
        
        # add layer if not already
        QgsMapLayerRegistry.instance().addMapLayer(self.poilayer)

        # store layer id and refresh
        self.poilayerid = self.poilayer.id()
        self.canvas.refresh()
    
    def _saveToFile( self, sender ):
        'save to file'
        #"Shape Files (*.shp);;Geojson File (*.geojson);;GML ( *.gml);;Comma separated value File (excel) (*.csv);;MapInfo TAB (*.TAB);;Any File (*.*)"
        filter = "ESRI Shape Files (*.shp);;SpatiaLite (*.sqlite);;Any File (*.*)" #show only formats with update capabilty
        Fdlg = QFileDialog()
        Fdlg.setFileMode(QFileDialog.AnyFile)
        fName = Fdlg.getSaveFileName( sender, "open file" , None, filter)
        if fName:
          ext = os.path.splitext( fName )[1]
          if "SHP" in ext.upper():
            flType = "ESRI Shapefile"
          elif "SQLITE" in ext.upper():
            flType = "SQLite" 
          elif "GEOJSON" in ext.upper():  #no update possible -> hidden
            flType = "GeoJSON"
          elif "GML" in ext.upper():
            flType = "GML"
          elif 'TAB' in ext.upper():
            flType = 'MapInfo File'
          elif 'KML' in ext.upper():
            flType = 'KML'
          else:
            fName = fName + ".shp"
            flType = "ESRI Shapefile"
          return (fName , flType )
        else:
            return None
      
    def addPointGraphic(self, xy, color="#FFFF00", size=1, pen=10, markerType=QgsVertexMarker.ICON_BOX ):
        "create a point Graphic at location xy and return it"
        x, y = list( xy )[:2]
        m = QgsVertexMarker(self.canvas)
        m.setCenter(QgsPoint(x,y))
        m.setColor(QColor(color))
        m.setIconSize(size)
        m.setIconType(markerType) 
        m.setPenWidth(pen)
        return m

    @staticmethod
    def getBoundsOfPointArray( pointArray, delta=100):
        minX = 1.7976931348623157e+308
        maxX = -1.7976931348623157e+308
        minY = 1.7976931348623157e+308
        maxY = -1.7976931348623157e+308
    
        for xy in pointArray:
            x, y = list(xy)[:2]
            if x > maxX: maxX = x
            if x < minX: minX = x
            if y > maxY: maxY = y
            if y < minY: minY = y
          
        Xdelta = (maxX - minX) /delta
        Ydelta = (maxY - minY) /delta
        
        return [ minX - Xdelta, minY - Ydelta, maxX + Xdelta, maxY + Ydelta]
    
    @staticmethod
    def getBoundsOfPoint( x, y, delta=None):
      if delta is None:
        if x >= 360:
            delta = 300 #x bigger then 360 -> meters
        else:
            delta = 0.0025 #x smaller then 360 -> degrees
      
        xmax = x + delta
        xmin = x - delta
        ymax = y + delta
        ymin = y - delta
        
        return [xmin, ymin, xmax,ymax]