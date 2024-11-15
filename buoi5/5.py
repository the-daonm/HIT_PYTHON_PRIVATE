# Tạo từ điển
docker_compose = {
    "version": "3.8",
    "services": {
        "app": {
            "image": "python:3.10-slim",
            "command": "python app.py",
            "volumes": "./app:/app",
            "restart": "always",
            "ports": "5000:5000",
            "depends_on": "db"
        }
    }
}

print("Ban dau:")
print(docker_compose)

docker_compose["version"] = "3.10"
print("\nSau khi sua version:")
print(docker_compose)

image_value = docker_compose["services"]["app"]["image"]
print("\nGia tri cua key 'image':", image_value)

docker_compose["services"]["app"]["environment"] = ["PYTHONUNBUFFERED=1"]
print("\nSau khi them key 'environment':")
print(docker_compose)

contains_volumes = "volumes" in docker_compose["services"]["app"]
print("\nChua key 'volumes'?", contains_volumes)

del docker_compose["services"]["app"]["depends_on"]
print("\nSau khi xoa key 'depends_on':")
print(docker_compose)

key_count = len(docker_compose["services"]["app"])
print("\nSo key trong dictionary:", key_count)

all_values = list(docker_compose["services"]["app"].values())
print("\nDanh sach cac gia tri trong dictionary:")
print(all_values)

contains_always = "always" in docker_compose["services"]["app"].values()
print("\n'Always' la value?", contains_always)

new_key = input("\nNew key: ")
new_value = input("Value: ")
docker_compose["services"]["app"][new_key] = new_value
print("\nSau khi them key:")
print(docker_compose)
