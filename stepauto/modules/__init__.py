import stepauto.config as cfg


class StepMixin(object):
    def __init__(self, init_data):
        self.name = "X. Unsubclassed Step"
        self.config = cfg.get_config_parser()
        self.logger = cfg.get_logger()
        self.init_data = init_data

    def process(self):
        try:
            status = self.prep()
            if status["success"] is not True:
                self.logger.error(status["error"])
                return False
            self.run()
            self.cleanup()
            self.verify()

        except Exception:
            self.logger.exception('Step "%s" failed', self.name)
            return False

    def prep(self):
        """
        Verify that initial conditions for the step are met and possibly open the programs the step will be
        interacting with
        """
        return {"success": True, "error": ""}

    def run(self):
        """
        Do the actual thing the step is designed to accomplish
        """
        raise NotImplementedError

    def cleanup(self):
        """
        Remove any temporary files or resources generated during the run step
        """
        pass

    def verify(self):
        """
        Make sure this step ended up producing the artifacts it was supposed to, and (hopefully) that those artifacts
        are correct.
        """
        return {"success": True, "error": ""}
