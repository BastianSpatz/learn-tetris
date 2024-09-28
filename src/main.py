import asyncio
from src.agent import AgentTrainer
from src.environment.tetris_environment import TetrisEnv

from stable_baselines3 import PPO


async def train():
    # Configure the environment, model, and trainer
    env = TetrisEnv(
        gb_path=r"C:\Users\Admin\Downloads\Tetris\Tetris.gb",
    )
    trainer = AgentTrainer()
    model = PPO(
        "MlpPolicy",
        env,
        verbose=2,
        n_steps=2048,
        batch_size=64,
        n_epochs=10,
        gamma=0.99,
        device="cuda",
    )

    await trainer.train(model)


if __name__ == "__main__":
    asyncio.run(train())
