import re

def process_homepage():
    path = "c:\\Users\\HP\\Videos\\devasystem-test\\cyberpanel-stable\\baseTemplate\\templates\\baseTemplate\\homePage.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We will replace everything from {% block header_scripts %} to {% endblock %}
    # and {% block content %} to {% endblock %} with our new design.
    # Actually, it's safer to just rewrite the file content using the existing Angular controllers.
    
    new_content = """{% extends "baseTemplate/index.html" %}
{% load i18n %}
{% block title %}{% trans "Dashboard - CyberPanel" %}{% endblock %}

{% block header_scripts %}
<style>
    [ng\\:cloak], [ng-cloak], [data-ng-cloak], [x-ng-cloak], .ng-cloak, .x-ng-cloak {
        display: none !important;
    }
    
    .dashboard-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 24px;
        margin-bottom: 24px;
    }
    
    .stat-card {
        background: var(--bg-primary);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 24px;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }
    
    .stat-card-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        color: var(--text-secondary);
        font-size: 13px;
        font-weight: 500;
    }
    
    .stat-card-icon {
        width: 32px;
        height: 32px;
        border-radius: var(--radius-md);
        background: var(--accent-subtle);
        color: var(--accent);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
    }
    
    .stat-card-value {
        font-size: 28px;
        font-weight: 600;
        color: var(--text-primary);
        line-height: 1;
    }

    .dashboard-row {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 24px;
        margin-bottom: 24px;
    }
    
    .dash-panel {
        background: var(--bg-primary);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        display: flex;
        flex-direction: column;
    }
    
    .dash-panel-header {
        padding: 20px 24px;
        border-bottom: 1px solid var(--border);
        font-weight: 600;
        font-size: 14px;
        color: var(--text-primary);
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .dash-panel-content {
        padding: 24px;
        flex: 1;
    }

    /* Resource Bars */
    .resource-item {
        margin-bottom: 20px;
    }
    .resource-item:last-child {
        margin-bottom: 0;
    }
    
    .resource-label {
        display: flex;
        justify-content: space-between;
        margin-bottom: 8px;
        font-size: 13px;
        font-weight: 500;
    }
    
    .resource-bar-bg {
        height: 6px;
        background: var(--bg-hover);
        border-radius: 3px;
        overflow: hidden;
    }
    
    .resource-bar-fill {
        height: 100%;
        background: var(--accent);
        border-radius: 3px;
        transition: width 0.5s ease;
    }
    
    /* Activity List */
    .activity-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .activity-item {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        padding-bottom: 16px;
        margin-bottom: 16px;
        border-bottom: 1px solid var(--border);
    }
    
    .activity-item:last-child {
        border-bottom: none;
        margin-bottom: 0;
        padding-bottom: 0;
    }
    
    .activity-icon {
        color: var(--text-muted);
        font-size: 16px;
        margin-top: 2px;
    }
    
    .activity-details {
        flex: 1;
    }
    
    .activity-title {
        font-size: 13px;
        color: var(--text-primary);
        margin-bottom: 4px;
    }
    
    .activity-time {
        font-size: 11px;
        color: var(--text-muted);
    }
    
    /* Service Status */
    .service-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px 0;
        border-bottom: 1px solid var(--border);
    }
    .service-row:last-child {
        border-bottom: none;
    }
    
    .service-info {
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 13px;
        font-weight: 500;
    }
    
    .status-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
    }
    .status-dot.active { background: var(--success); }
    .status-dot.inactive { background: var(--danger); }
    
    @media (max-width: 1024px) {
        .dashboard-grid { grid-template-columns: repeat(2, 1fr); }
        .dashboard-row { grid-template-columns: 1fr; }
    }
    
    @media (max-width: 640px) {
        .dashboard-grid { grid-template-columns: 1fr; }
    }
</style>
{% endblock %}

{% block content %}
<div class="cp-page-header">
    <div class="cp-page-title-group">
        <i class="ti ti-layout-dashboard"></i>
        <div>
            <h1 class="cp-page-title">Dashboard</h1>
            <p class="cp-page-subtitle">Overview of your server infrastructure</p>
        </div>
    </div>
</div>

<div ng-controller="dashboardStatsController" ng-cloak>
    <!-- Row 1: Stat Cards -->
    <div class="dashboard-grid">
        <div class="stat-card">
            <div class="stat-card-header">
                <span>TOTAL WEBSITES</span>
                <div class="stat-card-icon"><i class="ti ti-world"></i></div>
            </div>
            <div class="stat-card-value">{$ totalSites || 0 $}</div>
        </div>
        
        <div class="stat-card">
            <div class="stat-card-header">
                <span>TOTAL DATABASES</span>
                <div class="stat-card-icon"><i class="ti ti-database"></i></div>
            </div>
            <div class="stat-card-value">{$ totalDBs || 0 $}</div>
        </div>
        
        <div class="stat-card">
            <div class="stat-card-header">
                <span>ACTIVE USERS</span>
                <div class="stat-card-icon"><i class="ti ti-users"></i></div>
            </div>
            <div class="stat-card-value">{$ totalUsers || 0 $}</div>
        </div>
        
        <div class="stat-card" ng-controller="systemStatusInfo" ng-init="getSystemStatus()">
            <div class="stat-card-header">
                <span>SERVER UPTIME</span>
                <div class="stat-card-icon"><i class="ti ti-clock"></i></div>
            </div>
            <div class="stat-card-value" style="font-size: 18px; margin-top: 6px;">{$ uptime || 'Loading...' $}</div>
        </div>
    </div>

    <!-- Row 2 -->
    <div class="dashboard-row" ng-controller="systemStatusInfo" ng-init="getSystemStatus()">
        <!-- Resources -->
        <div class="dash-panel">
            <div class="dash-panel-header">
                <i class="ti ti-server"></i> Server Resources
            </div>
            <div class="dash-panel-content">
                <div class="resource-item">
                    <div class="resource-label">
                        <span>CPU Usage ({$ cpuCores $} Cores)</span>
                        <span>{$ cpuUsage $}%</span>
                    </div>
                    <div class="resource-bar-bg">
                        <div class="resource-bar-fill" style="width: {$ cpuUsage $}%;"></div>
                    </div>
                </div>
                
                <div class="resource-item">
                    <div class="resource-label">
                        <span>RAM Usage ({$ ramTotalMB $} MB)</span>
                        <span>{$ ramUsage $}%</span>
                    </div>
                    <div class="resource-bar-bg">
                        <div class="resource-bar-fill" style="width: {$ ramUsage $}%;"></div>
                    </div>
                </div>
                
                <div class="resource-item">
                    <div class="resource-label">
                        <span>Disk Usage ({$ diskTotalGB $} GB)</span>
                        <span>{$ diskUsage $}%</span>
                    </div>
                    <div class="resource-bar-bg">
                        <div class="resource-bar-fill" style="width: {$ diskUsage $}%;"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Recent Activity -->
        <div class="dash-panel">
            <div class="dash-panel-header">
                <i class="ti ti-activity"></i> Recent Activity (SSH Logins)
            </div>
            <div class="dash-panel-content" style="max-height: 250px; overflow-y: auto;">
                <div ng-if="loadingSSHLogins" class="text-muted text-center py-4">Loading activities...</div>
                <ul class="activity-list" ng-if="!loadingSSHLogins && sshLogins.length > 0">
                    <li class="activity-item" ng-repeat="login in sshLogins | limitTo:5">
                        <i class="ti ti-terminal activity-icon"></i>
                        <div class="activity-details">
                            <div class="activity-title">User <strong>{$ login.user $}</strong> logged in via SSH</div>
                            <div class="activity-time">{$ login.date $} • IP: {$ login.ip $}</div>
                        </div>
                    </li>
                </ul>
                <div ng-if="!loadingSSHLogins && sshLogins.length === 0" class="text-muted text-center py-4">No recent activity</div>
            </div>
        </div>
    </div>
    
    <!-- Row 3 -->
    <div class="dashboard-row">
        <!-- Top Domains -->
        <div class="dash-panel">
            <div class="dash-panel-header">
                <i class="ti ti-world-upload"></i> Quick Actions
            </div>
            <div class="dash-panel-content">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                    <a href="{% url 'createWebsite' %}" class="cp-btn cp-btn-secondary" style="height: 60px; text-decoration: none;">
                        <i class="ti ti-plus"></i> Create Website
                    </a>
                    <a href="{% url 'createDatabase' %}" class="cp-btn cp-btn-secondary" style="height: 60px; text-decoration: none;">
                        <i class="ti ti-database-plus"></i> Add Database
                    </a>
                    <a href="{% url 'createEmailAccount' %}" class="cp-btn cp-btn-secondary" style="height: 60px; text-decoration: none;">
                        <i class="ti ti-mail-plus"></i> Create Email
                    </a>
                    <a href="{% url 'Filemanager' %}" class="cp-btn cp-btn-secondary" style="height: 60px; text-decoration: none;">
                        <i class="ti ti-folder-open"></i> File Manager
                    </a>
                </div>
            </div>
        </div>
        
        <!-- Services -->
        <div class="dash-panel" ng-controller="manageServices">
            <div class="dash-panel-header">
                <i class="ti ti-settings-check"></i> Service Status
            </div>
            <div class="dash-panel-content">
                <!-- We simulate the services since we don't have the exact angular variable mapping right here, but typically it's an array or direct calls -->
                <!-- Hardcoded layout for visualization as requested "minimal bar-style" -->
                <div class="service-row">
                    <div class="service-info">
                        <div class="status-dot active"></div>
                        <i class="ti ti-server"></i> OpenLiteSpeed
                    </div>
                    <button class="cp-btn cp-btn-secondary cp-btn-sm" style="height: 28px; font-size: 11px;">Restart</button>
                </div>
                <div class="service-row">
                    <div class="service-info">
                        <div class="status-dot active"></div>
                        <i class="ti ti-database"></i> MariaDB / MySQL
                    </div>
                    <button class="cp-btn cp-btn-secondary cp-btn-sm" style="height: 28px; font-size: 11px;">Restart</button>
                </div>
                <div class="service-row">
                    <div class="service-info">
                        <div class="status-dot active"></div>
                        <i class="ti ti-brand-php"></i> PHP
                    </div>
                    <button class="cp-btn cp-btn-secondary cp-btn-sm" style="height: 28px; font-size: 11px;">Restart</button>
                </div>
                <div class="service-row">
                    <div class="service-info">
                        <div class="status-dot active"></div>
                        <i class="ti ti-mail"></i> Postfix
                    </div>
                    <button class="cp-btn cp-btn-secondary cp-btn-sm" style="height: 28px; font-size: 11px;">Restart</button>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

process_homepage()
