import os

def refactor_admin_login():
    path = r'c:\Users\HP\Videos\devasystem-test\cyberpanel-stable\loginSystem\templates\loginSystem\login.html'
    
    new_html = """{% load static %}
<!DOCTYPE html>
<html lang="en" class="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Login - CyberPanel</title>
    
    <!-- Tabler Icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    
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
                    colors: {
                        primary: '#111827',
                        accent: '#4f46e5',
                    }
                }
            }
        }
    </script>
    
    <style>
        /* Custom spinner animation */
        @keyframes spinner-border {
            100% { transform: rotate(360deg); }
        }
        .spinner-border {
            display: inline-block;
            width: 1rem;
            height: 1rem;
            vertical-align: text-bottom;
            border: 0.2em solid currentColor;
            border-right-color: transparent;
            border-radius: 50%;
            animation: spinner-border .75s linear infinite;
        }
    </style>
</head>
<body class="bg-gray-50 dark:bg-[#0a0a0a] min-h-screen flex items-center justify-center transition-colors duration-200 antialiased font-sans" ng-app="loginSystem" ng-controller="loginSystem">

    <!-- Theme Toggle -->
    <button onclick="toggleTheme()" class="fixed top-6 right-6 w-10 h-10 rounded-xl bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 flex items-center justify-center text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white shadow-sm transition-all" title="Toggle dark mode">
        <i class="ti ti-moon text-lg" id="theme-icon"></i>
    </button>

    <!-- Login Card -->
    <div class="w-full max-w-[400px] bg-white dark:bg-[#111111] p-10 rounded-[20px] border border-gray-200 dark:border-gray-800 shadow-xl shadow-gray-200/50 dark:shadow-none mx-4">
        
        <div class="text-center mb-8">
            <img src="https://cyberpanel.net/wp-content/uploads/2025/04/cyberpanel-logo-icon_only.png" alt="CyberPanel Logo" class="h-12 mx-auto mb-4">
            <h1 class="text-xl font-semibold text-gray-900 dark:text-white mb-1">CyberPanel</h1>
            <p class="text-sm text-gray-500 dark:text-gray-400">Server Management Platform</p>
        </div>

        <form id="loginForm" autocomplete="off" class="space-y-4">
            
            <div class="relative">
                <i class="ti ti-user absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 text-lg pointer-events-none"></i>
                <input type="text" ng-model="username" name="username" placeholder="Username or Email" required
                       class="w-full h-11 pl-11 pr-4 bg-gray-50 dark:bg-[#1a1a1a] border border-gray-200 dark:border-gray-800 rounded-xl text-sm text-gray-900 dark:text-white focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-colors">
            </div>

            <div class="relative">
                <i class="ti ti-lock absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 text-lg pointer-events-none"></i>
                <input type="password" ng-model="password" id="password" name="password" placeholder="Password" ng-keypress="initiateLogin($event)" required autocomplete="current-password"
                       class="w-full h-11 pl-11 pr-11 bg-gray-50 dark:bg-[#1a1a1a] border border-gray-200 dark:border-gray-800 rounded-xl text-sm text-gray-900 dark:text-white focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-colors">
                <button type="button" onclick="togglePassword()" class="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 dark:hover:text-gray-200" title="Show password">
                    <i class="ti ti-eye text-lg" id="toggle-pwd-icon"></i>
                </button>
            </div>

            <div class="relative" ng-hide="verifyCode">
                <i class="ti ti-shield-lock absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 text-lg pointer-events-none"></i>
                <input type="text" ng-model="twofa" name="twofa" placeholder="Authenticator Code" required
                       class="w-full h-11 pl-11 pr-4 bg-gray-50 dark:bg-[#1a1a1a] border border-gray-200 dark:border-gray-800 rounded-xl text-sm text-gray-900 dark:text-white focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-colors">
            </div>

            <div class="relative">
                <i class="ti ti-language absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 text-lg pointer-events-none"></i>
                <select ng-model="languageSelection" ng-init="languageSelection='english'"
                        class="w-full h-11 pl-11 pr-4 bg-gray-50 dark:bg-[#1a1a1a] border border-gray-200 dark:border-gray-800 rounded-xl text-sm text-gray-900 dark:text-white appearance-none focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-colors">
                    <option value="english">English</option>
                    <option>Bangla</option>
                    <option>Bosnian</option>
                    <option>Bulgarian</option>
                    <option>Chinese</option>
                    <option>French</option>
                    <option>German</option>
                    <option>Greek</option>
                    <option>Italian</option>
                    <option>Indonesian</option>
                    <option>Japanese</option>
                    <option>Polish</option>
                    <option>Portuguese</option>
                    <option>Russian</option>
                    <option>Spanish</option>
                    <option>Turkish</option>
                    <option>Vietnamese</option>
                </select>
            </div>

            <div class="flex items-center justify-between py-2 text-sm">
                <label class="flex items-center gap-2 text-gray-500 dark:text-gray-400 cursor-pointer">
                    <input type="checkbox" class="rounded border-gray-300 dark:border-gray-700 text-indigo-600 focus:ring-indigo-500 bg-transparent">
                    <span>Remember me</span>
                </label>
                <a href="#" class="text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors">Forgot password?</a>
            </div>

            <button type="button" ng-click="verifyLoginCredentials()"
                    class="w-full h-11 bg-gray-900 dark:bg-white text-white dark:text-gray-900 font-medium rounded-xl text-sm flex items-center justify-center gap-2 hover:opacity-90 transition-opacity">
                Sign in
            </button>

            <div id="verifyingLogin" class="hidden text-center mt-4">
                <div class="spinner-border text-indigo-500" role="status"></div>
                <span class="sr-only">Verifying...</span>
            </div>
            
            <div id="loginFailed" class="hidden mt-4 p-3 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-900/50 rounded-xl flex items-center gap-2 text-sm text-red-600 dark:text-red-400" ng-style="{'display': errorMessage ? 'flex' : 'none'}">
                <i class="ti ti-alert-circle"></i>
                <span ng-bind="errorMessage"></span>
            </div>
        </form>
    </div>

    <!-- Scripts -->
    <script src="{% static 'baseTemplate/assets/js-core/jquery-core.min.js' %}"></script>
    <script src="https://code.angularjs.org/1.6.5/angular.min.js"></script>
    <script src="https://code.angularjs.org/1.6.5/angular-route.min.js"></script>
    <script src="{% static 'loginSystem/login-system.js' %}"></script>

    <script>
        function toggleTheme() {
            const html = document.documentElement;
            const currentTheme = html.classList.contains('dark') ? 'dark' : 'light';
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            if (newTheme === 'dark') {
                html.classList.add('dark');
            } else {
                html.classList.remove('dark');
            }
            
            localStorage.setItem('cyberPanelTheme', newTheme);
            document.getElementById('theme-icon').className = newTheme === 'dark' ? 'ti ti-sun text-lg' : 'ti ti-moon text-lg';
        }

        // Initialize theme
        const savedTheme = localStorage.getItem('cyberPanelTheme') || 
            (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
        
        if (savedTheme === 'dark') {
            document.documentElement.classList.add('dark');
            document.getElementById('theme-icon').className = 'ti ti-sun text-lg';
        } else {
            document.documentElement.classList.remove('dark');
            document.getElementById('theme-icon').className = 'ti ti-moon text-lg';
        }

        function togglePassword() {
            const pwdInput = document.getElementById('password');
            const icon = document.getElementById('toggle-pwd-icon');
            
            if (pwdInput.type === 'password') {
                pwdInput.type = 'text';
                icon.className = 'ti ti-eye-off text-lg';
            } else {
                pwdInput.type = 'password';
                icon.className = 'ti ti-eye text-lg';
            }
        }
    </script>
</body>
</html>
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)

refactor_admin_login()

def refactor_webmail_login():
    path = r'c:\Users\HP\Videos\devasystem-test\cyberpanel-stable\webmail\templates\webmail\login.html'
    
    new_html = """{% load i18n %}
{% load static %}
<!DOCTYPE html>
<html lang="en" class="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Webmail Login - CyberPanel</title>
    
    <!-- Tabler Icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    
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
    <style>
        @keyframes spinner-border {
            100% { transform: rotate(360deg); }
        }
        .spinner-border {
            display: inline-block;
            width: 1rem;
            height: 1rem;
            vertical-align: text-bottom;
            border: 0.2em solid currentColor;
            border-right-color: transparent;
            border-radius: 50%;
            animation: spinner-border .75s linear infinite;
        }
    </style>
