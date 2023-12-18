from magicbot.state_machine import state, timed_state, AutonomousStateMachine

class BaseAuto(AutonomousStateMachine):
    """
    This class is used to end each autonomous mode.
    At the end of each mode either failed or finished will be called.
    Flushing the drive system reduces potential errrors.
    """

    @state
    def failed(self):
        """
        This state should only be called when an auto mode has failed.
        """
        self.next_state('finish')

    @state
    def finish(self):
        self.done()
