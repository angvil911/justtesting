import os
import re

def refactor_index_tailwind():
    path = r"c:\Users\HP\Videos\devasystem-test\cyberpanel-stable\baseTemplate\templates\baseTemplate\index.html"
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
    
    # Remove custom CSS links
    content = re.sub(r'<link rel="stylesheet"[^>]*design-system\.css[^>]*>', '', content)
    content = re.sub(r'<link rel="stylesheet"[^>]*layout\.css[^>]*>', '', content)
    
    # Inject CDN before </head>
    if 'cdn.tailwindcss.com' not in content:
        content = content.replace('</head>', f'{cdn_script}</head>')

    # Fix body
    content = content.replace('<body class="cp-layout">', '<body class="flex h-screen bg-gray-50 dark:bg-[#0a0a0a] overflow-hidden transition-colors duration-200 antialiased font-sans text-gray-900 dark:text-gray-100">')
    
    # Sidebar
    content = content.replace('class="cp-sidebar"', 'class="w-[260px] h-full bg-white dark:bg-[#111111] border-r border-gray-200 dark:border-gray-800 flex flex-col shrink-0 transition-transform duration-300 z-20 overflow-y-auto"')
    content = content.replace('class="cp-sidebar-header"', 'class="h-[68px] flex items-center justify-center border-b border-gray-200 dark:border-gray-800 shrink-0 sticky top-0 bg-white dark:bg-[#111111] z-10"')
    content = content.replace('class="cp-sidebar-section-label"', 'class="text-[11px] font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider mt-6 mb-2 px-6"')
    
    # Replace sidebar items (we'll replace class="cp-sidebar-item" and add Tailwind classes)
    content = re.sub(r'class="cp-sidebar-item([^"]*)"', r'class="\1 flex items-center gap-3 px-4 py-2.5 mx-3 rounded-xl text-sm font-medium text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-white/5 hover:text-gray-900 dark:hover:text-white transition-colors cursor-pointer"', content)
    
    # Submenus
    content = re.sub(r'class="cp-sidebar-submenu([^"]*)"', r'class="\1 pl-11 pr-4 py-1 space-y-1 hidden"', content)
    
    # Submenu items (<li><a ...>)
    # Find all <a> inside .cp-sidebar-submenu and add tailwind classes. Easiest way is to replace `<ul class="... cp-sidebar-submenu ...">` children.
    # Actually, we can inject a global style in tailwind for sidebar-submenu a, or just replace `<li><a` inside the sidebar.
    # A quick fix:
    content = content.replace('<li><a ', '<li><a class="block py-1.5 text-[13px] text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors" ')
    
    # Wrapper
    content = content.replace('class="cp-main-wrapper"', 'class="flex-1 flex flex-col min-w-0 overflow-hidden"')
    
    # Topbar
    content = content.replace('class="cp-topbar"', 'class="h-[68px] bg-white/80 dark:bg-[#111111]/80 backdrop-blur-md border-b border-gray-200 dark:border-gray-800 flex items-center justify-between px-6 shrink-0 z-10"')
    content = content.replace('class="cp-topbar-right"', 'class="flex items-center gap-4"')
    content = content.replace('class="cp-mobile-toggle"', 'class="md:hidden text-gray-500 hover:text-gray-900 dark:hover:text-white"')
    
    # Main Content
    content = content.replace('class="cp-main-content"', 'class="flex-1 overflow-y-auto p-6 md:p-8"')

    # Theme toggle logic update in scripts
    # Find toggleTheme() function and replace to toggle class .dark on html
    # But wait, index.html might have old JS.
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
        
refactor_index_tailwind()

def refactor_home_tailwind():
    path = r"c:\Users\HP\Videos\devasystem-test\cyberpanel-stable\baseTemplate\templates\baseTemplate\homePage.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # The homePage uses cp-card, cp-stat-grid, cp-stat-card, etc.
    content = content.replace('class="cp-stat-grid"', 'class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8"')
    
    # Stat cards
    content = re.sub(r'class="cp-stat-card([^"]*)"', r'class="\1 bg-white dark:bg-[#111111] p-6 rounded-2xl border border-gray-200 dark:border-gray-800 shadow-sm flex items-center gap-4"', content)
    content = content.replace('class="cp-stat-icon"', 'class="w-12 h-12 rounded-xl flex items-center justify-center text-xl bg-indigo-50 dark:bg-indigo-900/20 text-indigo-600 dark:text-indigo-400"')
    content = content.replace('class="cp-stat-info"', 'class="flex-1"')
    content = content.replace('class="cp-stat-value"', 'class="text-2xl font-bold text-gray-900 dark:text-white"')
    content = content.replace('class="cp-stat-label"', 'class="text-sm font-medium text-gray-500 dark:text-gray-400"')
    
    # Generic cards
    content = re.sub(r'class="cp-card([^"]*)"', r'class="\1 bg-white dark:bg-[#111111] rounded-2xl border border-gray-200 dark:border-gray-800 shadow-sm overflow-hidden mb-8"', content)
    content = content.replace('class="cp-card-header"', 'class="px-6 py-5 border-b border-gray-200 dark:border-gray-800 flex items-center justify-between"')
    content = content.replace('class="cp-card-title"', 'class="text-base font-semibold text-gray-900 dark:text-white flex items-center gap-2"')
    content = content.replace('class="cp-card-body"', 'class="p-6"')
    
    # Resource bars
    content = content.replace('class="cp-resource-item"', 'class="mb-6 last:mb-0"')
    content = content.replace('class="cp-resource-header"', 'class="flex items-center justify-between mb-2"')
    content = content.replace('class="cp-resource-label"', 'class="text-sm font-medium text-gray-700 dark:text-gray-300 flex items-center gap-2"')
    content = content.replace('class="cp-resource-value"', 'class="text-sm font-semibold text-gray-900 dark:text-white"')
    content = content.replace('class="cp-progress-bg"', 'class="h-2 w-full bg-gray-100 dark:bg-gray-800 rounded-full overflow-hidden"')
    content = content.replace('class="cp-progress-bar"', 'class="h-full rounded-full transition-all duration-500"')
    
    # Tables
    content = content.replace('class="cp-table-responsive"', 'class="overflow-x-auto"')
    content = content.replace('class="cp-table"', 'class="w-full text-left text-sm text-gray-600 dark:text-gray-400"')
    content = content.replace('class="cp-table th"', 'class="px-6 py-4 font-semibold text-gray-900 dark:text-white border-b border-gray-200 dark:border-gray-800"')
    content = content.replace('class="cp-table td"', 'class="px-6 py-4 border-b border-gray-100 dark:border-gray-800/50"')
    
    # Make sure we didn't just replace "class='cp-table th'" literally. The HTML probably has `<th>` directly.
    content = content.replace('<thead>', '<thead class="bg-gray-50/50 dark:bg-white/5 border-b border-gray-200 dark:border-gray-800">')
    # Use regex to add classes to th and td
    content = re.sub(r'<th>', r'<th class="px-6 py-3 text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">', content)
    content = re.sub(r'<td([^>]*)>', r'<td\1 class="px-6 py-4 whitespace-nowrap text-sm text-gray-700 dark:text-gray-300">', content)
    content = re.sub(r'<tr([^>]*)>', r'<tr\1 class="border-b border-gray-100 dark:border-gray-800/50 hover:bg-gray-50 dark:hover:bg-white/5 transition-colors">', content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

refactor_home_tailwind()