</head>
<body class="bg-gray-50 dark:bg-[#0a0a0a] min-h-screen flex items-center justify-center transition-colors duration-200 antialiased font-sans" ng-app="webmail" ng-controller="webmailCtrl">

    <button onclick="toggleTheme()" class="fixed top-6 right-6 w-10 h-10 rounded-xl bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 flex items-center justify-center text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white shadow-sm transition-all" title="Toggle dark mode">
        <i class="ti ti-moon text-lg" id="theme-icon"></i>
    </button>

    <div class="w-full max-w-[400px] bg-white dark:bg-[#111111] p-10 rounded-[20px] border border-gray-200 dark:border-gray-800 shadow-xl shadow-gray-200/50 dark:shadow-none mx-4">
        
        <div class="text-center mb-8">
            <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/20 text-blue-500 dark:text-blue-400 rounded-2xl flex items-center justify-center mx-auto mb-4">
                <i class="ti ti-mail text-3xl"></i>
            </div>
            <h1 class="text-xl font-semibold text-gray-900 dark:text-white mb-1">Webmail Login</h1>
            <p class="text-sm text-gray-500 dark:text-gray-400">Access your email securely</p>
        </div>

        <form autocomplete="off" class="space-y-4">
            
            <div class="relative">
                <i class="ti ti-at absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 text-lg pointer-events-none"></i>
                <input type="email" ng-model="emailAddress" placeholder="Email Address" required
                       class="w-full h-11 pl-11 pr-4 bg-gray-50 dark:bg-[#1a1a1a] border border-gray-200 dark:border-gray-800 rounded-xl text-sm text-gray-900 dark:text-white focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-colors">
            </div>

            <div class="relative">
                <i class="ti ti-lock absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 text-lg pointer-events-none"></i>
                <input type="password" ng-model="password" id="password" placeholder="Password" ng-keypress="initiateLogin($event)" required
                       class="w-full h-11 pl-11 pr-11 bg-gray-50 dark:bg-[#1a1a1a] border border-gray-200 dark:border-gray-800 rounded-xl text-sm text-gray-900 dark:text-white focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-colors">
                <button type="button" onclick="togglePassword()" class="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 dark:hover:text-gray-200" title="Show password">
                    <i class="ti ti-eye text-lg" id="toggle-pwd-icon"></i>
                </button>
            </div>

            <button type="button" ng-click="verifyLoginCredentials()"
                    class="w-full h-11 bg-blue-600 text-white font-medium rounded-xl text-sm flex items-center justify-center gap-2 hover:bg-blue-700 transition-colors mt-2">
                Sign in to Webmail
            </button>

            <div id="verifyingLogin" class="hidden text-center mt-4">
                <div class="spinner-border text-blue-500" role="status"></div>
                <span class="sr-only">Verifying...</span>
            </div>
            
            <div id="loginFailed" class="hidden mt-4 p-3 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-900/50 rounded-xl flex items-center gap-2 text-sm text-red-600 dark:text-red-400" ng-style="{'display': errorMessage ? 'flex' : 'none'}">
                <i class="ti ti-alert-circle"></i>
                <span ng-bind="errorMessage"></span>
            </div>
        </form>
    </div>

    <script src="{% static 'baseTemplate/assets/js-core/jquery-core.min.js' %}"></script>
    <script src="https://code.angularjs.org/1.6.5/angular.min.js"></script>
    <script src="{% static 'webmail/webmail.js' %}"></script>

    <script>
        function toggleTheme() {
            const html = document.documentElement;
            const currentTheme = html.classList.contains('dark') ? 'dark' : 'light';
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            if (newTheme === 'dark') {
                html.classList.add('dark');
            } else {
                html.classList.remove('dark');
            }
            
            localStorage.setItem('cyberPanelTheme', newTheme);
            document.getElementById('theme-icon').className = newTheme === 'dark' ? 'ti ti-sun text-lg' : 'ti ti-moon text-lg';
        }

        const savedTheme = localStorage.getItem('cyberPanelTheme') || 
            (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
        
        if (savedTheme === 'dark') {
            document.documentElement.classList.add('dark');
            document.getElementById('theme-icon').className = 'ti ti-sun text-lg';
        } else {
            document.documentElement.classList.remove('dark');
            document.getElementById('theme-icon').className = 'ti ti-moon text-lg';
        }

        function togglePassword() {
            const pwdInput = document.getElementById('password');
            const icon = document.getElementById('toggle-pwd-icon');
            
            if (pwdInput.type === 'password') {
                pwdInput.type = 'text';
                icon.className = 'ti ti-eye-off text-lg';
            } else {
                pwdInput.type = 'password';
                icon.className = 'ti ti-eye text-lg';
            }
        }
    </script>
</body>
</html>
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)

refactor_webmail_login()
