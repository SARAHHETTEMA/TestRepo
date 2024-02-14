'''
 Name: Sarah Hettema
 Date: 2/13/2024

Purpose: Lab 4A:  Working with tables
'''

print ( "*** Lab 4A Script by Sarah Hettema starting")

#import modules
print("\nImport Modules")
import arcpy

# Set environments and variables
# Set the workspace to your copy of the UnionCity GDB
print("Set environments and variables")
path = r"N:\Classes\workspace\HettemaS\Lab 4\Lesson4LabData\PSA Book Ch 8 Data"

arcpy.env.workspace = path
arcpy.env.overwriteOutput = True


# Q1) write the code to create a cursor and return each airport name.
print("\nQ1) Create a cursor and return each airport name.")
# Syntax: arcpy.da.SearchCursor(in_table, field_names, {where_clause}, {spatial_reference},
# {explode_to_points}, {sql_clause}, {datum_transformation}, {spatial_filter}, {spatial_relationship}, {search_order})
airport = "airports.shp"

with arcpy.da.SearchCursor(airport, ["Name"], "TOT_ENP > 100000") as cur_air:
    numrows = 0
    for row in cur_air:
        print("Airport Name = " + row[0])
        # Add a counter to the loop to only print out the first 10 records
        numrows += 1


# Q2) return those records with a TOT_ENP value greater than 100000
print("\nQ2) return those records with a TOT_ENP value greater than 100000")
# added: "TOT_ENP > 100000"
print(f"{numrows} airports have a TOT_ENP value of greater than 100,000")

# Q3) Make copy of original data
print("\nQ3)")
print("Original data can be found in: airports_original.shp")
print("Create update cursor")
# Syntax: arcpy.da.UpdateCursor(in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points},
# {sql_clause}, {datum_transformation}, {explicit}, {spatial_filter}, {spatial_relationship}, {search_order})

with arcpy.da.UpdateCursor(airport, ["STATE"], "STATE <> 'AK'") as cur_AK:
    print("Updating fields....")
    for row in cur_AK:
        row[0] = "AK"
        cur_AK.updateRow(row)

print(f"\nScript ran successfully. Check {airport} fields to see if correctly updated.")