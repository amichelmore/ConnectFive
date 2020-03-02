from gym.envs.registration import register

register(
    id='cf-v0',
    entry_point='connect_five.envs:CfEnv',
)