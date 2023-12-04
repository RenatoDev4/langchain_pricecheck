import json

config_list = [
    {
        "model": "gpt-3.5-turbo",
        "api_key": "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",
    }
]

with open("OAI_CONFIG_LIST.json", "w") as f:
    json.dump(config_list, f)
