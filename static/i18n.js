/**
 * Flow2API Frontend Internationalization (i18n) Module
 * Supports English (en) and Simplified Chinese (zh-CN)
 */

// Current language state
let currentLang = 'en';
let translations = {};

// Default English translations (fallback)
const DEFAULT_TRANSLATIONS = {
    // General
    'app_name': 'Flow2API',
    'loading': 'Loading...',
    'error': 'Error',
    'success': 'Success',
    'confirm': 'Confirm',
    'cancel': 'Cancel',
    'save': 'Save',
    'delete': 'Delete',
    'edit': 'Edit',
    'add': 'Add',
    'refresh': 'Refresh',
    'export': 'Export',
    'import': 'Import',
    'close': 'Close',
    'copy': 'Copy',
    'test': 'Test',

    // Login page
    'login_title': 'Login - Flow2API',
    'admin_console': 'Admin Console',
    'account': 'Account',
    'password': 'Password',
    'enter_account': 'Please enter account',
    'enter_password': 'Please enter password',
    'login_button': 'Login',
    'logging_in': 'Logging in...',
    'login_failed': 'Login failed',
    'network_error': 'Network error, please try again later',
    'copyright': 'Flow2API © 2025',

    // Navigation
    'github_repo': 'GitHub Repository',
    'logout': 'Logout',

    // Token management
    'token_management': 'Token Management',
    'total_tokens': 'Total Tokens',
    'active_tokens': 'Active Tokens',
    'today_images_total_images': "Today's Images / Total Images",
    'today_videos_total_videos': "Today's Videos / Total Videos",
    'today_errors_total_errors': "Today's Errors / Total Errors",
    'token_list': 'Token List',
    'auto_refresh_at': 'Auto Refresh AT',
    'auto_refresh_at_hint': 'Automatically refresh AT using ST when token expires within 1 hour',
    'refresh_tokens': 'Refresh',
    'export_all_tokens': 'Export All Tokens',
    'import_tokens': 'Import Tokens',
    'add_token': 'Add New',

    // Token table headers
    'email': 'Email',
    'status': 'Status',
    'expire_time': 'Expire Time',
    'balance': 'Balance',
    'type': 'Type',
    'project_id': 'Project ID',
    'images': 'Images',
    'videos': 'Videos',
    'errors': 'Errors',
    'actions': 'Actions',

    // System config
    'system_config': 'System Configuration',
    'security_config': 'Security Configuration',
    'admin_username': 'Admin Username',
    'old_password': 'Old Password',
    'enter_old_password': 'Enter old password',
    'new_password': 'New Password',
    'enter_new_password': 'Enter new password',
    'change_password': 'Change Password',

    'api_key_config': 'API Key Configuration',
    'current_api_key': 'Current API Key',
    'current_api_key_readonly': 'Current API Key (read-only)',
    'new_api_key': 'New API Key',
    'enter_new_api_key': 'Enter new API key',
    'api_key_for_client': 'Key used by client to call API',
    'update_api_key': 'Update API Key',

    'proxy_config': 'Proxy Configuration',
    'enable_request_proxy': 'Enable Request Proxy',
    'request_proxy_address': 'Request Proxy Address',
    'proxy_placeholder': 'http://127.0.0.1:7890 or socks5://127.0.0.1:1080',
    'supports_http_socks5': 'Supports HTTP and SOCKS5 proxy',
    'media_upload_download_proxy': 'Media Upload/Download Proxy',
    'media_proxy_hint': 'When enabled, image upload and cached file download can use this proxy separately',
    'media_proxy_address': 'Media Upload/Download Proxy Address',
    'test_proxy': 'Test Proxy',
    'save_config': 'Save Configuration',
    'test_target': 'Test target:',

    'generation_config': 'Generation Configuration',
    'image_timeout_seconds': 'Image Generation Timeout (seconds)',
    'image_timeout_hint': 'Image generation timeout, range: 60-3600 seconds (1min-1hr), auto-release token lock after timeout',
    'video_timeout_seconds': 'Video Generation Timeout (seconds)',
    'video_timeout_hint': 'Video generation timeout, range: 60-7200 seconds (1min-2hr), return upstream API timeout error after timeout',
    'max_retries': 'Maximum Retries',
    'max_retries_hint': 'Maximum retry count when generation, upload, polling requests fail, minimum value is 1',

    'token_polling_config': 'Token Polling Configuration',
    'polling_mode': 'Polling Mode',
    'random_polling': 'Random Polling',
    'sequential_polling': 'Sequential Polling',
    'polling_mode_hint': 'Random polling uses default load priority strategy; sequential polling uses available tokens in stable order.',

    'error_handling_config': 'Error Handling Configuration',
    'error_ban_threshold': 'Error Ban Threshold',
    'error_ban_hint': 'Token will be automatically disabled after consecutive errors reach this count',

    'cache_config': 'Cache Configuration',
    'enable_cache': 'Enable Cache',
    'cache_hint': 'When disabled, generated images and videos will output original links directly without caching to local',
    'cache_timeout_seconds': 'Cache Timeout (seconds)',
    'cache_timeout_hint': 'File cache timeout, range: 0-86400 seconds, 0 means never expire, cache files not automatically deleted',
    'cache_file_access_domain': 'Cache File Access Domain',
    'cache_domain_hint': 'Leave empty to use server address, e.g.: https://yourdomain.com',
    'current_effective_address': 'Current Effective Address:',

    'plugin_connection_config': 'Plugin Connection Configuration',
    'connection_interface': 'Connection Interface',
    'connection_token': 'Connection Token',
    'leave_empty_auto_generate': 'Leave empty to auto-generate',
    'plugin_token_hint': 'Used to verify Chrome extension plugin identity, leave empty to auto-generate random token',
    'auto_enable_on_update': 'Auto-enable when updating token',
    'auto_enable_hint': 'When plugin updates token, if the token is disabled, automatically enable it',
    'plugin_usage_hint': 'Install Chrome extension, configure connection interface and token in plugin, plugin will automatically extract Google Labs cookie and update to system',

    'captcha_config': 'Captcha Configuration',
    'captcha_method': 'Captcha Method',
    'select_captcha_method': 'Select captcha method',

    'browser_captcha': 'Browser Captcha (Headed)',
    'personal_captcha': 'Browser Captcha (Built-in)',
    'remote_browser_captcha': 'Remote Browser Captcha',

    'debug_config': 'Debug Configuration',
    'enable_debug_mode': 'Enable Debug Mode',
    'debug_mode_hint': 'When enabled, detailed upstream API request and response logs will be written to logs.txt file',
    'debug_warning': 'Warning: Debug mode generates very large amounts of logs, only enable during debugging',
    'switch_auto_saved': 'Switch state auto-saved',

    // Request logs
    'request_logs': 'Request Logs',
    'clear_logs': 'Clear Logs',

    // Status
    'active': 'Active',
    'disabled': 'Disabled',
    'banned': 'Banned',
    'expired': 'Expired',
    'unknown': 'Unknown',

    // Messages
    'operation_success': 'Operation successful',
    'operation_failed': 'Operation failed',
    'token_not_found': 'Token not found',
    'invalid_credentials': 'Invalid credentials',
    'session_expired': 'Session expired, please login again',

    // Additional
    'browser': 'Browser',
    'project_pool_size': 'Project Pool Size',
    'max_resident_tabs': 'Max Resident Tabs',
    'fresh_restart_every': 'Fresh Restart Every',
    'idle_tab_ttl': 'Idle Tab TTL (seconds)',
    'captcha_service': 'Captcha Service',
    'built_in_browser': 'Built-in Browser',
    'remote_browser': 'Remote Browser',
    'captcha_mode': 'Captcha Mode',
};

