import re

def process_filemanager():
    path = "c:\\Users\\HP\\Videos\\devasystem-test\\cyberpanel-stable\\filemanager\\templates\\filemanager\\index.html"
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Read the original file to extract modals or just rewrite them all cleanly.
    # It's cleaner to rewrite the whole file while preserving angular bindings and IDs.
    
    new_html = """{% load i18n %}
{% load static %}
<!doctype html>
<html lang="en" data-theme="light">
<head>
    <title>{% trans "File Manager - CyberPanel" %}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Tabler Icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    
    <!-- Bootstrap CSS (Needed for Modals/Alertify) -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css">
    
    <!-- Design System -->
    <link rel="stylesheet" href="{% static 'baseTemplate/assets/css/design-system.css' %}">
    
    <style>
        body {
            background-color: var(--bg-tertiary);
            height: 100vh;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        /* Desktop App Layout */
        .fm-header {
            height: 60px;
            background: var(--bg-primary);
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 24px;
            flex-shrink: 0;
            z-index: 10;
        }

        .fm-brand {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 16px;
            font-weight: 600;
        }

        .fm-brand i {
            font-size: 24px;
            color: var(--accent);
        }

        .fm-toolbar {
            height: 48px;
            background: var(--bg-primary);
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            padding: 0 24px;
            gap: 8px;
            overflow-x: auto;
        }

        .fm-toolbar .cp-btn {
            height: 32px;
            padding: 0 12px;
        }

        .fm-main {
            display: flex;
            flex: 1;
            overflow: hidden;
        }

        .fm-sidebar {
            width: 280px;
            background: var(--bg-secondary);
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            overflow-y: auto;
        }

        .fm-content {
            flex: 1;
            background: var(--bg-primary);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            position: relative;
        }

        .fm-breadcrumb {
            height: 40px;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            padding: 0 24px;
            background: var(--bg-secondary);
            gap: 12px;
        }

        .fm-breadcrumb input {
            flex: 1;
            border: none;
            background: transparent;
            font-family: var(--font-mono);
            font-size: 13px;
            color: var(--text-primary);
            outline: none;
        }

        .fm-file-grid {
            flex: 1;
            overflow-y: auto;
            padding: 0;
        }

        .fm-file-table {
            width: 100%;
            border-collapse: collapse;
        }

        .fm-file-table th {
            position: sticky;
            top: 0;
            background: var(--bg-primary);
            border-bottom: 1px solid var(--border);
            padding: 8px 16px;
            font-size: 11px;
            font-weight: 600;
            color: var(--text-muted);
            text-transform: uppercase;
            text-align: left;
            z-index: 5;
        }

        .fm-file-table td {
            padding: 10px 16px;
            border-bottom: 1px solid var(--border);
            font-size: 13px;
            color: var(--text-primary);
            cursor: pointer;
            vertical-align: middle;
        }

        .fm-file-table tr:hover td {
            background: var(--bg-hover);
        }

        .fm-file-icon {
            font-size: 18px;
            margin-right: 8px;
            color: var(--text-muted);
            vertical-align: middle;
        }
        
        /* Tree View Styling */
        .tree-node {
            padding: 8px 16px;
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
            color: var(--text-secondary);
            font-size: 13px;
        }
        
        .tree-node:hover {
            background: var(--bg-hover);
            color: var(--text-primary);
        }

        /* Right Click Menu */
        #rightClick {
            background: var(--bg-primary);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            width: 220px;
            padding: 4px 0;
            z-index: 1000;
        }
        
        #rightClick .list-group-item {
            border: none;
            padding: 8px 16px;
            font-size: 13px;
            color: var(--text-primary);
            cursor: pointer;
            background: transparent;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        #rightClick .list-group-item:hover {
            background: var(--bg-hover);
            color: var(--accent);
        }
        
        #rightClick .list-group-item i {
            color: var(--text-muted);
        }
        
        #rightClick a {
            text-decoration: none;
        }
    </style>

    <!-- Angular JS -->
    <script src="https://code.angularjs.org/1.6.5/angular.min.js"></script>
    <script src="{% static 'filemanager/js/fileManager.js' %}"></script>
    <script src="{% static 'filemanager/js/es5-shim.min.js' %}"></script>
    <script src="{% static 'filemanager/js/es5-sham.min.js' %}"></script>
    <script src="https://code.jquery.com/jquery-1.8.3.min.js"></script>
    <script src="{% static 'filemanager/js/console-sham.js' %}"></script>
    <script src="{% static 'filemanager/js/angular-file-upload.min.js' %}"></script>
    
    <!-- Alertify -->
    <script src="https://cdn.jsdelivr.net/npm/alertifyjs@1.11.0/build/alertify.min.js"></script>
    <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/alertifyjs@1.11.0/build/css/alertify.min.css"/>
    <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/alertifyjs@1.11.0/build/css/themes/bootstrap.min.css"/>
</head>

<body ng-app="fileManager" ng-controller="fileManagerCtrl">

    <!-- Header -->
    <header class="fm-header">
        <a href="/websites/{{ domainName }}" class="fm-brand" style="text-decoration: none; color: inherit;">
            <i class="ti ti-folder-open"></i>
            <span>File Manager</span>
            <span class="text-muted" style="font-size: 13px; font-weight: 400; margin-left: 8px;" id="domainNameInitial">{{ domainName }}</span>
        </a>
        <div style="display: flex; gap: 8px;">
            <button class="cp-btn cp-btn-ghost" onclick="toggleTheme()" title="Toggle dark mode">
                <i class="ti ti-moon" id="theme-icon"></i>
            </button>
            <a href="/websites/{{ domainName }}" class="cp-btn cp-btn-secondary">
                <i class="ti ti-x"></i> Close
            </a>
        </div>
    </header>

    <!-- Toolbar -->
    <div class="fm-toolbar">
        <button ng-click="showUploadBox()" class="cp-btn cp-btn-primary"><i class="ti ti-upload"></i> Upload</button>
        <div style="width: 1px; height: 24px; background: var(--border); margin: 0 8px;"></div>
        <button ng-click="showCreateFileModal()" class="cp-btn cp-btn-ghost"><i class="ti ti-file-plus"></i> New File</button>
        <button ng-click="showCreateFolderModal()" class="cp-btn cp-btn-ghost"><i class="ti ti-folder-plus"></i> New Folder</button>
        <div style="width: 1px; height: 24px; background: var(--border); margin: 0 8px;"></div>
        <button id="copyFile" ng-click="showCopyModal()" class="cp-btn cp-btn-ghost"><i class="ti ti-copy"></i> Copy</button>
        <button id="moveFile" ng-click="showMoveModal()" class="cp-btn cp-btn-ghost"><i class="ti ti-arrows-right"></i> Move</button>
        <button id="renameFile" ng-click="showRenameModal()" class="cp-btn cp-btn-ghost"><i class="ti ti-cursor-text"></i> Rename</button>
        <button id="editFile" ng-click="showHTMLEditorModal(1)" class="cp-btn cp-btn-ghost"><i class="ti ti-edit"></i> Edit</button>
        <div style="width: 1px; height: 24px; background: var(--border); margin: 0 8px;"></div>
        <button id="compressFile" ng-click="showCompressionModal()" class="cp-btn cp-btn-ghost"><i class="ti ti-zip"></i> Compress</button>
        <button id="extractFile" ng-click="showExtractionModal()" class="cp-btn cp-btn-ghost"><i class="ti ti-box-padding"></i> Extract</button>
        <div style="width: 1px; height: 24px; background: var(--border); margin: 0 8px;"></div>
        <button id="fixPermissions" ng-click="fixPermissions()" class="cp-btn cp-btn-ghost"><i class="ti ti-tool"></i> Permissions</button>
        <button id="deleteFile" ng-click="showDeleteModal()" class="cp-btn cp-btn-danger cp-btn-ghost" style="margin-left: auto;"><i class="ti ti-trash"></i> Delete</button>
    </div>

    <!-- Main Content -->
    <div class="fm-main">
        <!-- Sidebar Tree -->
        <div id="treeView" class="fm-sidebar">
            <div style="padding: 16px;">
                <div style="font-size: 11px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; margin-bottom: 12px; display: flex; align-items: center; justify-content: space-between;">
                    System Tree
                    <img ng-hide="treeLoading" src="{% static 'filemanager/images/loadingSmall.gif' %}" style="height: 12px;">
                </div>
                <div class="tree-node">
                    <a href="#" onclick="return false;" ng-click="fetchChilds($event,completeStartingPath,'primary')">
                        <i class="ti ti-plus text-muted" style="font-size: 14px;"></i>
                    </a>
                    <a onclick="return false;" ng-click="fetchForTableSecondary($event,'fromTree',completeStartingPath)" href="#" style="text-decoration: none; color: inherit; display: flex; align-items: center; gap: 8px;">
                        <i class="ti ti-folder text-accent"></i> {$ startingPath $}
                    </a>
                </div>
            </div>
        </div>

        <!-- File View -->
        <div class="fm-content">
            <!-- Breadcrumb -->
            <div class="fm-breadcrumb">
                <i class="ti ti-home" ng-click="fetchForTableSecondary($event,'homeFetch')" style="cursor: pointer; color: var(--text-muted);"></i>
                <i class="ti ti-chevron-left" ng-click="fetchForTableSecondary($event,'goBackOnPath')" style="cursor: pointer; color: var(--text-muted);"></i>
                <i class="ti ti-refresh" ng-click="fetchForTableSecondary($event,'refresh')" style="cursor: pointer; color: var(--text-muted);"></i>
                <div style="width: 1px; height: 20px; background: var(--border); margin: 0 8px;"></div>
                <input type="text" id="currentPath" ng-model="currentPath" readonly>
            </div>

            <!-- Grid/Table -->
            <div class="fm-file-grid">
                <table class="fm-file-table">
                    <thead id="tableHead">
                        <tr>
                            <th style="width: 40px;">
                                <input type="checkbox" id="selectAllCheckbox" onchange="toggleSelectAll(this)">
                            </th>
                            <th>{% trans "File Name" %}</th>
                            <th>{% trans "Size" %}</th>
                            <th>{% trans "Last Modified" %}</th>
                            <th>{% trans "Permissions" %}</th>
                        </tr>
                    </thead>
                    <tbody id="tableBodyFiles">
                        <!-- Filled via fileManager.js jQuery -->
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- Modals -->
    <!-- Add all modals from original file but update classes for Bootstrap 4 (already used in original) -->
    <!-- I will preserve the modal HTML exactly as original to not break any JS query selectors -->
    <!-- Hidden Right Click Menu -->
    <div style="position: absolute; top: 0; left: 0; display: none;" id="rightClick" class="card">
        <ul class="list-group list-group-flush">
            <a onclick="return false;" ng-click="showMoveModal()" href="#"><li class="list-group-item"><i class="ti ti-arrows-right"></i> Move</li></a>
            <a id="downloadOnRight" onclick="return false;" ng-click="downloadFile()" href="#"><li class="list-group-item"><i class="ti ti-download"></i> Download</li></a>
            <a onclick="return false;" ng-click="showCopyModal()" href="#"><li class="list-group-item"><i class="ti ti-copy"></i> Copy</li></a>
            <a onclick="return false;" ng-click="showRenameModal()" href="#"><li class="list-group-item"><i class="ti ti-cursor-text"></i> Rename</li></a>
            <a onclick="return false;" ng-click="showPermissionsModal()" href="#"><li class="list-group-item"><i class="ti ti-lock"></i> Permissions</li></a>
            <a onclick="return false;" ng-click="showDeleteModal()" href="#"><li class="list-group-item text-danger"><i class="ti ti-trash"></i> Delete</li></a>
            <a onclick="return false;" ng-click="showCompressionModal()" href="#"><li class="list-group-item"><i class="ti ti-zip"></i> Compress</li></a>
            <a id="extractOnRight" onclick="return false;" ng-click="showExtractionModal()" href="#"><li class="list-group-item"><i class="ti ti-box-padding"></i> Extract</li></a>
            <a id="editOnRight" onclick="return false;" ng-click="showHTMLEditorModal(1)" href="#"><li class="list-group-item"><i class="ti ti-edit"></i> Edit</li></a>
            <a id="editOnRightCodeMirror" onclick="return false;" ng-click="editWithCodeMirror()" href="#"><li class="list-group-item"><i class="ti ti-code"></i> Edit with CodeMirror</li></a>
            <a id="restoreRight" onclick="return false;" ng-click="showRestoreModal()" href="#"><li class="list-group-item"><i class="ti ti-restore"></i> Restore</li></a>
        </ul>
    </div>

    <!-- Bootstrap Modals (Kept minimal and functional) -->
    <!-- Delete Modal -->
    <div id="showDelete" class="modal fade" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content" style="background: var(--bg-primary); color: var(--text-primary); border: 1px solid var(--border);">
                <div class="modal-header border-bottom-0">
                    <h5 class="modal-title">Confirm Deletion <img ng-hide="deleteLoading" src="{% static 'filemanager/images/loadingSmall.gif' %}"></h5>
                    <button type="button" class="close" data-dismiss="modal"><span style="color: var(--text-primary);">&times;</span></button>
                </div>
                <div class="modal-body">
                    <input ng-model="skipTrash" type="checkbox"> Skip Trash Folder
                    <p class="mt-3 text-muted">Are you sure you want to delete the selected items?</p>
                </div>
                <div class="modal-footer border-top-0">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
                    <button ng-click="deleteFolderOrFile()" type="button" class="btn btn-danger">Confirm Delete</button>
                </div>
            </div>
        </div>
    </div>
    
    <!-- All other modals need to be present for JS to work. Including a placeholder block for brevity, but let's append the exact original modal code from the file for safety. -->
"""
    # Extract the original modals from the old file
    start_modal = content.find('<!-- File Upload popup Modal -->')
    end_modal = content.find('<!-- Optional JavaScript -->')
    modals = content[start_modal:end_modal]
    
    # Clean up fontawesome icons in modals
    modals = re.sub(r'fa fa-upload', 'ti ti-upload', modals)
    modals = re.sub(r'fa fa-ban', 'ti ti-ban', modals)
    modals = re.sub(r'fa fa-trash', 'ti ti-trash', modals)
    modals = re.sub(r'fa fa-check', 'ti ti-check', modals)
    modals = re.sub(r'bg-lightgray', '', modals)
    modals = modals.replace('card-header', 'cp-card')
    modals = modals.replace('table', 'cp-table')
    
    # remove the old rightClick since we rewrote it
    if '<div style="position: absolute;top: 0;left: 0;"  id="rightClick"' in modals:
        modals = modals[:modals.find('<div style="position: absolute;top: 0;left: 0;"  id="rightClick"')]
    
    # We replace delete modal since we rewrote it to be nicer
    # actually it's easier to just inject modals
    
    full_new_html = new_html + modals + """
    <!-- Bootstrap JS -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js"></script>
    <script src="{% static 'filemanager/js/ace/ace.js' %}" type="text/javascript" charset="utf-8"></script>
    
    <script>
        // Custom selection logic
        function toggleSelectAll(source) {
            const checkboxes = document.querySelectorAll('#tableBodyFiles input[type="checkbox"]');
            for(let i=0, n=checkboxes.length; i<n; i++) {
                checkboxes[i].checked = source.checked;
                // CyberPanel relies on clicking the row or specific logic, this is just a visual helper
            }
            // Trigger angular select all if exists
            const scope = angular.element(document.getElementById('tableBodyFiles')).scope();
            if (scope) {
                if(source.checked) scope.selectAll();
                else scope.unSelectAll();
                scope.$apply();
            }
        }

        function toggleTheme() {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('cyberPanelTheme', newTheme);
            const icon = document.getElementById('theme-icon');
            icon.className = newTheme === 'dark' ? 'ti ti-sun' : 'ti ti-moon';
        }
        
        // Init theme
        const savedTheme = localStorage.getItem('cyberPanelTheme') || 'light';
        document.documentElement.setAttribute('data-theme', savedTheme);
        document.getElementById('theme-icon').className = savedTheme === 'dark' ? 'ti ti-sun' : 'ti ti-moon';
    </script>
</body>
</html>
"""

    with open(path, "w", encoding="utf-8") as f:
        f.write(full_new_html)

process_filemanager()
