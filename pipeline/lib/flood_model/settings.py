
##################
## LOAD SECRETS ##
##################

# 1. Try to load secrets from Azure key vault (i.e. when running through Logic App) if user has access
try:
    from azure.identity import DefaultAzureCredential
    from azure.keyvault.secrets import SecretClient
    az_credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url='https://ibf-flood-keys.vault.azure.net', credential=az_credential)

    ADMIN_LOGIN = secret_client.get_secret("ADMIN-LOGIN").value
    GLOFAS_USER = secret_client.get_secret("GLOFAS-USER").value
    GLOFAS_PW = secret_client.get_secret("GLOFAS-PW").value
    #GOOGLE_DRIVE_DATA_URL = secret_client.get_secret("GOOGLE-DRIVE-DATA-URL").value
    UGA_URL=secret_client.get_secret("UGA-URL").value
    ZMB_URL=secret_client.get_secret("ZMB-URL").value
    ETH_URL=secret_client.get_secret("ETH-URL").value
    KEN_URL=secret_client.get_secret("KEN-URL").value
    PHL_URL=secret_client.get_secret("PHL-URL-test").value
    UGA_PASSWORD=secret_client.get_secret("UGA-PASSWORD").value
    ZMB_PASSWORD=secret_client.get_secret("ZMB-PASSWORD").value
    ETH_PASSWORD=secret_client.get_secret("ETH-PASSWORD").value
    KEN_PASSWORD=secret_client.get_secret("KEN-PASSWORD").value
    PHL_PASSWORD=secret_client.get_secret("PHL-PASSWORD-test").value
    
    DATALAKE_STORAGE_ACCOUNT_NAME = secret_client.get_secret("DATALAKE-STORAGE-ACCOUNT-NAME").value
    DATALAKE_STORAGE_ACCOUNT_KEY = secret_client.get_secret("DATALAKE-STORAGE-ACCOUNT-KEY").value
    DATALAKE_API_VERSION = '2018-11-09'
 


except Exception as e:
    print('No access to Azure Key vault, skipping.')

# 2. Try to load secrets from env-variables (i.e. when using Github Actions)
try:
    import os
    
    ADMIN_LOGIN = os.environ['ADMIN_LOGIN']
    GLOFAS_USER = os.environ['GLOFAS_USER']
    GLOFAS_PW = os.environ['GLOFAS_PW']
    #GOOGLE_DRIVE_DATA_URL = os.environ['GOOGLE_DRIVE_DATA_URL']
    UGA_URL=os.environ['UGA_URL']
    ZMB_URL=os.environ['ZMB_URL']
    ETH_URL=os.environ['ETH_URL']
    KEN_URL=os.environ['KEN_URL']
    PHL_URL=os.environ['PHL_URL']
    UGA_PASSWORD=os.environ['UGA_PASSWORD']
    ZMB_PASSWORD=os.environ['ZMB_PASSWORD']
    ETH_PASSWORD=os.environ['ETH_PASSWORD']
    KEN_PASSWORD=os.environ['KEN_PASSWORD']
    PHL_PASSWORD=os.environ['PHL_PASSWORD']
    DATALAKE_STORAGE_ACCOUNT_NAME = os.environ['DATALAKE-STORAGE-ACCOUNT-NAME']
    DATALAKE_STORAGE_ACCOUNT_KEY = os.environ['DATALAKE-STORAGE-ACCOUNT-KEY']
    DATALAKE_API_VERSION = '2018-11-09'

except Exception as e:
    print('No environment variables found.')

# 3. If 1. and 2. both fail, then assume secrets are loaded via secrets.py file (when running locally). If neither of the 3 options apply, this script will fail.
try:
    from flood_model.secrets import *
except ImportError:
    print('No secrets file found.')


######################
## COUNTRY SETTINGS ##
######################

# Countries to include
COUNTRY_CODES = ['ZMB','KEN','ETH','UGA'] #'PHL'