/**
 * Initialize i18n system
 * Load translations from server and apply to page
 */
async function initI18n() {
    // Get saved language from cookie or localStorage
    const savedLang = getCookie('language') || localStorage.getItem('language') || 'en';
    await setLanguage(savedLang);
}

/**
 * Set current language and load translations
 * @param {string} lang - Language code (en, zh-CN)
 */
async function setLanguage(lang) {
    try {
        // Fetch translations from server
        const response = await fetch(`/api/i18n?lang=${lang}`);
        if (response.ok) {
            const data = await response.json();
            translations = data.translations;
            currentLang = data.lang;
        } else {
            // Fallback to default translations
            translations = DEFAULT_TRANSLATIONS;
            currentLang = 'en';
        }
    } catch (error) {
        console.error('Failed to load translations:', error);
        translations = DEFAULT_TRANSLATIONS;
        currentLang = 'en';
    }

    // Save language preference
    document.cookie = `language=${currentLang};path=/;max-age=${365*24*60*60}`;
    localStorage.setItem('language', currentLang);

    // Apply translations to page
    applyTranslations();

    // Update language selector if exists
    updateLanguageSelector();

    return currentLang;
}

/**
 * Get translation for a key
 * @param {string} key - Translation key
 * @returns {string} Translated text or key itself
 */
