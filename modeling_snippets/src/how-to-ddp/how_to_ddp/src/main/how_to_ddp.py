import os

import torch  # type: ignore


class Network(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x


class Model:
    def __init__(self) -> None:
        self.network: torch.nn.Module = Network()

    def ddp_setup(self, rank: int, world_size: int) -> None:
        os.environ["MASTER_ADDR"] = "localhost"
        os.environ["MASTER_PORT"] = "12355"

        torch.distributed.init_process_group("nccl", rank=rank, world_size=world_size)
        torch.cuda.set_device(rank)

        self.network = self.network.to(rank)
        self.network = torch.nn.parallel.DistributedDataParallel(
            self.network, device_ids=[rank], find_unused_parameters=True
        )

    def train(
        self,
        rank: int,
        world_size: int,
        dataset_train: torch.utils.data.Dataset,
        dataset_valid: torch.utils.data.Dataset,
    ) -> None:
        self.ddp_setup(rank, world_size)

        epochs: int = 5
        for epoch_idx in range(epochs):
            for batch_idx, batch in enumerate(dataset_train):
                pass


class HowToDDP:
    def __init__(self):
        self.world_size: int = torch.cuda.device_count()
        torch.multiprocessing.set_start_method("spawn")

    def __call__(self):
        dataset_train, dataset_valid = None, None
        model: Model = Model()
        torch.multiprocessing.spawn(
            model.train,
            args=(self.world_size, dataset_train, dataset_valid),
            nprocs=self.world_size,
            join=True,
        )


if __name__ == "__main__":
    HowToDDP()()
