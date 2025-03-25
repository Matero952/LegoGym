# import numpy as np
#
# from envs.LegoStateSpace.TwoDim.LegoSpace import LegoSpace
#
#
# class ConstrainedRNGGenerator(LegoSpace):
#     def __init__(self, env_shape, seed):
#         super().__init__(env_shape, dtype=np.float16)
#         self._rng = np.random.default_rng(seed)
#     def generate(self):
#         while True:
#
#     def is_valid(self, world):
#         for r_idx, row in enumerate(world):
#             for c_idx, col in enumerate(row):
#                 return False if (
#                     ConstrainedRNGGenerator.is_occupied(row_idx=r_idx, col_idx=c_idx, world=world),
#                     not (ConstrainedRNGGenerator.in_bounds(row_idx=r_idx, col_idx=c_idx, world)),
#
#
#
#
#                 )
