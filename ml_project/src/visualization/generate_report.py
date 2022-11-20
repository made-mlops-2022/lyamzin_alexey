#!/usr/bin/env python3
import hydra
import pandas as pd
from pandas_profiling import ProfileReport
from configs.profile import ProfileConfig
from hydra.core.config_store import ConfigStore

cs = ConfigStore.instance()
cs.store(name='profile', node=ProfileConfig)


@hydra.main(version_base=None, config_name='profile')
def generate_report(cfg: ProfileConfig) -> None:
    df = pd.read_csv(cfg.input_data)
    profile = ProfileReport(df, title=cfg.title, explorative=cfg.explorative)
    profile.to_file(cfg.out_path)


if __name__ == "__main__":
    generate_report()
