import os
import re

def bulk_refactor(directory):
    icon_map = {
        'fa-server': 'ti-server',
        'fa-cog': 'ti-settings',
        'fa-database': 'ti-database',
        'fa-users': 'ti-users',
        'fa-globe': 'ti-world',
        'fa-lock': 'ti-lock',
        'fa-unlock': 'ti-lock-open',
        'fa-check': 'ti-check',
        'fa-times': 'ti-x',
        'fa-plus': 'ti-plus',
        'fa-trash': 'ti-trash',
        'fa-pencil': 'ti-pencil',
        'fa-download': 'ti-download',
        'fa-upload': 'ti-upload',
        'fa-arrow-right': 'ti-arrow-right',
        'fa-arrow-left': 'ti-arrow-left',
        'fa-info-circle': 'ti-info-circle',
        'fa-exclamation-triangle': 'ti-alert-triangle'
    }

    modified_count = 0

    for root, dirs, files in os.walk(directory):
        # Skip static assets
        if 'static' in root.split(os.sep):
            continue

        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    original_content = content

                    # 1. Replace FontAwesome prefixes
                    content = re.sub(r'fas\s+fa-([a-zA-Z0-9-]+)', lambda m: f"ti ti-{m.group(1)}", content)
                    content = re.sub(r'fab\s+fa-([a-zA-Z0-9-]+)', lambda m: f"ti ti-{m.group(1)}", content)
                    content = re.sub(r'fa\s+fa-([a-zA-Z0-9-]+)', lambda m: f"ti ti-{m.group(1)}", content)

                    # 2. Map specific icons
                    for old, new in icon_map.items():
                        content = content.replace(f'ti-{old[3:]}', new)

                    # 3. Replace common Bootstrap classes with new Design System classes
                    content = content.replace('class="btn btn-primary"', 'class="cp-btn cp-btn-primary"')
                    content = content.replace('class="btn btn-danger"', 'class="cp-btn cp-btn-danger"')
                    content = content.replace('class="btn btn-success"', 'class="cp-btn cp-btn-primary"')
                    content = content.replace('class="btn btn-info"', 'class="cp-btn cp-btn-secondary"')
                    content = content.replace('class="btn btn-default"', 'class="cp-btn cp-btn-secondary"')
                    
                    content = content.replace('class="form-control"', 'class="cp-input"')
                    content = content.replace('class="table"', 'class="cp-table"')
                    content = content.replace('class="table table-striped"', 'class="cp-table"')
                    content = content.replace('class="table table-bordered"', 'class="cp-table"')
                    content = content.replace('class="card"', 'class="cp-card"')

                    if content != original_content:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        modified_count += 1
                        print(f"Refactored: {path}")

                except Exception as e:
                    print(f"Error processing {path}: {e}")

    print(f"\\nBulk refactor complete. Modified {modified_count} files.")

if __name__ == "__main__":
    target_dir = "c:\\\\Users\\\\HP\\\\Videos\\\\devasystem-test\\\\cyberpanel-stable"
    print(f"Starting bulk refactoring in {target_dir}...")
    bulk_refactor(target_dir)
