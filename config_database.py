import configparser
import subprocess


class ConfigDataBase:


    def __init__(self):
        current_branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).strip().decode("utf-8")

        if current_branch == "main":
            current_branch = "prd"
            self.active_environement = "PRD"
        elif current_branch == "tst":
            current_branch = "tst"
            self.active_environement = "TST"
        else:
            current_branch = "dev"
            self.active_environement = "DEV"


        config = configparser.ConfigParser()
        config.read(".config")
        self.database_name = config.get(current_branch, "database_name")
        
    def get_database_info(self) -> dict:
        """
        Get the database name and environment based on which git branch is activated
        :return database name
        """
        data_base_info = {"database name": f"databases//{self.database_name}", "environment": self.active_environement}
        return data_base_info

    