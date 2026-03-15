import os
import logging
from typing import Dict, List

class TerraformUtils:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.logger = logging.getLogger(__name__)

    def get_terraform_files(self) -> List[str]:
        terraform_files = []
        for root, dirs, files in os.walk(self.root_dir):
            for file in files:
                if file.endswith('.tf') or file.endswith('.tfvars'):
                    terraform_files.append(os.path.join(root, file))
        return terraform_files

    def load_tfvars(self, file_path: str) -> Dict:
        tfvars = {}
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    tfvars[key.strip()] = value.strip().strip('"')
        return tfvars

    def validate_terraform_config(self, config_file: str) -> bool:
        try:
            with open(config_file, 'r') as file:
                for line in file:
                    if 'terraform {' in line:
                        return True
        except FileNotFoundError:
            self.logger.error(f"Config file '{config_file}' not found")
        return False