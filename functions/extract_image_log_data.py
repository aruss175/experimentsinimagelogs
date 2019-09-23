
# python 3.6.8

# DLISIO v0.1.12

# Function purpose:  This will take the list of filepaths and find the specific curves of interest.  THey will be written to a
# list of dataframes and exported to csv by well.

import dlisio

def getimagedata(filepath_list, exportfolderpath = "...\\FORCE Data\\"):

    curves_L = []
    curves_name = []
    df_list = []
    for f in filepath_list:
        with dlisio.load(f) as file:
            for d in file:
                for origin in d.origin:
                    wellname = origin.well_name
                for fram in d.frames:
                    for channel in d.channels:
                        curvename = channel.name
                        if "TDEP" in curvename:
                            curves_L.append(channel.curves())
                            curves_name.append(curvename)
                        elif "GR" in curvename:
                            curves_L.append(channel.curves())
                            curves_name.append(curvename)
                        elif "STAT" in curvename:
                            curves_L.append(channel.curves())
                            curves_name.append(curvename)
                        elif "PAD" in curvename:
                            curves_L.append(channel.curves())
                            curves_name.append(curvename)
                        elif "DYN" in curvename:
                            curves_L.append(channel.curves())
                            curves_name.append(curvename)
                        else:
                            pass
    df = pd.DataFrame(data=curves_L, index=curves_name).T
    df['Wellname'] = wellname
    df_list.append(df)
    df.to_csv(exportfolderpath + wellname + ".csv")

    return df_list
