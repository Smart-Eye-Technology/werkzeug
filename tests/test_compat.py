# -*- coding: utf-8 -*-
"""
    tests.compat
    ~~~~~~~~~~~~

    Ensure that old stuff does not break on update.

    :copyright: (c) 2014 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
import warnings

from werkzeug.wrappers import Response
from werkzeug.test import create_environ


def test_old_imports():
    from werkzeug.utils import Headers, MultiDict, CombinedMultiDict, \
         Headers, EnvironHeaders
    from werkzeug.http import Accept, MIMEAccept, CharsetAccept, \
         LanguageAccept, ETags, HeaderSet, WWWAuthenticate, \
         Authorization

def test_exposed_werkzeug_mod():
    import werkzeug
    assert _expected_all == set(werkzeug.__all__)
    for key in _expected_all:
        getattr(werkzeug, key)


_expected_all = frozenset((
    'OrderedMultiDict', 'ImmutableOrderedMultiDict', 'ETagResponseMixin',
    'http_date', 'create_environ', 'redirect', 'ETagRequestMixin',
    'quote_etag', 'BaseResponse', 'FileStorage', 'UserAgentMixin',
    'parse_options_header', 'make_line_iter', 'url_unquote_plus',
    'HTTP_STATUS_CODES', 'get_host', 'FileWrapper', 'Headers', 'FileMultiDict',
    'uri_to_iri', 'url_encode', 'ImmutableTypeConversionDict',
    'is_hop_by_hop_header', 'ResponseStreamMixin',
    'parse_authorization_header', 'parse_date', 'Aborter', 'CharsetAccept',
    'ResponseCacheControl', 'url_quote', 'ImmutableList', 'is_entity_header',
    'LocalStack', 'EnvironHeaders', 'run_wsgi_app', 'WWWAuthenticate',
    'SharedDataMiddleware', 'check_password_hash', 'EnvironBuilder',
    'BaseRequest', 'parse_form_data', 'wrap_file', 'import_string',
    'HeaderSet', 'ETags', 'dump_options_header', 'url_decode',
    'header_property', 'pop_path_info', 'MultiDict', 'find_modules',
    'CommonRequestDescriptorsMixin', 'RequestCacheControl', 'ImmutableDict',
    'generate_etag', 'Local', 'Authorization', 'unquote_header_value',
    'unquote_etag', 'generate_password_hash', 'AuthorizationMixin',
    'bind_arguments', 'environ_property', 'ImmutableMultiDict',
    'append_slash_redirect', 'MIMEAccept', 'validate_arguments',
    'get_current_url', 'parse_etags', 'CombinedMultiDict', 'LimitedStream',
    'parse_www_authenticate_header', 'cached_property', 'run_simple',
    'parse_cache_control_header', 'ClosingIterator', 'Client', 'unescape',
    'iri_to_uri', 'remove_entity_headers', 'url_quote_plus', 'dump_cookie',
    'Response', 'DebuggedApplication', 'release_local', 'Href',
    'quote_header_value', 'remove_hop_by_hop_headers', 'test_app', 'escape',
    'LocalProxy', 'abort', 'dump_header', 'secure_filename',
    'CommonResponseDescriptorsMixin', 'peek_path_info', 'parse_dict_header',
    'format_string', 'HTMLBuilder', 'cookie_date', 'html',
    'WWWAuthenticateMixin', 'UserAgent', 'xhtml', 'extract_path_info',
    'parse_accept_header', 'Request', 'LanguageAccept', 'LocalManager',
    'DispatcherMiddleware', 'ArgumentValidationError', 'url_unquote',
    'AcceptMixin', '_easteregg', 'url_fix', 'responder', 'Accept',
    'parse_list_header', 'TypeConversionDict', 'is_resource_modified',
    'CallbackDict', 'parse_set_header', 'parse_cookie', 'exceptions',
    'routing', 'script'
))
