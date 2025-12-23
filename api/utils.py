import os
import json
import logging

from infra_terraform.backend import get_terraform_backend

def get_terraform_config(file_path):
    """
    Reads Terraform configuration from a JSON file.

    :param file_path: Path to the Terraform configuration file.
    :return: A dictionary containing the Terraform configuration.
    """
    with open(file_path) as f:
        return json.load(f)

def get_terraform_backend(root_dir):
    """
    Returns the Terraform backend configuration for the given root directory.

    :param root_dir: The root directory of the Terraform project.
    :return: The Terraform backend configuration as a dictionary.
    """
    return get_terraform_backend(root_dir)

def get_terraform_outputs(terraform_config):
    """
    Extracts the Terraform outputs from the given configuration.

    :param terraform_config: The Terraform configuration as a dictionary.
    :return: A dictionary containing the Terraform outputs.
    """
    return terraform_config.get('outputs', {})

def get_terraform_variables(terraform_config):
    """
    Extracts the Terraform variables from the given configuration.

    :param terraform_config: The Terraform configuration as a dictionary.
    :return: A dictionary containing the Terraform variables.
    """
    return terraform_config.get('variables', {})

def get_terraform_backend_config(terraform_config):
    """
    Extracts the Terraform backend configuration from the given configuration.

    :param terraform_config: The Terraform configuration as a dictionary.
    :return: The Terraform backend configuration as a dictionary.
    """
    return terraform_config.get('backend', {})

def configure_logging():
    """
    Configures the logging module.
    """
    logging.basicConfig(level=logging.INFO)