import os
import re

def refactor_filemanager_tailwind():
    path = r"c:\Users\HP\Videos\devasystem-test\cyberpanel-stable\filemanager\templates\filemanager\index.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Inject Tailwind CDN
    cdn_script = """
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    },
                }
            }
        }
    </script>
    """
    if 'cdn.tailwindcss.com' not in content:
        content = content.replace('</head>', f'{cdn_script}</head>')
    
    # Remove custom design-system.css
    content = re.sub(r'<link rel="stylesheet"[^>]*design-system\.css[^>]*>', '', content)

    # Remove the large style block
    start_str = '<style>'
    end_str = '</style>'
    if start_str in content:
        start_idx = content.find(start_str)
        end_idx = content.find(end_str, start_idx) + len(end_str)
        content = content[:start_idx] + content[end_idx:]

    # Add tailwind classes
    content = content.replace('<body ng-app="fileManager"', '<body class="bg-gray-50 dark:bg-black h-screen overflow-hidden flex flex-col text-gray-900 dark:text-gray-100 font-sans antialiased" ng-app="fileManager"')
    
    content = content.replace('class="fm-header"', 'class="flex h-[60px] bg-white dark:bg-[#111111] border-b border-gray-200 dark:border-gray-800 items-center justify-between px-6 shrink-0 z-10"')
    content = content.replace('class="fm-toolbar"', 'class="flex h-12 bg-white dark:bg-[#111111] border-b border-gray-200 dark:border-gray-800 items-center px-6 gap-2 overflow-x-auto"')
    content = content.replace('class="fm-main"', 'class="flex flex-1 overflow-hidden"')
    content = content.replace('class="fm-sidebar"', 'class="w-[280px] bg-gray-50 dark:bg-[#0a0a0a] border-r border-gray-200 dark:border-gray-800 flex flex-col overflow-y-auto"')
    content = content.replace('class="fm-content"', 'class="flex-1 bg-white dark:bg-[#111111] flex flex-col overflow-hidden relative"')
    content = content.replace('class="fm-breadcrumb"', 'class="flex h-10 border-b border-gray-200 dark:border-gray-800 items-center px-6 bg-gray-50 dark:bg-[#0a0a0a] gap-3"')
    
    content = content.replace('class="fm-breadcrumb input"', 'class="flex-1 border-none bg-transparent font-mono text-[13px] text-gray-900 dark:text-gray-100 outline-none"')
    # Fix the actual input
    content = content.replace('id="currentPath" ng-model="currentPath" readonly', 'id="currentPath" ng-model="currentPath" readonly class="flex-1 border-none bg-transparent font-mono text-[13px] text-gray-900 dark:text-gray-100 outline-none w-full"')
    
    content = content.replace('class="fm-file-grid"', 'class="flex-1 overflow-y-auto p-0"')
    content = content.replace('class="fm-file-table"', 'class="w-full border-collapse text-left"')
    
    # Table headers
    content = re.sub(r'<thead id="tableHead">.*?</tr>.*?</thead>', 
                     r'<thead id="tableHead"><tr class="sticky top-0 bg-white dark:bg-[#111111] border-b border-gray-200 dark:border-gray-800 z-5"><th class="px-4 py-2 w-10"><input type="checkbox" id="selectAllCheckbox" onchange="toggleSelectAll(this)"></th><th class="px-4 py-2 text-[11px] font-semibold text-gray-500 uppercase tracking-wider">File Name</th><th class="px-4 py-2 text-[11px] font-semibold text-gray-500 uppercase tracking-wider">Size</th><th class="px-4 py-2 text-[11px] font-semibold text-gray-500 uppercase tracking-wider">Last Modified</th><th class="px-4 py-2 text-[11px] font-semibold text-gray-500 uppercase tracking-wider">Permissions</th></tr></thead>', 
                     content, flags=re.DOTALL)
    
    # The table body td classes are added dynamically by Angular/jQuery in filemanager.js. We can't change them easily here.
    # But we can inject a small <style> tag for them instead of inline classes since they are dynamically created.
    dynamic_styles = """
    <style>
        .fm-file-table td {
            padding: 10px 16px;
            border-bottom: 1px solid #e5e7eb;
            font-size: 13px;
            cursor: pointer;
            vertical-align: middle;
        }
        .dark .fm-file-table td {
            border-bottom-color: #1f2937;
        }
        .fm-file-table tr:hover td {
            background-color: #f9fafb;
        }
        .dark .fm-file-table tr:hover td {
            background-color: #1a1a1a;
        }
        .tree-node {
            padding: 8px 16px;
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
            font-size: 13px;
        }
        .tree-node:hover {
            background-color: #f9fafb;
        }
        .dark .tree-node:hover {
            background-color: #1a1a1a;
        }
    </style>
    """
    content = content.replace('</head>', f'{dynamic_styles}</head>')

    # Buttons in toolbar
    content = content.replace('class="cp-btn cp-btn-primary"', 'class="h-8 px-3 inline-flex items-center gap-1.5 text-xs font-medium rounded-lg bg-gray-900 text-white hover:bg-gray-800 dark:bg-white dark:text-gray-900 dark:hover:bg-gray-100 transition-colors"')
    content = content.replace('class="cp-btn cp-btn-ghost"', 'class="h-8 px-3 inline-flex items-center gap-1.5 text-xs font-medium rounded-lg text-gray-600 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-800 transition-colors"')
    content = content.replace('class="cp-btn cp-btn-danger cp-btn-ghost"', 'class="h-8 px-3 inline-flex items-center gap-1.5 text-xs font-medium rounded-lg text-red-600 hover:bg-red-50 dark:text-red-400 dark:hover:bg-red-900/20 transition-colors"')
    content = content.replace('class="cp-btn cp-btn-secondary"', 'class="h-8 px-3 inline-flex items-center gap-1.5 text-xs font-medium rounded-lg bg-gray-100 text-gray-700 hover:bg-gray-200 dark:bg-gray-800 dark:text-gray-300 dark:hover:bg-gray-700 transition-colors"')
    
    # Theme toggle logic update
    if 'document.documentElement.setAttribute(\'data-theme\', newTheme);' in content:
        content = content.replace('document.documentElement.setAttribute(\'data-theme\', newTheme);', """
        if (newTheme === 'dark') {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
        """)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def refactor_webmail_tailwind():
    path = r"c:\Users\HP\Videos\devasystem-test\cyberpanel-stable\webmail\templates\webmail\index.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We remove webmail.css
    content = re.sub(r'<link rel="stylesheet" href="{% static \'webmail/webmail\.css\' %}">', '', content)
    
    # Inject Tailwind CDN (if not inherited, but it extends baseTemplate which has it now! Wait, index.html of webmail extends baseTemplate/index.html.
    # So Tailwind CDN is already loaded!)
    
    # We replace `.wm-` classes with Tailwind classes
    content = content.replace('class="webmail-container"', 'class="h-[calc(100vh-120px)] flex flex-col bg-white dark:bg-[#111111] border border-gray-200 dark:border-gray-800 rounded-2xl overflow-hidden"')
    content = content.replace('class="wm-account-bar"', 'class="flex items-center justify-between p-3 px-6 bg-gray-50 dark:bg-[#0a0a0a] border-b border-gray-200 dark:border-gray-800"')
    content = content.replace('class="wm-account-current"', 'class="flex items-center gap-2 font-medium text-gray-900 dark:text-white"')
    content = content.replace('class="wm-account-select"', 'class="px-3 py-1.5 border border-gray-200 dark:border-gray-800 rounded-lg bg-white dark:bg-[#111111] text-gray-900 dark:text-white outline-none"')
    content = content.replace('class="wm-layout"', 'class="flex flex-1 overflow-hidden"')
    
    # Sidebar
    content = content.replace('class="wm-sidebar"', 'class="w-60 bg-gray-50 dark:bg-[#0a0a0a] border-r border-gray-200 dark:border-gray-800 flex flex-col py-6 shrink-0"')
    content = content.replace('class="btn btn-primary wm-compose-btn"', 'class="mx-6 mb-6 h-10 flex items-center justify-center gap-2 bg-gray-900 dark:bg-white text-white dark:text-gray-900 font-medium rounded-xl hover:opacity-90 transition-opacity"')
    content = content.replace('class="wm-folder-list"', 'class="flex-1 overflow-y-auto px-3"')
    content = re.sub(r'class="wm-folder-item([^"]*)"', r'class="\1 flex items-center p-2 mb-1 rounded-lg cursor-pointer text-gray-600 dark:text-gray-400 hover:bg-gray-200/50 dark:hover:bg-white/5 hover:text-gray-900 dark:hover:text-white transition-colors"', content)
    # the active class needs a style or angular directive. angular `ng-class="{'bg-gray-200/50 dark:bg-white/5 text-gray-900 dark:text-white font-medium': currentFolder === folder.name}"`
    # Let's just use a <style> block for active state since it's cleaner than modifying all ng-class logic.
    dynamic_styles = """
    <style>
        .wm-folder-item.active {
            background-color: rgba(0,0,0,0.05);
            color: #111827;
            font-weight: 500;
        }
        .dark .wm-folder-item.active {
            background-color: rgba(255,255,255,0.05);
            color: #ffffff;
        }
        .wm-nav-link.active {
            background-color: rgba(0,0,0,0.05);
            color: #111827;
        }
        .dark .wm-nav-link.active {
            background-color: rgba(255,255,255,0.05);
            color: #ffffff;
        }
        .wm-msg-row {
            padding: 16px;
            border-bottom: 1px solid #e5e7eb;
            cursor: pointer;
            position: relative;
        }
        .dark .wm-msg-row {
            border-bottom-color: #1f2937;
        }
        .wm-msg-row:hover { background-color: #f9fafb; }
        .dark .wm-msg-row:hover { background-color: #1a1a1a; }
        .wm-msg-row.unread { background-color: #f3f4f6; }
        .dark .wm-msg-row.unread { background-color: #111827; }
        .wm-msg-row.selected { background-color: #eef2ff; }
        .dark .wm-msg-row.selected { background-color: rgba(79, 70, 229, 0.1); }
    </style>
    """
    content = content.replace('{% block content %}', '{% block content %}\n' + dynamic_styles)
    
    content = content.replace('class="wm-folder-name"', 'class="flex-1 ml-3"')
    content = content.replace('class="wm-badge"', 'class="bg-indigo-600 text-white text-[10px] px-1.5 py-0.5 rounded-full font-bold"')
    content = content.replace('class="wm-sidebar-divider"', 'class="h-px bg-gray-200 dark:bg-gray-800 my-4 mx-6"')
    content = content.replace('class="wm-sidebar-nav"', 'class="px-3"')
    content = re.sub(r'class="wm-nav-link([^"]*)"', r'class="\1 flex items-center p-2 mb-1 rounded-lg cursor-pointer text-gray-600 dark:text-gray-400 hover:bg-gray-200/50 dark:hover:bg-white/5 hover:text-gray-900 dark:hover:text-white transition-colors"', content)
    
    # Message List
    content = content.replace('class="wm-message-list"', 'class="w-[340px] border-r border-gray-200 dark:border-gray-800 flex flex-col bg-white dark:bg-[#111111] shrink-0"')
    content = content.replace('class="wm-search-bar"', 'class="p-4 border-b border-gray-200 dark:border-gray-800 flex gap-2"')
    content = content.replace('class="wm-search-input"', 'class="flex-1 px-3 py-2 border border-gray-200 dark:border-gray-800 rounded-lg bg-gray-50 dark:bg-[#1a1a1a] text-gray-900 dark:text-white outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 text-sm"')
    content = content.replace('class="wm-search-btn"', 'class="w-9 h-9 rounded-lg bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white flex items-center justify-center transition-colors"')
    
    content = content.replace('class="wm-bulk-actions"', 'class="flex items-center px-4 py-2 border-b border-gray-200 dark:border-gray-800 bg-gray-50 dark:bg-[#0a0a0a] gap-2 shrink-0"')
    content = content.replace('class="wm-action-btn"', 'class="w-7 h-7 rounded bg-transparent text-gray-500 dark:text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-800 hover:text-gray-900 dark:hover:text-white flex items-center justify-center transition-colors"')
    content = content.replace('class="wm-page-info"', 'class="ml-auto text-[11px] text-gray-500"')
    
    content = content.replace('class="wm-messages"', 'class="flex-1 overflow-y-auto"')
    content = content.replace('class="wm-msg-from"', 'class="text-[13px] text-gray-900 dark:text-white font-medium mb-1 pr-14 truncate"')
    content = content.replace('class="wm-msg-subject"', 'class="text-xs text-gray-500 dark:text-gray-400 truncate"')
    content = content.replace('class="wm-msg-date"', 'class="absolute top-4 right-4 text-[11px] text-gray-400"')
    
    # Detail Pane
    content = content.replace('class="wm-detail-pane"', 'class="flex-1 flex flex-col bg-white dark:bg-[#111111] overflow-y-auto"')
    content = content.replace('class="wm-read-view"', 'class="flex flex-col h-full"')
    content = content.replace('class="wm-read-toolbar"', 'class="px-6 py-4 border-b border-gray-200 dark:border-gray-800 flex gap-2 shrink-0"')
    content = content.replace('class="wm-read-header"', 'class="p-6 border-b border-gray-200 dark:border-gray-800 shrink-0"')
    content = content.replace('class="wm-read-subject"', 'class="text-xl font-semibold text-gray-900 dark:text-white mb-4"')
    content = content.replace('class="wm-read-meta"', 'class="text-[13px] text-gray-600 dark:text-gray-400 space-y-1"')
    content = content.replace('class="wm-read-body"', 'class="p-6 flex-1 text-sm text-gray-800 dark:text-gray-200 leading-relaxed overflow-y-auto"')
    
    content = content.replace('class="wm-empty-detail"', 'class="flex flex-col items-center justify-center h-full text-gray-400"')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

refactor_filemanager_tailwind()
refactor_webmail_tailwind()
