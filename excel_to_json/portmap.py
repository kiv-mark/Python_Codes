import glob
import os
import logger
import sys
import time
from port_excel_csv import csv_from_excel
from port_csv_split import * 
from convert_portmap_json import *
from kit_details import *

json_path = "/var/nfvShell/json/"
csv_path = "/var/nfvShell/conf/"


class Create_portmap_json():
    """This class will take the excel file
       convert it to csv file, and later
       converts it to json file.
    """
    def __init__(self):
        pass

    def kit_type(self):
        """Checking the kit type
        """
        try:

            logger.logger.debug('Checking the kit type.')
            kit = KITDetails()
            kit_name = kit.check_starter_kit_type()
            if kit_name == "Enclosure":
                excel_file = glob.glob('/mnt/base/*.json')
                file_name = str(excel_file[0])
                fo = open(file_name)
                json_data = json.load(fo)
                kit_id = json_data["hpe_nfvsystem"]["kit_type"]

                if kit_id == "MSTRE1-4":
                    return "1 Enclosure"
                elif kit_id == "MSTRE1-8":
                    return "1 Enclosure"
                elif kit_id == "MSTRE1-16":
                    return "1 Enclosure"
                elif kit_id == "MSTRE2-16":
                    return "2 Enclosure"
                elif kit_id == "MSTRE2-32":
                    return "2 Enclosure"
                else:
                    return "Wrong Details"
        except Exception as e:
            logger.logger.debug(e)

    def copy_excel_file(self):
        try:
            excel_copy_file = glob.glob('/home/nfvadmin/NFV_CLI/cli/nfvShell/*.xlsx')
            file_name = str(excel_copy_file[0])
            logger.logger.debug("Copying "+file_name+" to /var/nfvShell/conf/")
            os.system(" cp "+file_name+"  /var/nfvShell/conf/")
            var_excel = glob.glob('/var/nfvShell/conf/*.xlsx')
            ex_name = str(var_excel[0])
            os.system("sudo chmod 777 "+ex_name)
            os.system("sudo chown nfvadmin "+ex_name)
            os.system("sudo chgrp nfvadmin "+ex_name)
            os.system("sudo rm -rf "+file_name)
        except Exception as e:
            logger.logger.debug(e)

    def excel_to_csv(self):
        """Converting the excel file to csv
        """

        try:
            logger.logger.debug('Converting the Portmap excel file to csv')
            excel_file = glob.glob('/var/nfvShell/conf/*.xlsx')
            file_name = str(excel_file[0])
            csv_from_excel(file_name)
            time.sleep(2)
            logger.logger.debug('Portmap excel file converted to csv')
        except Exception as e:
            logger.logger.debug(e)

    def csv_split(self):
        """Spliting the csv files
        """

        port_5900_csv = csv_path+"hpe_nfvsys_5900_portmap.csv"
        port_5950_csv = csv_path+"hpe_nfvsys_5950_portmap.csv"
        port_5950_mstrr_csv = csv_path+"hpe_nfvsys_mstrr_5950_portmap.csv"
        port_6125_split_e1_csv = csv_path+"hpe_nfvsys_6125_e1_portmap.csv"
        port_6125_split_e2_csv = csv_path+"hpe_nfvsys_6125_e2_portmap.csv"

        try:

            logger.logger.debug('Spliting the csv files')
            split_5900_cid(port_5900_csv)
            split_5950_cid(port_5950_csv)
            split_mstrr_5950_cid(port_5950_mstrr_csv)

            kit = KITDetails()
            kit_name = kit.check_starter_kit_type()
            if kit_name == "Enclosure":

                kit_details = self.kit_type()
                if kit_details == "2 Enclosure":
                    split_6125_cid(port_6125_split_e1_csv, 'e1')
                    split_6125_cid(port_6125_split_e2_csv, 'e2')
                else:
                    split_6125_cid(port_6125_split_e1_csv, 'e1')


            logger.logger.debug('Spliting the csv files Successful')

        except Exception as e:
            logger.logger.debug(e)

    def create_json(self):
        """Converting csv files to json
        """
        
        logger.logger.debug('Creating json of CSV..')
        try:
            logger.logger.debug('Creating JSON for 5900')
            create_5900_json(csv_path+"5900_1.csv", json_path+"hpe_nfvsys_5900_sw1_port.json")
            create_5900_json(csv_path+"5900_2.csv", json_path+"hpe_nfvsys_5900_sw2_port.json")

            logger.logger.debug('Creating JSON for 5950')
            create_5950_json(csv_path+"5950_1.csv", json_path+"hpe_nfvsys_5950_sw1_port.json")
            create_5950_json(csv_path+"5950_2.csv", json_path+"hpe_nfvsys_5950_sw2_port.json")

            logger.logger.debug('Creating JSON for 5950 Rackmount')
            create_5950_mstrr_json(csv_path+"5950_mstrr_1.csv", json_path+"hpe_nfvsys_5950_mstrr_sw1_port.json")
            create_5950_mstrr_json(csv_path+"5950_mstrr_2.csv", json_path+"hpe_nfvsys_5950_mstrr_sw2_port.json")

            kit = KITDetails()
            kit_name = kit.check_starter_kit_type()
            print kit_name
            if kit_name == "Enclosure":

                kit_details = self.kit_type()
                if kit_details == "2 Enclosure":
                    logger.logger.debug('Creating JSON for 2 6125')
                    create_6125_json(csv_path+"6125_e1_1.csv", json_path+"hpe_nfvsys_6125_e1_sw1_port.json")
                    create_6125_json(csv_path+"6125_e1_2.csv", json_path+"hpe_nfvsys_6125_e1_sw2_port.json")
                    create_6125_json(csv_path+"6125_e1_3.csv", json_path+"hpe_nfvsys_6125_e1_sw3_port.json")
                    create_6125_json(csv_path+"6125_e1_4.csv", json_path+"hpe_nfvsys_6125_e1_sw4_port.json")

                    create_6125_json(csv_path+"6125_e2_1.csv", json_path+"hpe_nfvsys_6125_e2_sw1_port.json")
                    create_6125_json(csv_path+"6125_e2_2.csv", json_path+"hpe_nfvsys_6125_e2_sw2_port.json")
                    create_6125_json(csv_path+"6125_e2_3.csv", json_path+"hpe_nfvsys_6125_e2_sw3_port.json")
                    create_6125_json(csv_path+"6125_e2_4.csv", json_path+"hpe_nfvsys_6125_e2_sw4_port.json")

                else:
                    logger.logger.debug('Creating JSON for 6125')
                    create_6125_json(csv_path+"6125_e1_1.csv", json_path+"hpe_nfvsys_6125_e1_sw1_port.json")
                    create_6125_json(csv_path+"6125_e1_2.csv", json_path+"hpe_nfvsys_6125_e1_sw2_port.json")
                    create_6125_json(csv_path+"6125_e1_3.csv", json_path+"hpe_nfvsys_6125_e1_sw3_port.json")
                    create_6125_json(csv_path+"6125_e1_4.csv", json_path+"hpe_nfvsys_6125_e1_sw4_port.json")
            
                os.system("python port_csv_json.py")

            else:
                os.system("python port_csv_json_mstrr.py")

            print "Port map Json for 5900 successfully created"
            print "Port map Json for 5950 successfully created"

        except Exception as e:
            logger.logger.debug(e)


if __name__ == "__main__":
    logger.logger.debug("Creating object")
    print ("Creating object")
    obj = Create_portmap_json()
    obj.copy_excel_file()
    obj.excel_to_csv()
    obj.csv_split()
    obj.create_json()

    fo = open("/mnt/base/component_initial_config/hpe_nfvsys_nfvseedvm.json")
    json_data = json.load(fo)
    seedvm_ip = json_data["nfvseed_vm_nfv_pxeip"]
    seedvm_user = json_data["nfvseed_vm_user"]
    seedvm_password = json_data["nfvseed_vm_password"]

    try:
        os.system('sshpass -p'+seedvm_password+' scp /var/nfvShell/json/* '+seedvm_user+'@'+seedvm_ip+':/depot/hpe_nfvsystem/common/schema/nsds/base/component_initial_config/')
    except Exception as e:
        logger.logger.debug(e)
