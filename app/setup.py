import os
# Add the variable ARGOS_PACKAGES_DIR to a variable in the system
os.environ['ARGOS_PACKAGES_DIR'] = './argos_packages'
import argostranslate.package
import argostranslate.translate
import logging
import json

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('argostranslate').setLevel(logging.DEBUG)
# print logs to console
# logging.getLogger().addHandler(logging.StreamHandler())


def install_packages(package_list: list=[], all: bool=False):
    argostranslate.package.update_package_index()

    available_packages = argostranslate.package.get_available_packages()
    installed_packages = argostranslate.package.get_installed_packages()

    # check of package is already installed
    remove_list = []
    for package in package_list:
        if package in installed_packages:
            logging.debug(f"{package} is already installed")
            remove_list.append(package)
    
    for package in remove_list:
        package_list.remove(package)

    # install all packages
    if all:
        for package in available_packages:
            if package not in installed_packages:
                logging.debug(f"Installing {i.to_code}")
                package.install()
    else:     
        # install specific packages
        for package in package_list:
            logging.debug(f"Installing {package}")
            package.install()
    
    installed_packages = argostranslate.package.get_installed_packages()

    from_to = {}
    for package in installed_packages:
        if package.from_code not in from_to:
            from_to[package.from_code] = []
        from_to[package.from_code].append(package.to_code)

    with open('installed_packages.json', 'w') as f:
        json.dump(from_to, f)

if __name__ == "__main__":
    # argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()

    pack_list = []

    for i in available_packages:
        if i.from_code == "en" and i.to_code == "fr":
            pack_list.append(i)

        if i.from_code == "fr" and i.to_code == "en":
            pack_list.append(i)
        
    install_packages(pack_list, False)
    
