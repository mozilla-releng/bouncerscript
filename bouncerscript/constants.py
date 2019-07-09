ALIASES_REGEXES = {
    'thunderbird-beta-latest': r'^Thunderbird-\d+\.0b\d+$',
    'thunderbird-beta-latest-ssl': r'^Thunderbird-\d+\.0b\d+-SSL$',
    'thunderbird-beta-msi-latest-ssl': r'^Thunderbird-\d+\.0b\d+-msi-SSL$',
    'thunderbird-latest': r'^Thunderbird-\d+\.\d+(\.\d+)?$',
    'thunderbird-latest-ssl': r'^Thunderbird-\d+\.\d+(\.\d+)?-SSL$',
    'thunderbird-msi-latest-ssl': r'^Thunderbird-\d+\.\d+(\.\d+)?-msi-SSL$',
    # TODO Use mozilla-version
    'fennec-beta-latest': r'^Fennec-\d+\.\d+b\d+$',
    'fennec-latest': r'^Fennec-\d+\.\d+(\.\d+)?$',
    'firefox-devedition-stub': r'^Devedition-\d+\.0b\d+-stub$',
    'firefox-devedition-latest': r'^Devedition-\d+\.0b\d+$',
    'firefox-devedition-latest-ssl': r'^Devedition-\d+\.0b\d+-SSL$',
    'firefox-devedition-msi-latest-ssl': r'^Devedition-\d+\.0b\d+-msi-SSL$',
    'firefox-beta-stub': r'^Firefox-\d+\.0b\d+-stub$',
    'firefox-beta-latest': r'^Firefox-\d+\.0b\d+$',
    'firefox-beta-latest-ssl': r'^Firefox-\d+\.0b\d+-SSL$',
    'firefox-beta-msi-latest-ssl': r'^Firefox-\d+\.0b\d+-msi-SSL$',
    'firefox-stub': r'^Firefox-\d+\.\d+(\.\d+)?-stub$',
    'firefox-latest': r'^Firefox-\d+\.\d+(\.\d+)?$',
    'firefox-latest-ssl': r'^Firefox-\d+\.\d+(\.\d+)?-SSL$',
    'firefox-msi-latest-ssl': r'^Firefox-\d+\.\d+(\.\d+)?-msi-SSL$',
    'firefox-esr-latest': r'^Firefox-\d+\.\d+(\.\d+)?esr$',
    'firefox-esr-latest-ssl': r'^Firefox-\d+\.\d+(\.\d+)?esr-SSL$',
    'firefox-esr-msi-latest-ssl': r'^Firefox-\d+\.\d+(\.\d+)?esr-msi-SSL$',
    'firefox-esr-next-latest': r'^Firefox-\d+\.\d+(\.\d+)?esr$',
    'firefox-esr-next-latest-ssl': r'^Firefox-\d+\.\d+(\.\d+)?esr-SSL$',
    'firefox-esr-next-msi-latest-ssl': r'^Firefox-\d+\.\d+(\.\d+)?esr-msi-SSL$',
    'firefox-sha1': r'^Firefox-\d+\.\d+(\.\d+)?esr-sha1$',
    'firefox-sha1-ssl': r'^Firefox-\d+\.\d+(\.\d+)?esr-sha1$',
}

PARTNER_ALIASES_REGEX = {
    r'^partner-firefox-beta-(.*)-latest$': r'^Firefox-\d+\.0b\d+-(.*)$',
    r'^partner-firefox-beta-(.*)-stub$': r'^Firefox-\d+\.0b\d+-(.*)-stub$',
    r'^partner-firefox-release-(.*)-latest$': r'^Firefox-\d+\.\d+(?:\.\d+)?-(.*)$',
    r'^partner-firefox-release-(.*)-stub$': r'^Firefox-\d+\.\d+(?:\.\d+)?-(.*)-stub$',
    r'^partner-firefox-esr-(.*)-latest$': r'^Firefox-\d+\.\d+(?:\.\d+)?esr-(.*)$',
    r'^partner-firefox-esr-(.*)-stub$': r'^Firefox-\d+\.\d+(?:\.\d+)?esr-(.*)-stub$',
}

