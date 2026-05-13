"""
Internationalization (i18n) module for Flow2API
Supports English (en) and Simplified Chinese (zh-CN)
"""
from typing import Dict, Optional
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# Translation dictionary structure
TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "en": {
        # General
        "app_name": "Flow2API",
        "loading": "Loading...",
        "error": "Error",
        "success": "Success",
        "confirm": "Confirm",
        "cancel": "Cancel",
        "save": "Save",
        "delete": "Delete",
        "edit": "Edit",
        "add": "Add",
        "refresh": "Refresh",
        "export": "Export",
        "import": "Import",
        "close": "Close",
        "copy": "Copy",
        "test": "Test",

        # Login page
        "login_title": "Login - Flow2API",
        "admin_console": "Admin Console",
        "account": "Account",
        "password": "Password",
        "enter_account": "Please enter account",
        "enter_password": "Please enter password",
        "login_button": "Login",
        "logging_in": "Logging in...",
        "login_failed": "Login failed",
        "network_error": "Network error, please try again later",
        "copyright": "Flow2API © 2025",

        # Navigation
        "github_repo": "GitHub Repository",
        "logout": "Logout",

        # Token management
        "token_management": "Token Management",
        "total_tokens": "Total Tokens",
        "active_tokens": "Active Tokens",
        "today_images_total_images": "Today's Images / Total Images",
        "today_videos_total_videos": "Today's Videos / Total Videos",
        "today_errors_total_errors": "Today's Errors / Total Errors",
        "token_list": "Token List",
        "auto_refresh_at": "Auto Refresh AT",
        "auto_refresh_at_hint": "Automatically refresh AT using ST when token expires within 1 hour",
        "refresh_tokens": "Refresh",
        "export_all_tokens": "Export All Tokens",
        "import_tokens": "Import Tokens",
        "add_token": "Add New",

        # Token table headers
        "email": "Email",
        "status": "Status",
        "expire_time": "Expire Time",
        "balance": "Balance",
        "type": "Type",
        "project_id": "Project ID",
        "images": "Images",
        "videos": "Videos",
        "errors": "Errors",
        "actions": "Actions",

        # System config
        "system_config": "System Configuration",
        "security_config": "Security Configuration",
        "admin_username": "Admin Username",
        "old_password": "Old Password",
        "enter_old_password": "Enter old password",
        "new_password": "New Password",
        "enter_new_password": "Enter new password",
        "change_password": "Change Password",

        "api_key_config": "API Key Configuration",
        "current_api_key": "Current API Key",
        "current_api_key_readonly": "Current API Key (read-only)",
        "new_api_key": "New API Key",
        "enter_new_api_key": "Enter new API key",
        "api_key_for_client": "Key used by client to call API",
        "update_api_key": "Update API Key",

        "proxy_config": "Proxy Configuration",
        "enable_request_proxy": "Enable Request Proxy",
        "request_proxy_address": "Request Proxy Address",
        "proxy_placeholder": "http://127.0.0.1:7890 or socks5://127.0.0.1:1080",
        "supports_http_socks5": "Supports HTTP and SOCKS5 proxy",
        "media_upload_download_proxy": "Media Upload/Download Proxy",
        "media_proxy_hint": "When enabled, image upload and cached file download can use this proxy separately",
        "media_proxy_address": "Media Upload/Download Proxy Address",
        "test_proxy": "Test Proxy",
        "save_config": "Save Configuration",
        "test_target": "Test target:",

        "generation_config": "Generation Configuration",
        "image_timeout_seconds": "Image Generation Timeout (seconds)",
        "image_timeout_hint": "Image generation timeout, range: 60-3600 seconds (1min-1hr), auto-release token lock after timeout",
        "video_timeout_seconds": "Video Generation Timeout (seconds)",
        "video_timeout_hint": "Video generation timeout, range: 60-7200 seconds (1min-2hr), return upstream API timeout error after timeout",
        "max_retries": "Maximum Retries",
        "max_retries_hint": "Maximum retry count when generation, upload, polling requests fail, minimum value is 1",

        "token_polling_config": "Token Polling Configuration",
        "polling_mode": "Polling Mode",
        "random_polling": "Random Polling",
        "sequential_polling": "Sequential Polling",
        "polling_mode_hint": "Random polling uses default load priority strategy; sequential polling uses available tokens in stable order, all轮完后再开始下一轮。",

        "error_handling_config": "Error Handling Configuration",
        "error_ban_threshold": "Error Ban Threshold",
        "error_ban_hint": "Token will be automatically disabled after consecutive errors reach this count",

        "cache_config": "Cache Configuration",
        "enable_cache": "Enable Cache",
        "cache_hint": "When disabled, generated images and videos will output original links directly without caching to local",
        "cache_timeout_seconds": "Cache Timeout (seconds)",
        "cache_timeout_hint": "File cache timeout, range: 0-86400 seconds, 0 means never expire, cache files not automatically deleted",
        "cache_file_access_domain": "Cache File Access Domain",
        "cache_domain_hint": "Leave empty to use server address, e.g.: https://yourdomain.com",
        "current_effective_address": "Current Effective Address:",

        "plugin_connection_config": "Plugin Connection Configuration",
        "connection_interface": "Connection Interface",
        "connection_token": "Connection Token",
        "leave_empty_auto_generate": "Leave empty to auto-generate",
        "plugin_token_hint": "Used to verify Chrome extension plugin identity, leave empty to auto-generate random token",
        "auto_enable_on_update": "Auto-enable when updating token",
        "auto_enable_hint": "When plugin updates token, if the token is disabled, automatically enable it",
        "plugin_usage_hint": "Install Chrome extension, configure connection interface and token in plugin, plugin will automatically extract Google Labs cookie and update to system",
        "chrome_extension_config": "Chrome Extension Config",

        "captcha_config": "Captcha Configuration",
        "captcha_method": "Captcha Method",
        "select_captcha_method": "Select captcha method",

        # Captcha methods
        "yescaptcha": "YesCaptcha",
        "capmonster": "CapMonster",
        "ezcaptcha": "EzCaptcha",
        "capsolver": "CapSolver",
        "browser_captcha": "Browser Captcha (Headed)",
        "personal_captcha": "Browser Captcha (Built-in)",
        "remote_browser_captcha": "Remote Browser Captcha",

        # YesCaptcha
        "yescaptcha_api_key": "YesCaptcha API Key",
        "enter_yescaptcha_key": "Enter YesCaptcha API key",
        "yescaptcha_key_hint": "Used for automatic reCAPTCHA captcha acquisition, leave empty to not use captcha",
        "yescaptcha_api_address": "YesCaptcha API Address",
        "yescaptcha_type": "YesCaptcha Type",

        # Browser captcha
        "browser_captcha_hint": "Use Playwright automated browser to get captcha, no additional config needed, but consumes more system resources",
        "enable_proxy": "Enable Proxy",
        "browser_proxy_hint": "Configure independent proxy for headed browser",
        "proxy_address": "Proxy Address",
        "browser_count": "Browser Count",
        "browser_count_hint": "Number of browser instances to start simultaneously, each browser only opens 1 tab, requests are distributed by polling",

        # Personal browser captcha
        "personal_captcha_hint": "Use nodriver automated browser to get captcha, supports tab reuse, better performance",
        "browser_instance_count": "Browser Instance Count",
        "instance_count_hint": "Real browser instance count in personal mode. Effective slots approximately equal to instance count × per-instance tabs, up to 50.",
        "single_token_project_pool_size": "Single Token Project Pool Size",
        "pool_size_hint": "Only affects the number of project_ids this token can rotate, does not determine captcha tab count. Captcha tabs are shared globally.",
        "max_tabs_per_instance": "Max Tabs Per Instance",
        "max_tabs_hint": "Maximum resident captcha tabs per browser. Total concurrent slots approximately equal to instance count × this value, up to 50.",
        "reset_code_count": "Reset Code Count",
        "reset_code_hint": "Restart browser after successfully obtaining this many captchas. High concurrency recommends 0 or >=50, 5/10 causes frequent restarts leading to queuing.",
        "tab_idle_timeout_seconds": "Tab Idle Timeout (seconds)",
        "tab_idle_hint": "Auto-recycle idle tabs after this duration, default 600 seconds (10 minutes)",
        "personal_proxy_enabled": "Enable Proxy",
        "personal_proxy_hint": "Configure independent proxy for built-in browser (higher priority than global request proxy)",

        # Remote browser captcha
        "remote_browser_captcha_hint": "Get token via HTTP call to independent captcha service, callback finish/error after request ends",
        "remote_service_base_url": "Remote Service Base URL",
        "remote_service_api_key": "Remote Service API Key",
        "remote_request_timeout_seconds": "Remote Request Timeout (seconds)",

        "debug_config": "Debug Configuration",
        "enable_debug_mode": "Enable Debug Mode",
        "debug_mode_hint": "When enabled, detailed upstream API request and response logs will be written to logs.txt file",
        "debug_warning": "Warning: Debug mode generates very large amounts of logs, only enable during debugging, otherwise disk will boom",
        "switch_auto_saved": "Switch state auto-saved",

        # Request logs
        "request_logs": "Request Logs",
        "clear_logs": "Clear Logs",
        "operation": "Operation",
        "token_email": "Token Email",
        "status_col": "Status",
        "progress": "Progress",
        "time": "Time",
        "duration": "Duration",
        "message": "Message",

        # Test page
        "test_page": "Test Page",

        # API endpoints
        "api_login": "API Login",
        "api_stats": "API Statistics",

        # Status
        "active": "Active",
        "disabled": "Disabled",
        "banned": "Banned",
        "expired": "Expired",
        "unknown": "Unknown",

        # Messages
        "operation_success": "Operation successful",
        "operation_failed": "Operation failed",
        "token_not_found": "Token not found",
        "invalid_credentials": "Invalid credentials",
        "session_expired": "Session expired, please login again",
    },
    "zh-CN": {
        # General
        "app_name": "Flow2API",
        "loading": "加载中...",
        "error": "错误",
        "success": "成功",
        "confirm": "确认",
        "cancel": "取消",
        "save": "保存",
        "delete": "删除",
        "edit": "编辑",
        "add": "新增",
        "refresh": "刷新",
        "export": "导出",
        "import": "导入",
        "close": "关闭",
        "copy": "复制",
        "test": "测试",

        # Login page
        "login_title": "登录 - Flow2API",
        "admin_console": "管理员控制台",
        "account": "账户",
        "password": "密码",
        "enter_account": "请输入账户",
        "enter_password": "请输入密码",
        "login_button": "登录",
        "logging_in": "登录中...",
        "login_failed": "登录失败",
        "network_error": "网络错误,请稍后重试",
        "copyright": "Flow2API © 2025",

        # Navigation
        "github_repo": "GitHub 仓库",
        "logout": "退出",

        # Token management
        "token_management": "Token 管理",
        "total_tokens": "Token 总数",
        "active_tokens": "活跃 Token",
        "today_images_total_images": "今日图片/总图片",
        "today_videos_total_videos": "今日视频/总视频",
        "today_errors_total_errors": "今日错误/总错误",
        "token_list": "Token 列表",
        "auto_refresh_at": "自动刷新AT",
        "auto_refresh_at_hint": "Token距离过期<1h时自动使用ST刷新AT",
        "refresh_tokens": "刷新",
        "export_all_tokens": "导出所有Token",
        "import_tokens": "导入Token",
        "add_token": "新增",

        # Token table headers
        "email": "邮箱",
        "status": "状态",
        "expire_time": "过期时间",
        "balance": "余额",
        "type": "类型",
        "project_id": "项目ID",
        "images": "图片",
        "videos": "视频",
        "errors": "错误",
        "actions": "操作",

        # System config
        "system_config": "系统配置",
        "security_config": "安全配置",
        "admin_username": "管理员用户名",
        "old_password": "旧密码",
        "enter_old_password": "输入旧密码",
        "new_password": "新密码",
        "enter_new_password": "输入新密码",
        "change_password": "修改密码",

        "api_key_config": "API 密钥配置",
        "current_api_key": "当前 API Key",
        "current_api_key_readonly": "当前使用的 API Key（只读）",
        "new_api_key": "新 API Key",
        "enter_new_api_key": "输入新的 API Key",
        "api_key_for_client": "用于客户端调用 API 的密钥",
        "update_api_key": "更新 API Key",

        "proxy_config": "代理配置",
        "enable_request_proxy": "启用请求代理",
        "request_proxy_address": "请求代理地址",
        "proxy_placeholder": "http://127.0.0.1:7890 或 socks5://127.0.0.1:1080",
        "supports_http_socks5": "支持 HTTP 和 SOCKS5 代理",
        "media_upload_download_proxy": "媒体上传下载代理",
        "media_proxy_hint": "启用后，图片上传与图片/视频缓存下载可单独走该代理",
        "media_proxy_address": "媒体上传下载代理地址",
        "test_proxy": "测试代理",
        "save_config": "保存配置",
        "test_target": "测试目标：",

        "generation_config": "生成配置",
        "image_timeout_seconds": "图片生成超时时间（秒）",
        "image_timeout_hint": "图片生成超时时间，范围：60-3600 秒（1分钟-1小时），超时后自动释放Token锁",
        "video_timeout_seconds": "视频生成超时时间（秒）",
        "video_timeout_hint": "视频生成超时时间，范围：60-7200 秒（1分钟-2小时），超时后返回上游API超时错误",
        "max_retries": "最大重试次数",
        "max_retries_hint": "生成、上传、轮询等请求失败时的最大重试次数，最小值为 1",

        "token_polling_config": "Token 轮询配置",
        "polling_mode": "轮询模式",
        "random_polling": "随机轮询",
        "sequential_polling": "顺序轮询",
        "polling_mode_hint": "随机轮询使用默认负载优先策略；顺序轮询会按可用Token的稳定顺序依次使用，全部轮完后再开始下一轮。",

        "error_handling_config": "错误处理配置",
        "error_ban_threshold": "错误封禁阈值",
        "error_ban_hint": "Token 连续错误达到此次数后自动禁用",

        "cache_config": "缓存配置",
        "enable_cache": "启用缓存",
        "cache_hint": "关闭后，生成的图片和视频将直接输出原始链接，不会缓存到本地",
        "cache_timeout_seconds": "缓存超时时间（秒）",
        "cache_timeout_hint": "文件缓存超时时间，范围：0-86400 秒，其中 0 表示永不过期，不自动删除缓存文件",
        "cache_file_access_domain": "缓存文件访问域名",
        "cache_domain_hint": "留空则使用服务器地址，例如：https://yourdomain.com",
        "current_effective_address": "当前生效的访问地址：",

        "plugin_connection_config": "插件连接配置",
        "connection_interface": "连接接口",
        "connection_token": "连接Token",
        "leave_empty_auto_generate": "留空自动生成",
        "plugin_token_hint": "用于验证Chrome扩展插件的身份，留空将自动生成随机token",
        "auto_enable_on_update": "更新token时自动启用",
        "auto_enable_hint": "当插件更新token时，如果该token被禁用，则自动启用它",
        "plugin_usage_hint": "安装Chrome扩展后，将连接接口和Token配置到插件中，插件会自动提取Google Labs的cookie并更新到系统",
        "chrome_extension_config": "Chrome扩展配置",

        "captcha_config": "验证码配置",
        "captcha_method": "打码方式",
        "select_captcha_method": "选择验证码获取方式",

        # Captcha methods
        "yescaptcha": "YesCaptcha打码",
        "capmonster": "CapMonster打码",
        "ezcaptcha": "EzCaptcha打码",
        "capsolver": "CapSolver打码",
        "browser_captcha": "有头浏览器打码",
        "personal_captcha": "内置浏览器打码",
        "remote_browser_captcha": "远程有头打码",

        # YesCaptcha
        "yescaptcha_api_key": "YesCaptcha API密钥",
        "enter_yescaptcha_key": "请输入YesCaptcha API密钥",
        "yescaptcha_key_hint": "用于自动获取reCAPTCHA验证码，留空则不使用验证码",
        "yescaptcha_api_address": "YesCaptcha API地址",
        "yescaptcha_type": "YesCaptcha Type",

        # Browser captcha
        "browser_captcha_hint": "使用Playwright自动化浏览器获取验证码，无需额外配置，但会占用更多系统资源",
        "enable_proxy": "启用代理",
        "browser_proxy_hint": "为有头浏览器配置独立代理",
        "proxy_address": "代理地址",
        "browser_count": "浏览器数量",
        "browser_count_hint": "同时启动的浏览器实例数量，每个浏览器只开1个标签页，请求轮询分配",

        # Personal browser captcha
        "personal_captcha_hint": "使用nodriver自动化浏览器获取验证码，支持标签页复用，性能更优",
        "browser_instance_count": "浏览器实例数量",
        "instance_count_hint": "personal 模式真实浏览器实例数。有效槽位约等于 实例数 × 单实例标签页，上限 50。",
        "single_token_project_pool_size": "单 Token 项目池大小",
        "pool_size_hint": "只影响该 Token 可轮换的 project_id 数量，不决定打码标签页数。打码标签页由全局共享池统一复用。",
        "max_tabs_per_instance": "单实例最大标签页",
        "max_tabs_hint": "每个浏览器最多保留多少个共享打码标签页。总并发槽位约为 浏览器实例数 × 这里，上限 50。",
        "reset_code_count": "重置码数",
        "reset_code_hint": "成功获取多少个码后清理并重启浏览器。高并发建议 0 或 >=50，5/10 会频繁重启导致排队。",
        "tab_idle_timeout_seconds": "标签空闲超时(秒)",
        "tab_idle_hint": "标签页空闲多久后自动回收，默认600秒(10分钟)",
        "personal_proxy_enabled": "启用代理",
        "personal_proxy_hint": "为内置浏览器配置独立代理（优先级高于全局请求代理）",

        # Remote browser captcha
        "remote_browser_captcha_hint": "通过 HTTP 调用独立打码服务获取 token，并在请求结束后回调 finish/error",
        "remote_service_base_url": "远程服务 Base URL",
        "remote_service_api_key": "远程服务 API Key",
        "remote_request_timeout_seconds": "远程请求超时（秒）",

        "debug_config": "调试配置",
        "enable_debug_mode": "启用调试模式",
        "debug_mode_hint": "开启后，详细的上游API请求和响应日志将写入 logs.txt 文件",
        "debug_warning": "注意：调试模式会产生非常大量 的日志，仅限Debug时候开启，否则磁盘boom",
        "switch_auto_saved": "开关状态自动保存",

        # Request logs
        "request_logs": "请求日志",
        "clear_logs": "清空日志",
        "operation": "操作",
        "token_email": "Token邮箱",
        "status_col": "状态",
        "progress": "进度",
        "time": "时间",
        "duration": "耗时",
        "message": "消息",

        # Test page
        "test_page": "测试页面",

        # API endpoints
        "api_login": "API 登录",
        "api_stats": "API 统计",

        # Status
        "active": "活跃",
        "disabled": "已禁用",
        "banned": "已封禁",
        "expired": "已过期",
        "unknown": "未知",

        # Messages
        "operation_success": "操作成功",
        "operation_failed": "操作失败",
        "token_not_found": "Token不存在",
        "invalid_credentials": "用户名或密码错误",
        "session_expired": "会话已过期，请重新登录",
    }
}

