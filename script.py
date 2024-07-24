import re

# Đường dẫn đến file YAML
file_path = 'after-service.datadog.yaml'

# Đọc nội dung của file YAML
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Thay thế "golang" thành "go"
content = content.replace('golang', 'go')

# Thay thế "JavaScript" thành "javascript"
content = content.replace('JavaScript', 'javascript')
content = content.replace('Java', 'java')

# Ghi nội dung đã chỉnh sửa trở lại vào file YAML
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(content)

print("Đã thay thế 'golang' bằng 'go' và 'JavaScript' bằng 'javascript' thành công.")