PRODUCT_TO_DESTINATIONS_REGEXES = {
    'fennec': r'^(/mobile/releases/.*?/(?:android-api-16|android-x86)/\:lang/fennec-.*\:lang\.(?:android-arm|android-i386)\.apk)$',
    'firefox-rc': r'^(/firefox/candidates/.*?/build[0-9]+/(update/)?(?:linux-i686|linux-x86_64|mac|win32|win64(?:|-aarch64))/\:lang/(?:firefox|Firefox).*\.(?:bz2|dmg|exe|mar))$',
    'firefox': r'^(/firefox/releases/.*?/(update/)?(?:linux-i686|linux-x86_64|mac|win32|win64(?:|-aarch64))/\:lang/(?:firefox|Firefox).*\.(?:bz2|dmg|exe|mar|msi))$',
    'devedition': r'^(/devedition/releases/.*?/(update/)?(?:linux-i686|linux-x86_64|mac|win32|win64(?:|-aarch64))/\:lang/(?:firefox|Firefox).*\.(?:bz2|dmg|exe|mar|msi))$',
    'thunderbird': (r'^(/thunderbird/releases/.*?/(update/)?(?:linux-i686|linux-x86_64|mac|win32|win64(?:|-aarch64))/\:lang/'
                    r'(?:thunderbird|Thunderbird).*\.(?:bz2|dmg|exe|mar|msi))$'),
}

_BOUNCER_PATH_REGEXES_PER_PRODUCT_DEFAULT = {
    'firefox-nightly-latest': (r'^(/firefox/nightly/latest-mozilla-central-l10n/firefox-\d+\.0a1\.:lang\.'
                               r'(?:linux-i686\.tar\.bz2|linux-x86_64\.tar\.bz2|mac\.dmg|win32\.installer\.exe|win64\.installer\.exe|win64-aarch64\.installer\.exe))$'),
    'firefox-nightly-latest-ssl': (r'^(/firefox/nightly/latest-mozilla-central/firefox-\d+\.0a1\.en-US\.'
                                   r'(?:linux-i686\.tar\.bz2|linux-x86_64\.tar\.bz2|mac\.dmg|win32\.installer\.exe|win64\.installer\.exe|win64-aarch64\.installer\.exe))$'),
    'firefox-nightly-latest-l10n': (r'^(/firefox/nightly/latest-mozilla-central-l10n/firefox-\d+\.0a1\.:lang\.'
                                    r'(?:linux-i686\.tar\.bz2|linux-x86_64\.tar\.bz2|mac\.dmg|win32\.installer\.exe|win64\.installer\.exe|win64-aarch64\.installer\.exe))$'),
    'firefox-nightly-latest-l10n-ssl': (r'^(/firefox/nightly/latest-mozilla-central-l10n/firefox-\d+\.0a1\.:lang\.'
                                        r'(?:linux-i686\.tar\.bz2|linux-x86_64\.tar\.bz2|mac\.dmg|win32\.installer\.exe|win64\.installer\.exe|win64-aarch64\.installer\.exe))$'),
}

_BOUNCER_PATH_REGEXES_PER_PRODUCT_MSI = {
    **_BOUNCER_PATH_REGEXES_PER_PRODUCT_DEFAULT,
    'firefox-nightly-msi-latest-ssl': (r'^(/firefox/nightly/latest-mozilla-central/firefox-\d+\.0a1\.en-US\.'
                                       r'(?:win32\.installer\.msi|win64(?:|-aarch64)\.installer\.msi))$'),
    'firefox-nightly-msi-latest-l10n-ssl': (r'^(/firefox/nightly/latest-mozilla-central-l10n/firefox-\d+\.0a1\.:lang\.'
                                            r'(?:win32\.installer\.msi|win64(?:|-aarch64)\.installer\.msi))$'),
}

BOUNCER_PATH_REGEXES_PER_PRODUCT = [_BOUNCER_PATH_REGEXES_PER_PRODUCT_DEFAULT, _BOUNCER_PATH_REGEXES_PER_PRODUCT_MSI]

# XXX A list of tuple is used because we care about the order:
# the firefox regex also matches the firefox-rc regex.
PRODUCT_TO_PRODUCT_ENTRY = [
    ('fennec', r'^Fennec-.*$'),
    ('firefox-rc', r'^Firefox-.*build[0-9]+-.*$'),
    ('firefox', r'^Firefox-.*$'),
    ('devedition', r'^Devedition-.*$'),
    ('thunderbird', r'^Thunderbird-.*$'),
]

BOUNCER_LOCATION_PLATFORMS = [
    'linux',
    'linux64',
    'osx',
    'win',
    'win64',
    'android-x86',
    'android',
    'win64-aarch64',
]

GO_BOUNCER_URL_TMPL = {
    'project:releng:bouncer:server:production':
        'https://download.mozilla.org/?product={}&print=yes',
    'project:comm:thunderbird:releng:bouncer:server:production':
        'https://download.mozilla.org/?product={}&print=yes',
    'project:releng:bouncer:server:staging':
        'https://bouncer-bouncer-releng.stage.mozaws.net/?product={}&print=yes',
    'project:comm:thunderbird:releng:bouncer:server:staging':
        'https://bouncer-bouncer-releng.stage.mozaws.net/?product={}&print=yes',
}

NIGHTLY_VERSION_REGEX = r'\d+\.0a1'
