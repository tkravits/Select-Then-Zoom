import arcpy

# uses the mxd that is running this code
mxd = arcpy.mapping.MapDocument("CURRENT")
# df is the dataframe, Layers is used to run through all the layers within the mxd. Leave Layers as is
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
# lyr sets the layer, needs to be spelt exactly as the layer sits in ArcMap
lyr = arcpy.mapping.ListLayers(mxd, "BOGO.PARCELS.PARCELS", df)[0]
arcpy.env.overwriteOutput = True

# sets the parameters, this must be setup in the toolbox script
arcpy.AddMessage("Workspace added")
FClass = arcpy.GetParameterAsText(0)
Field = arcpy.GetParameterAsText(1)
Feature = arcpy.GetParameterAsText(2)

# sets the Feature parameter equal to the user input string
where_clause = """{} = '{}'""".format(arcpy.AddFieldDelimiters(FClass, Field),
                                      Feature)  # I have added extra pair of single quotes for selecting strings
arcpy.AddMessage(where_clause)
# selects the attribute using the string the user input
arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", where_clause)
# zooms to selected feature
df.zoomToSelectedFeatures()
# great job!
arcpy.RefreshActiveView()
arcpy.AddMessage("All done!")
