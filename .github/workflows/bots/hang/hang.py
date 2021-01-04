from sc2 import run_game, maps, Race, Difficulty, BotAI
from sc2.player import Bot, Computer
import time

class hang(BotAI):
    def __init__(self):
        super().__init__()
        self.actions = []

    async def on_step(self, iteration):
        self.actions = []

        if iteration == 0:
            target = self.enemy_start_locations[0]

            for worker in self.workers:
                self.actions.append(worker.attack(target))
        
        if iteration > 10:
            time.sleep(2000)


        await self.do_actions(self.actions)
