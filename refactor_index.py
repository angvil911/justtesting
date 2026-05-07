import re

def process_index_html():
    path = "c:\\Users\\HP\\Videos\\devasystem-test\\cyberpanel-stable\\baseTemplate\\templates\\baseTemplate\\index.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace FontAwesome with Tabler Icons CDN
    content = content.replace(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">',
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">\n    <link rel="stylesheet" href="{% static \'baseTemplate/assets/css/design-system.css\' %}?v={{ CP_VERSION }}">\n    <link rel="stylesheet" href="{% static \'baseTemplate/assets/css/layout.css\' %}?v={{ CP_VERSION }}">'
    )

    # Remove inline style blocks related to theme (we'll remove everything between <!-- Modern Design System --> and </style> inclusive)
    start_str = '<!-- Modern Design System -->'
    end_str = '</style>'
    if start_str in content:
        start_idx = content.find(start_str)
        end_idx = content.find(end_str, start_idx) + len(end_str)
        content = content[:start_idx] + content[end_idx:]

    # Add dark mode detection script to head if not present
    dark_mode_script = """
    <script>
        (function() {
            const savedTheme = localStorage.getItem('cyberPanelTheme');
            const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            const theme = savedTheme || (prefersDark ? 'dark' : 'light');
            document.documentElement.setAttribute('data-theme', theme);
        })();
    </script>
    """
    if 'data-theme' not in content[:1000]:
        content = content.replace('</head>', f'{dark_mode_script}</head>')

    # Update IDs and classes to match new layout.css
    # header -> cp-topbar
    content = content.replace('id="header"', 'id="header" class="cp-topbar"')
    content = content.replace('id="header-right"', 'id="header-right" class="cp-topbar-right"')
    content = content.replace('id="sidebar"', 'id="sidebar" class="cp-sidebar"')
    content = content.replace('id="main-content"', 'id="main-content" class="cp-main-content"')
    
    # Update layout shell wrapping
    content = content.replace('<body>', '<body class="cp-layout">')
    # Move topbar inside a main wrapper, but wait, topbar and main-content are currently siblings of sidebar
    # Let's adjust classes instead of changing DOM tree too much, layout.css might need adjustment if DOM is different.
    # Actually, layout.css expects .cp-layout > .cp-sidebar and .cp-layout > .cp-main-wrapper > .cp-topbar + .cp-main-content
    # Let's write a regex to do this.

    # 2. Icon Replacements
    icon_map = {
        'fa-bars': 'ti-menu-2',
        'fa-facebook-f': 'ti-brand-facebook',
        'fa-youtube': 'ti-brand-youtube',
        'fa-twitter': 'ti-brand-x',
        'fa-moon': 'ti-moon',
        'fa-sun': 'ti-sun',
        'fa-arrow-right-from-bracket': 'ti-logout',
        'fa-desktop': 'ti-device-desktop',
        'fa-th-large': 'ti-layout-dashboard',
        'fa-code-branch': 'ti-git-branch',
        'fa-palette': 'ti-palette',
        'fa-link': 'ti-link',
        'fa-comments': 'ti-messages',
        'fa-users': 'ti-users',
        'fa-chevron-right': 'ti-chevron-right',
        'fa-wordpress': 'ti-brand-wordpress',
        'fa-ship': 'ti-ship',
        'fa-globe': 'ti-world',
        'fa-cube': 'ti-box',
        'fa-database': 'ti-database',
        'fa-sitemap': 'ti-sitemap',
        'fa-envelope': 'ti-mail',
        'fa-folder': 'ti-folder',
        'fa-save': 'ti-device-floppy',
        'fa-lock': 'ti-lock',
        'fa-folder-open': 'ti-folder-open',
        'fa-fire': 'ti-flame',
        'fa-cogs': 'ti-settings',
        'fa-adjust': 'ti-adjustments',
        'fa-cog': 'ti-settings',
        'fa-code': 'ti-code',
        'fa-file': 'ti-file',
        'fa-shield': 'ti-shield',
        'fa-plug': 'ti-plug',
        'fa-times': 'ti-x',
        'fa-shield-alt': 'ti-shield-check',
        'fa-brain': 'ti-brain',
        'fa-rocket': 'ti-rocket',
        'fa-magic': 'ti-wand',
        'fa-check-circle': 'ti-circle-check',
        'fa-book-open': 'ti-book'
    }

    content = re.sub(r'fas\s+(fa-[a-zA-Z0-9-]+)', lambda m: f"ti ti-{m.group(1)[3:]}", content)
    content = re.sub(r'fab\s+(fa-[a-zA-Z0-9-]+)', lambda m: f"ti ti-{m.group(1)[3:]}", content)
    
    for old, new in icon_map.items():
        content = content.replace(f'ti-{old[3:]}', new)

    # Class mappings
    content = content.replace('class="sidebar-logo"', 'class="cp-sidebar-header"')
    content = content.replace('class="section-header"', 'class="cp-sidebar-section-label"')
    content = content.replace('class="menu-item"', 'class="cp-sidebar-item"')
    content = content.replace('class="menu-item ', 'class="cp-sidebar-item ')
    content = content.replace('class="submenu"', 'class="cp-sidebar-submenu"')
    content = content.replace('class="icon-wrapper"', 'class="icon"')
    content = content.replace('id="mobile-menu-toggle"', 'id="mobile-menu-toggle" class="cp-mobile-toggle"')
    content = content.replace('class="logout-btn"', 'class="cp-sidebar-logout"')
    
    # We also need to add a wrapper around header and main-content for .cp-main-wrapper
    content = content.replace('<!-- Header -->', '<div class="cp-main-wrapper">\n    <!-- Header -->')
    # Find the end of main-content and close the wrapper
    # Actually, we can just close it before <!-- Additional Scripts -->
    content = content.replace('<!-- Additional Scripts -->', '</div>\n    <!-- Additional Scripts -->')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

process_index_html()