SETTINGS = {
    "ZMB": {
        "IBF_API_URL": ZMB_URL,
        "PASSWORD": ZMB_PASSWORD,
        "mock": False,
        "if_mock_trigger": False,
        "notify_email": True,
        'lead_times': {
            "7-day": 7
        },
        'admin_level': 3,
        'levels':[3,2,1],
        'GLOFAS_FTP':'data-portal.ecmwf.int/ZambiaRedcross_glofas_point/',
        'GLOFAS_FILENAME':'glofas_pointdata_ZambiaRedcross',   
        'EXPOSURE_DATA_SOURCES': {
            "population": {
                "source": "population/hrsl_zmb_pop_resized_100",
                "rasterValue": 1
            }
        }
    },
    "UGA": {
        "IBF_API_URL": UGA_URL,
        "PASSWORD": UGA_PASSWORD,
        "mock": False,
        "if_mock_trigger": False,
        "notify_email": True,
        'lead_times': {
            "5-day": 5
        },
        'admin_level': 4,
        'levels':[4,3,2,1],
        'GLOFAS_FTP':'data-portal.ecmwf.int/ZambiaRedcross_glofas_point/',
        'GLOFAS_FILENAME':'glofas_pointdata_ZambiaRedcross',   
        'EXPOSURE_DATA_SOURCES': {
            "population": {
                "source": "population/hrsl_uga_pop_resized_100",
                "rasterValue": 1
            }
        }
    },
    "KEN": {
        "IBF_API_URL": KEN_URL,
        "PASSWORD": KEN_PASSWORD,
        "mock": False,
        "if_mock_trigger": False,
        "notify_email": True,
        'lead_times': {
            "7-day": 7
        },
        'admin_level': 3,
        'levels':[3,2,1],
        'GLOFAS_FTP':'data-portal.ecmwf.int/ZambiaRedcross_glofas_point/',
        'GLOFAS_FILENAME':'glofas_pointdata_ZambiaRedcross',   
        'EXPOSURE_DATA_SOURCES': {
            "population": {
                "source": "population/hrsl_ken_pop_resized_100",
                "rasterValue": 1
            }
        }
    },
    "ETH": {
        "IBF_API_URL": ETH_URL,
        "PASSWORD": ETH_PASSWORD,
        "mock": False,
        "if_mock_trigger": False,
        "notify_email": True,
        'lead_times': {
            "7-day": 7
        },
        'admin_level': 3,
        'levels':[3],
        'GLOFAS_FTP':'data-portal.ecmwf.int/ZambiaRedcross_glofas_point/',
        'GLOFAS_FILENAME':'glofas_pointdata_ZambiaRedcross',   
        'EXPOSURE_DATA_SOURCES': {
            "population": {
                "source": "population/worldpop_eth",
                "rasterValue": 1
            }
        }
    },
    "PHL": {
        "IBF_API_URL": PHL_URL,
        "PASSWORD": PHL_PASSWORD,
        "mock": False,
        "if_mock_trigger": False,
        "notify_email": True,
        'lead_times': {
            "3-day": 3
        },
        'admin_level': 3,
        'levels':[3,2,1],
        'GLOFAS_FTP':'data-portal.ecmwf.int/RedcrossPhilippines_glofas_point/',
        'GLOFAS_FILENAME':'glofas_pointdata_RedcrossPhilippines', 
        'EXPOSURE_DATA_SOURCES': {
            "population": {
                "source": "population/hrsl_phl_pop_resized_10",
                "rasterValue": 1
            }
        }
    }
}





# Change this date only in case of specific testing purposes
from datetime import date, timedelta
CURRENT_DATE = date.today()
#CURRENT_DATE=date.today() - timedelta(1) # to use yesterday's date




####################
## OTHER SETTINGS ##
####################
GOOGLE_DRIVE_DATA_URL = 'https://drive.google.com/file/d/14MbG4uFPGJCduM5aLkvgSGqA8io6Gh9C/view?usp=sharing'

TRIGGER_LEVELS = {
    "minimum": 0.6,
    "medium": 0.7,
    "maximum": 0.8
}



###################
## PATH SETTINGS ##
###################
RASTER_DATA = 'data/raster/'
RASTER_INPUT = RASTER_DATA + 'input/'
RASTER_OUTPUT = RASTER_DATA + 'output/'
PIPELINE_DATA = 'data/other/'
PIPELINE_INPUT = PIPELINE_DATA + 'input/'
PIPELINE_OUTPUT = PIPELINE_DATA + 'output/'
TRIGGER_DATA_FOLDER='data/trigger_data/triggers_rp_per_station/'
TRIGGER_DATA_FOLDER_TR='data/trigger_data/glofas_trigger_levels/'
STATION_DISTRICT_MAPPING_FOLDER='data/trigger_data/station_district_mapping/'

#########################
## INPUT DATA SETTINGS ##
#########################

# Glofas input
#GLOFAS_FTP = 'data-portal.ecmwf.int/ZambiaRedcross_glofas_point/'
#GLOFAS_FILENAME = 'glofas_pointdata_ZambiaRedcross'


#####################
## ATTRIBUTE NAMES ##
#####################

TRIGGER_LEVEL = 'triggerLevel'
LEAD_TIME = 'leadTime'
