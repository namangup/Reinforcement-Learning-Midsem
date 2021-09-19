from gym.envs.registration import register

register(
    id = 'random-maze-env-v0',
    entry_point = 'gym_env.envs:RandomMazeEnvironment'
)