function t(key) {
    return translations[key] || DEFAULT_TRANSLATIONS[key] || key;
}

/**
 * Apply translations to all elements with data-i18n attribute
 */
function applyTranslations() {
    // Update elements with data-i18n attribute
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (element.tagName === 'INPUT' && element.placeholder !== undefined) {
            element.placeholder = t(key);
        } else {
            element.textContent = t(key);
        }
    });

    // Update elements with data-i18n-html attribute (for HTML content)
    document.querySelectorAll('[data-i18n-html]').forEach(element => {
        const key = element.getAttribute('data-i18n-html');
        element.innerHTML = t(key);
    });

    // Update elements with data-i18n-title attribute
    document.querySelectorAll('[data-i18n-title]').forEach(element => {
        const key = element.getAttribute('data-i18n-title');
        element.title = t(key);
    });

    // Update document title
    const titleKey = document.documentElement.getAttribute('data-i18n-title');
    if (titleKey) {
        document.title = t(titleKey);
    }
}

/**
 * Get cookie value by name
 * @param {string} name - Cookie name
 * @returns {string|null} Cookie value or null
 */
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

/**
 * Update language selector UI elements
 */
function updateLanguageSelector() {
    // Update any language toggle/selector elements
    document.querySelectorAll('.lang-toggle').forEach(btn => {
        const btnLang = btn.getAttribute('data-lang');
        if (btnLang === currentLang) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
}

/**
 * Create language switcher dropdown
 * @returns {string} HTML string for language switcher
 */
function createLanguageSwitcher() {
    const languages = [
        { code: 'en', name: 'English', flag: '🇺🇸' },
        { code: 'zh-CN', name: '简体中文', flag: '🇨🇳' }
    ];

    const currentLangName = currentLang === 'zh-CN' ? '简体中文' : 'English';
    const currentFlag = currentLang === 'zh-CN' ? '🇨🇳' : '🇺🇸';

    return `
        <div class="relative inline-block">
            <button id="langSwitcher" class="inline-flex items-center gap-1 text-xs transition-colors hover:bg-accent hover:text-accent-foreground h-7 px-2.5">
                <span>${currentFlag}</span>
                <span>${currentLangName}</span>
                <svg class="h-3 w-3" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="6 9 12 15 18 9"/>
                </svg>
            </button>
            <div id="langDropdown" class="hidden absolute right-0 mt-1 w-32 rounded-md border border-border bg-background shadow-lg z-50">
                ${languages.map(lang => `
                    <button onclick="setLanguage('${lang.code}')"
                            class="w-full text-left px-3 py-2 text-xs hover:bg-accent flex items-center gap-2 ${lang.code === currentLang ? 'bg-accent' : ''}">
                        <span>${lang.flag}</span>
                        <span>${lang.name}</span>
                    </button>
                `).join('')}
            </div>
        </div>
    `;
}

// Toggle language dropdown
document.addEventListener('click', function(e) {
    const switcher = document.getElementById('langSwitcher');
    const dropdown = document.getElementById('langDropdown');
    if (switcher && e.target.closest('#langSwitcher')) {
        dropdown.classList.toggle('hidden');
    } else if (dropdown && !e.target.closest('#langSwitcher')) {
        dropdown.classList.add('hidden');
    }
});

// Export functions for use in other scripts
window.i18n = {
    setLanguage,
    t,
    applyTranslations,
    initI18n,
    getCurrentLang: () => currentLang,
    createLanguageSwitcher
};