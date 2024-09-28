import os
import asyncio
from datetime import datetime


class AgentTrainer:
    """
    AgentTrainer can train and evaluate an agent for a reinforcement learning task.
    """

    def __init__(
        self, ensign=None, model_topic="agent-models", model_dir="./models", agent_id=1
    ):
        self.ensign = ensign
        self.model_topic = model_topic
        self.agent_id = agent_id
        self.model_dir = model_dir

    async def train(
        self, model, sessions=40, runs_per_session=4, model_version="0.1.0"
    ):
        """
        Train the agent for the specified number of steps.
        """

        model_name = model.__class__.__name__
        policy_name = model.policy.__class__.__name__

        if self.model_dir:
            os.makedirs(self.model_dir, exist_ok=True)

        # Train for the number of sessions
        for _ in range(sessions):
            session_start = datetime.now()
            model.learn(total_timesteps=model.n_steps * runs_per_session)
            session_end = datetime.now()
            duration = session_end - session_start

            # Ensure that async loggers have a chance to run
            await asyncio.sleep(5)

            if self.model_dir:
                model.save(
                    os.path.join(
                        self.model_dir,
                        "{}_{}.zip".format(
                            model_name, session_end.strftime("%Y%m%d-%H%M%S")
                        ),
                    )
                )

    async def eval(self, eval_topic="eval-agent", model_version="latest"):
        """
        Evaluate the agent in an independent testing environment using the specified
        model version or the latest model.
        """

    async def run(self, model_version="latest"):
        """
        Run the agent in "demo" mode using the model version.
        """

        pass
