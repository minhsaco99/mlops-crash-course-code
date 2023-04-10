from feast import FeatureStore

store = FeatureStore(repo_path="../feature_repo")

features = store.get_online_features(
    features=["driver_stats:acc_rate", "driver_stats:conv_rate"],
    entity_rows=[{"driver_id": 1001},
        {"driver_id": 1002}],
).to_dict(include_event_timestamps=False)


def print_online_features(features):
    for key, value in sorted(features.items()):
        print(key, " : ", value)


print_online_features(features)
