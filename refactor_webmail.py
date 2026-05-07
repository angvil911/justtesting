import re
import os

def process_webmail_html():
    path = "c:\\Users\\HP\\Videos\\devasystem-test\\cyberpanel-stable\\webmail\\templates\\webmail\\index.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    icon_map = {
        'fa-envelope': 'ti-mail',
        'fa-pen-to-square': 'ti-pencil-plus',
        'fa-address-book': 'ti-address-book',
        'fa-filter': 'ti-filter',
        'fa-gear': 'ti-settings',
        'fa-folder-plus': 'ti-folder-plus',
        'fa-search': 'ti-search',
        'fa-trash': 'ti-trash',
        'fa-envelope-open': 'ti-mail-opened',
        'fa-folder-open': 'ti-folder-open',
        'fa-chevron-left': 'ti-chevron-left',
        'fa-chevron-right': 'ti-chevron-right',
        'fa-star': 'ti-star',
        'fa-inbox': 'ti-inbox',
        'fa-spinner': 'ti-loader',
        'fa-spin': 'ti-spin',
        'fa-reply': 'ti-arrow-back-up',
        'fa-reply-all': 'ti-arrow-back-up-double',
        'fa-share': 'ti-share',
        'fa-paperclip': 'ti-paperclip',
        'fa-bold': 'ti-bold',
        'fa-italic': 'ti-italic',
        'fa-underline': 'ti-underline',
        'fa-list-ul': 'ti-list',
        'fa-list-ol': 'ti-list-numbers',
        'fa-link': 'ti-link',
        'fa-times': 'ti-x',
        'fa-xmark': 'ti-x',
        'fa-paper-plane': 'ti-send',
        'fa-floppy-disk': 'ti-device-floppy',
        'fa-plus': 'ti-plus',
        'fa-pencil': 'ti-pencil'
    }

    content = re.sub(r'fa\s+fa-([a-zA-Z0-9-]+)', lambda m: f"ti ti-{m.group(1)}", content)
    
    for old, new in icon_map.items():
        content = content.replace(f'ti-{old[3:]}', new)
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def process_webmail_css():
    path = "c:\\Users\\HP\\Videos\\devasystem-test\\cyberpanel-stable\\webmail\\static\\webmail\\webmail.css"
    if not os.path.exists(path):
        return
        
    new_css = """
/* CyberPanel Webmail Redesign */

.webmail-container {
    height: calc(100vh - 120px);
    display: flex;
    flex-direction: column;
    background: var(--bg-primary);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    overflow: hidden;
}

.wm-account-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 24px;
    background: var(--bg-secondary);
    border-bottom: 1px solid var(--border);
}

.wm-account-current {
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: 500;
    color: var(--text-primary);
}

.wm-account-select {
    padding: 6px 12px;
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    background: var(--bg-primary);
    color: var(--text-primary);
    outline: none;
}

.wm-layout {
    display: flex;
    flex: 1;
    overflow: hidden;
}

/* Sidebar */
.wm-sidebar {
    width: 240px;
    background: var(--bg-secondary);
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    padding: 24px 0;
}

.wm-compose-btn {
    margin: 0 24px 24px;
    background: var(--text-primary);
    color: var(--bg-primary);
    border: none;
    border-radius: var(--radius-md);
    padding: 10px;
    font-weight: 500;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    cursor: pointer;
}

.wm-compose-btn i {
    font-size: 16px;
}

.wm-folder-list {
    flex: 1;
    overflow-y: auto;
    padding: 0 12px;
}

.wm-folder-item {
    display: flex;
    align-items: center;
    padding: 8px 12px;
    margin-bottom: 4px;
    border-radius: var(--radius-md);
    cursor: pointer;
    color: var(--text-secondary);
    transition: all var(--transition);
}

.wm-folder-item:hover {
    background: var(--bg-hover);
    color: var(--text-primary);
}

.wm-folder-item.active {
    background: var(--bg-hover);
    color: var(--text-primary);
    font-weight: 500;
}

.wm-folder-item i {
    font-size: 16px;
    margin-right: 12px;
}

.wm-folder-name {
    flex: 1;
}

.wm-badge {
    background: var(--accent);
    color: white;
    font-size: 11px;
    padding: 2px 6px;
    border-radius: 10px;
    font-weight: 600;
}

.wm-sidebar-divider {
    height: 1px;
    background: var(--border);
    margin: 16px 24px;
}

.wm-sidebar-nav {
    padding: 0 12px;
}

.wm-nav-link {
    display: flex;
    align-items: center;
    padding: 8px 12px;
    color: var(--text-secondary);
    text-decoration: none;
    cursor: pointer;
    border-radius: var(--radius-md);
    margin-bottom: 4px;
}

.wm-nav-link:hover, .wm-nav-link.active {
    background: var(--bg-hover);
    color: var(--text-primary);
}

.wm-nav-link i {
    font-size: 16px;
    margin-right: 12px;
}

/* Message List */
.wm-message-list {
    width: 340px;
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    background: var(--bg-primary);
}

.wm-search-bar {
    padding: 16px;
    border-bottom: 1px solid var(--border);
    display: flex;
    gap: 8px;
}

.wm-search-input {
    flex: 1;
    padding: 8px 12px;
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    background: var(--bg-tertiary);
    color: var(--text-primary);
    outline: none;
}

.wm-search-btn {
    width: 36px;
    height: 36px;
    border-radius: var(--radius-md);
    background: var(--bg-hover);
    border: none;
    color: var(--text-primary);
    cursor: pointer;
}

.wm-bulk-actions {
    display: flex;
    align-items: center;
    padding: 8px 16px;
    border-bottom: 1px solid var(--border);
    background: var(--bg-secondary);
    gap: 8px;
}

.wm-action-btn {
    width: 28px;
    height: 28px;
    border-radius: var(--radius-sm);
    background: transparent;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
}

.wm-action-btn:hover {
    background: var(--bg-hover);
    color: var(--text-primary);
}

.wm-page-info {
    margin-left: auto;
    font-size: 11px;
    color: var(--text-muted);
}

.wm-messages {
    flex: 1;
    overflow-y: auto;
}

.wm-msg-row {
    padding: 16px;
    border-bottom: 1px solid var(--border);
    cursor: pointer;
    position: relative;
    transition: background var(--transition);
}

.wm-msg-row:hover {
    background: var(--bg-hover);
}

.wm-msg-row.unread {
    background: var(--bg-tertiary);
}

.wm-msg-row.unread .wm-msg-from {
    font-weight: 600;
}

.wm-msg-row.selected {
    background: var(--accent-subtle);
}

.wm-msg-from {
    font-size: 13px;
    color: var(--text-primary);
    margin-bottom: 4px;
    padding-right: 60px;
}

.wm-msg-subject {
    font-size: 12px;
    color: var(--text-secondary);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.wm-msg-date {
    position: absolute;
    top: 16px;
    right: 16px;
    font-size: 11px;
    color: var(--text-muted);
}

/* Detail Pane */
.wm-detail-pane {
    flex: 1;
    display: flex;
    flex-direction: column;
    background: var(--bg-primary);
    overflow-y: auto;
}

.wm-read-view {
    display: flex;
    flex-direction: column;
    height: 100%;
}

.wm-read-toolbar {
    padding: 16px 24px;
    border-bottom: 1px solid var(--border);
    display: flex;
    gap: 8px;
}

.wm-read-header {
    padding: 24px;
    border-bottom: 1px solid var(--border);
}

.wm-read-subject {
    font-size: 20px;
    font-weight: 600;
    margin: 0 0 16px 0;
    color: var(--text-primary);
}

.wm-read-meta {
    font-size: 13px;
    color: var(--text-secondary);
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.wm-read-body {
    padding: 24px;
    flex: 1;
    font-size: 14px;
    line-height: 1.6;
    color: var(--text-primary);
}

/* Empty */
.wm-empty-detail, .wm-empty {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: var(--text-muted);
}

.wm-empty-detail i {
    font-size: 48px;
    margin-bottom: 16px;
    opacity: 0.5;
}

/* Form inputs mapping */
.form-control {
    width: 100%;
    padding: 8px 12px;
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    background: var(--bg-primary);
    color: var(--text-primary);
}

.btn {
    padding: 8px 16px;
    border-radius: var(--radius-md);
    cursor: pointer;
    font-weight: 500;
    border: none;
}

.btn-default {
    background: var(--bg-hover);
    color: var(--text-primary);
}

.btn-primary {
    background: var(--text-primary);
    color: var(--bg-primary);
}

.btn-danger {
    background: var(--danger);
    color: white;
}
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_css)

process_webmail_html()
process_webmail_css()
