from dataclasses import dataclass, field


@dataclass
class ProfileConfig:
    title: str = field(default="EDA. Profile Report.")
    input_data: str = field(default="data/raw/heart_cleveland_upload.csv")
    out_path: str = field(default="reports/eda_profile.html")
    profile_config: str = field(default="configs/profile_config.yml")
    explorative: bool = field(default=False)
