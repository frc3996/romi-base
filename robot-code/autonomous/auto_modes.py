from .base_auto import BaseAuto
import math
from magicbot.state_machine import state, timed_state, AutonomousStateMachine
from components import tankdrive

class BaseAuto(AutonomousStateMachine):
    """
    Cette classe est utilisée pour terminer les divers mode autonomes.
    l'état 'failed' ou 'finish' devrait être appelé une fois terminé.
    """

    drive: tankdrive.TankDrive

    @state
    def failed(self):
        """
        Cet état est appelé par défaut si un mode auto a échoué
        """
        self.next_state("finish")

    @state
    def finish(self):
        self.drive.flush()
        self.done()
