import json
import csv
import glob

# DEFINING
json_file_name_e1 = "/var/nfvShell/json/hpe_nfvsys_6125_portmap_e1.json"
json_file_name_e2 = "/var/nfvShell/json/hpe_nfvsys_6125_portmap_e2.json"

bay_port_1 = []
bay_port_2 = []
bay_port_3 = []
bay_port_4 = []
bay_port_5 = []
bay_port_6 = []
bay_port_7 = []
bay_port_8 = []
bay_port_9 = []
bay_port_10 = []
bay_port_11 = []
bay_port_12 = []
bay_port_13 = []
bay_port_14 = []
bay_port_15 = []
bay_port_16 = []

# PREPARING THE JSON FILE

excel_file = glob.glob('/mnt/base/*.json')
file_name = str(excel_file[0])
fo = open(file_name)
json_data = json.load(fo)
kit_id = json_data["hpe_nfvsystem"]["kit_type"]

if kit_id == "MSTRE1-4":
    kit_type = "1 Enclosure"
elif kit_id == "MSTRE1-8":
    kit_type = "1 Enclosure"
elif kit_id == "MSTRE1-16":
    kit_type = "1 Enclosure"
elif kit_id == "MSTRE2-16":
    kit_type = "2 Enclosure"
elif kit_id == "MSTRE2-32":
    kit_type = "2 Enclosure"


def prepare_json(file_name):
    fo = open(file_name)
    reader = csv.DictReader(fo)
    for row in reader:
        if row["Dest System"] == 'Server Bay 1':
            bay_port_1.append(row['SwitchSide'])
        if row["Dest System"] == 'Server Bay 2':
            bay_port_2.append(row['SwitchSide'])
        if row["Dest System"] == 'Server Bay 3':
            bay_port_3.append(row['SwitchSide'])
        if row["Dest System"] == 'Server Bay 4':
            bay_port_4.append(row['SwitchSide'])
        if row["Dest System"] == 'Server Bay 5':
            bay_port_5.append(row['SwitchSide'])
        if row["Dest System"] == 'Server Bay 6':
            bay_port_6.append(row['SwitchSide'])
        if row["Dest System"] == 'Server Bay 7':
            bay_port_7.append(row['SwitchSide'])
        if row["Dest System"] == 'Server Bay 8':
            bay_port_8.append(row['SwitchSide'])
        if row["Dest System"] == 'Server Bay 9':
            bay_port_9.append(row['SwitchSide'])
        if row["Dest System"] == 'Server Bay 10':
            bay_port_10.append(row['SwitchSide'])
        if row["Dest System"] == 'Server Bay 11':
            bay_port_11.append(row['SwitchSide'])
        if row["Dest System"] == 'Server Bay 12':
            bay_port_12.append(row['SwitchSide'])
        if row["Dest System"] == 'Server Bay 13':
            bay_port_13.append(row['SwitchSide'])
        if row["Dest System"] == 'Server Bay 14':
            bay_port_14.append(row['SwitchSide'])
        if row["Dest System"] == 'Server Bay 15':
            bay_port_15.append(row['SwitchSide'])
        if row["Dest System"] == 'Server Bay 16':
            bay_port_16.append(row['SwitchSide'])


prepare_json("/var/nfvShell/conf/6125_e1_1.csv")
prepare_json("/var/nfvShell/conf/6125_e1_2.csv")
prepare_json("/var/nfvShell/conf/6125_e1_3.csv")
prepare_json("/var/nfvShell/conf/6125_e1_4.csv")


# CREATING JSON FILE NOW

dict_6125 = {
    "BL1": bay_port_1,
    "BL2": bay_port_2,
    "BL3": bay_port_3,
    "BL4": bay_port_4,
    "BL5": bay_port_5,
    "BL6": bay_port_6,
    "BL7": bay_port_7,
    "BL8": bay_port_8,
    "BL9": bay_port_9,
    "BL10": bay_port_10,
    "BL11": bay_port_11,
    "BL12": bay_port_12,
    "BL13": bay_port_13,
    "BL14": bay_port_14,
    "BL15": bay_port_15,
    "BL16": bay_port_16

}

# DUMPING THE JSON FILE

fw = open(json_file_name_e1, "w")
json.dump(dict_6125, fw, indent=4)

if kit_type == "2 Enclosure":

    fi = open(json_file_name_e2, "w")
    json.dump(dict_6125, fi, indent=4)

print "Port map Json for 6125 successfully created"
