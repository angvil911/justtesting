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

                    # 3. Replace common Bootstrap classes with new Tailwind classes
                    content = content.replace('class="btn btn-primary"', 'class="h-9 px-4 inline-flex items-center gap-2 bg-gray-900 text-white dark:bg-white dark:text-gray-900 text-sm font-medium rounded-lg hover:opacity-90 transition-opacity"')
                    content = content.replace('class="btn btn-danger"', 'class="h-9 px-4 inline-flex items-center gap-2 bg-red-600 text-white text-sm font-medium rounded-lg hover:bg-red-700 transition-colors"')
                    content = content.replace('class="btn btn-success"', 'class="h-9 px-4 inline-flex items-center gap-2 bg-green-600 text-white text-sm font-medium rounded-lg hover:bg-green-700 transition-colors"')
                    content = content.replace('class="btn btn-info"', 'class="h-9 px-4 inline-flex items-center gap-2 bg-blue-600 text-white text-sm font-medium rounded-lg hover:bg-blue-700 transition-colors"')
                    content = content.replace('class="btn btn-default"', 'class="h-9 px-4 inline-flex items-center gap-2 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 text-sm font-medium rounded-lg hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"')
                    
                    content = content.replace('class="form-control"', 'class="w-full h-10 px-3 bg-white dark:bg-[#1a1a1a] border border-gray-200 dark:border-gray-800 rounded-lg text-sm text-gray-900 dark:text-white focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-colors"')
                    content = content.replace('class="table"', 'class="w-full text-left text-sm text-gray-600 dark:text-gray-400 border-collapse"')
                    content = content.replace('class="table table-striped"', 'class="w-full text-left text-sm text-gray-600 dark:text-gray-400 border-collapse"')
                    content = content.replace('class="table table-bordered"', 'class="w-full text-left text-sm text-gray-600 dark:text-gray-400 border-collapse border border-gray-200 dark:border-gray-800"')
                    content = content.replace('class="card"', 'class="bg-white dark:bg-[#111111] rounded-2xl border border-gray-200 dark:border-gray-800 shadow-sm overflow-hidden"')

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