# Default language
DEFAULT_LANGUAGE = "zh-CN"
SUPPORTED_LANGUAGES = list(TRANSLATIONS.keys())


def get_translation(lang: str, key: str) -> str:
    """
    Get translation for a given language and key.
    Falls back to DEFAULT_LANGUAGE if key not found.
    """
    if lang not in TRANSLATIONS:
        lang = DEFAULT_LANGUAGE
    return TRANSLATIONS.get(lang, TRANSLATIONS[DEFAULT_LANGUAGE]).get(
        key, TRANSLATIONS[DEFAULT_LANGUAGE].get(key, key)
    )


def get_all_translations(lang: str) -> Dict[str, str]:
    """Get all translations for a given language."""
    if lang not in TRANSLATIONS:
        lang = DEFAULT_LANGUAGE
    return TRANSLATIONS.get(lang, TRANSLATIONS[DEFAULT_LANGUAGE]).copy()


class I18nMiddleware(BaseHTTPMiddleware):
    """
    Middleware to handle language detection and setting.
    Language preference order:
    1. Query parameter 'lang'
    2. Cookie 'language'
    3. Accept-Language header
    4. Default language (zh-CN)
    """

    async def dispatch(self, request: Request, call_next):
        # Get language from query param, cookie, or header
        lang = (
            request.query_params.get("lang") or
            request.cookies.get("language") or
            request.headers.get("accept-language", "").split(",")[0].split("-")[0] or
            DEFAULT_LANGUAGE
        )

        # Normalize language code
        if lang == "en":
            lang = "en"
        elif lang.startswith("zh"):
            lang = "zh-CN"
        else:
            lang = DEFAULT_LANGUAGE

        # Store language in request state for access in endpoints
        request.state.lang = lang
        request.state.translations = get_all_translations(lang)

        response = await call_next(request)
        return response


def get_current_language(request: Request) -> str:
    """Get current language from request state."""
    return getattr(request.state, "lang", DEFAULT_LANGUAGE)


def set_language(response, lang: str, max_age: int = 365 * 24 * 60 * 60):
    """Set language cookie in response."""
    if lang not in SUPPORTED_LANGUAGES:
        lang = DEFAULT_LANGUAGE
    response.set_cookie(
        key="language",
        value=lang,
        max_age=max_age,
        httponly=True,
        samesite="lax"
    )
    return lang