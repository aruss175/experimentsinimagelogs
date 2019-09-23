
# python 3.6.8

# DLISIO v0.1.12

# Function purpose:  This will take input of a folder path, and if you like you can change the string match for the curve
# or for the processing program.  The best defaults are currently filled in.  The function will run through a folder,
# search for the dlis files matching the criteria and return a list of those file paths, a list of well names it matched,
# and a list of well names it did not match.

import os

import dlisio

def gogetimages(folderpath, curvetofind = 'DYN', how = "Techlog"):
    no_match_well_list = []
    filepath_list = []
    found_well_list = []
    for (root, dirs, files) in os.walk(folderpath):
        for f in files:
            filepath = os.path.join(root, f)
            if filepath.endswith('.' + 'dlis') or filepath.endswith('.' + 'DLIS'):
                print(filepath)
                try:
                    with dlisio.load(filepath) as file:
                        for d in file:
                            for origin in d.origin:
                                created = origin.product
                                wellname = origin.well_name
                                if how in created:
                                    for channel in d.channels:
                                        curvename = channel.name
                                        if curvetofind in curvename:
                                            filepath_list.append(filepath)
                                            found_well_list.append(wellname)
                                        else:
                                            no_match_well_list.append(wellname)
                                else:
                                    for channel in d.channels:
                                        curvename = channel.name
                                        if curvetofind in curvename:
                                            filepath_list.append(filepath)
                                            found_well_list.append(wellname)
                                        else:
                                            no_match_well_list.append(wellname)
                except:
                    print("cannot read filepath " + filepath)
                    continue
    filepath_list = list(set(filepath_list))
    return filepath_list, found_well_list, no_match_well_list
