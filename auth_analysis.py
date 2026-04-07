import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("logs.csv")
print(data)

# timestamp
data["timestamp"] = pd.to_datetime(data["timestamp"])

# tri
data = data.sort_values(by=["username", "timestamp"]).reset_index(drop=True)

# off hours
data["off_hours"] = (data["timestamp"].dt.hour >= 22) | (data["timestamp"].dt.hour <= 6)

# previous values
data["prev_country"] = data.groupby("username")["country"].shift(1)
data["prev_device"] = data.groupby("username")["device"].shift(1)
data["prev_timestamp"] = data.groupby("username")["timestamp"].shift(1)

# new country/device
data["new_country"] = (data["country"] != data["prev_country"]) & data["prev_country"].notna()
data["new_device"] = (data["device"] != data["prev_device"]) & data["prev_device"].notna()

# time diff
data["time_diff"] = (data["timestamp"] - data["prev_timestamp"]).dt.total_seconds() / 60

# impossible travel
data["impossible_travel"] = (
    (data["country"] != data["prev_country"]) &
    (data["time_diff"] < 60) &
    data["prev_country"].notna()
)

#risk score
data["risk_score"] = 0

data.loc[data["status"] == "fail", "risk_score"] += 20
data.loc[data["off_hours"], "risk_score"] += 30
data.loc[data["new_country"], "risk_score"] += 40
data.loc[data["new_device"], "risk_score"] += 25
data.loc[data["impossible_travel"], "risk_score"] += 70

def classify_risk(score):
    if score >= 80:
        return "CRITICAL"
    elif score >= 50:
        return "HIGH"
    elif score >= 30:
        return "MEDIUM"
    else:
        return "LOW"

data["risk_level"] = data["risk_score"].apply(classify_risk)

print("\nFinal results:")
print(data[[
    "username",
    "timestamp",
    "status",
    "off_hours",
    "new_country",
    "new_device",
    "impossible_travel",
    "risk_score",
    "risk_level"
]])
