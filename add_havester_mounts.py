import yaml

chia_config_file = '/root/.chia/mainnet/config/config.yaml'

red='\033[0;31m'
yellow='\033[0;33m'
green='\033[0;32m'
white='\033[0;37m'
blue='\033[0;34m'
nc='\033[0m'


# taken from: https://github.com/rjsears/chia_plot_manager/blob/main/auto_drive/auto_drive.py
def update_chia_config(mountpoint):
    """
    This function adds the new mountpoint to your chia configuration file.
    """
    try:
        with open(chia_config_file) as f:
            chia_config = yaml.safe_load(f)
            if mountpoint in chia_config['harvester']['plot_directories']:
                print(f'{green}Mountpoint {red}Already{nc} Exists - We will not add it again!')
                return True
            else:
                chia_config['harvester']['plot_directories'].append(mountpoint)
    except IOError:
        print(f'{red}ERROR{nc} opening {yellow}{chia_config_file}{nc}! Please check your {yellow}filepath{nc} and try again!')
        return False
    try:
        with open(chia_config_file, 'w') as f:
            yaml.safe_dump(chia_config, f)
            return True
    except IOError:
        print(f'{red}ERROR{nc} opening {yellow}{chia_config_file}{nc}! Please check your {yellow}filepath{nc} and try again!')
        return False

for x in range(1, 8):
    update_chia_config('/plots' + str(x))