from torch import nn, Tensor
from typing import Optional

from . import register_norm_fn


@register_norm_fn(name="sync_batch_norm")
class SyncBatchNorm(nn.SyncBatchNorm):
    def __init__(self,
                 num_features: int,
                 eps: Optional[float] = 1e-5,
                 momentum: Optional[float] = 0.1,
                 affine: bool = True,
                 track_running_stats: bool = True
                 ):
        super(SyncBatchNorm, self).__init__(num_features=num_features, eps=eps, momentum=momentum, affine=affine,
                                            track_running_stats=track_running_stats)

    def profile_module(self, input: Tensor) -> (Tensor, float, float):
        # Since normalization layers can be fused, we do not count their operations
        params = sum([p.numel() for p in self.parameters()])
        return input, params, 0.0
