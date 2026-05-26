import os
import pandas as pd

# -------------------------
# Source Root Directories
# -------------------------

SOURCE_ZONES = [
    "data/raw",
    "data/streaming",
    "data/cdc",
    "data/logs"
]

metadata = []

# -------------------------
# Scan Source Zones
# -------------------------

for zone_path in SOURCE_ZONES:

    zone_name = zone_path.split("/")[-1]

    for file in os.listdir(zone_path):

        file_path = os.path.join(zone_path, file)

        if os.path.isfile(file_path):

            table_name = file.split(".")[0]
            file_format = file.split(".")[-1]

            # Infer load type
            if zone_name == "raw":
                load_type = "batch"

            elif zone_name == "cdc":
                load_type = "cdc"

            else:
                load_type = "stream"

            # Infer checkpoint requirement
            checkpoint_required = (
                "true"
                if load_type in ["stream", "cdc"]
                else "false"
            )

            metadata.append({
                "table_name": table_name,
                "source_zone": zone_name,
                "file_format": file_format,
                "load_type": load_type,
                "checkpoint_required": checkpoint_required
            })

# -------------------------
# Create Metadata DataFrame
# -------------------------

metadata_df = pd.DataFrame(metadata)

# -------------------------
# Save Metadata Config
# -------------------------

os.makedirs("config", exist_ok=True)

metadata_df.to_csv(
    "config/auto_bronze_config.csv",
    index=False
)

print("Metadata discovery completed successfully.")
print(metadata_df)