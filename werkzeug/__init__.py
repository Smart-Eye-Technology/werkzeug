# -*- coding: utf-8 -*-
"""
    werkzeug
    ~~~~~~~~

    Werkzeug is the Swiss Army knife of Python web development.

    It provides useful classes and functions for any WSGI application to make
    the life of a python web developer much easier.  All of the provided
    classes are independent from each other so you can mix it with any other
    library.


    :copyright: (c) 2014 by the Werkzeug Team, see AUTHORS for more details.
    :license: BSD, see LICENSE for more details.
"""

# the version.  Usually set automatically by a script.
__version__ = '0.10-dev'

from . import exceptions, routing, script

from .serving import run_simple

from .testapp import test_app

from .useragents import UserAgent

from ._internal import _easteregg

from .debug import DebuggedApplication

from .datastructures import Accept, Authorization, CallbackDict, CharsetAccept, \
    CombinedMultiDict, ETags, EnvironHeaders, FileMultiDict, FileStorage, \
    HeaderSet, Headers, ImmutableDict, ImmutableList, ImmutableMultiDict, \
    ImmutableOrderedMultiDict, ImmutableTypeConversionDict, LanguageAccept, \
    MIMEAccept, MultiDict, OrderedMultiDict, RequestCacheControl, \
    ResponseCacheControl, TypeConversionDict, WWWAuthenticate

from .utils import ArgumentValidationError, HTMLBuilder, append_slash_redirect, \
    bind_arguments, cached_property, dump_cookie, environ_property, escape, \
    find_modules, format_string, header_property, html, import_string, \
    parse_cookie, redirect, secure_filename, unescape, validate_arguments, \
    xhtml

from .wrappers import AcceptMixin, AuthorizationMixin, BaseRequest, \
    BaseResponse, CommonRequestDescriptorsMixin, \
    CommonResponseDescriptorsMixin, ETagRequestMixin, ETagResponseMixin, \
    Request, Response, ResponseStreamMixin, UserAgentMixin, \
    WWWAuthenticateMixin

from .local import Local, LocalManager, LocalProxy, LocalStack, release_local

from .security import check_password_hash, generate_password_hash

from .test import Client, EnvironBuilder, create_environ, run_wsgi_app

from .wsgi import ClosingIterator, DispatcherMiddleware, FileWrapper, \
    LimitedStream, SharedDataMiddleware, extract_path_info, get_current_url, \
    get_host, make_line_iter, peek_path_info, pop_path_info, responder, \
    wrap_file

from .http import HTTP_STATUS_CODES, cookie_date, dump_header, \
    dump_options_header, generate_etag, http_date, is_entity_header, \
    is_hop_by_hop_header, is_resource_modified, parse_accept_header, \
    parse_authorization_header, parse_cache_control_header, parse_date, \
    parse_dict_header, parse_etags, parse_list_header, parse_options_header, \
    parse_set_header, parse_www_authenticate_header, quote_etag, \
    quote_header_value, remove_entity_headers, remove_hop_by_hop_headers, \
    unquote_etag, unquote_header_value

from .urls import Href, iri_to_uri, uri_to_iri, url_decode, url_encode, \
    url_fix, url_quote, url_quote_plus, url_unquote, url_unquote_plus

from .formparser import parse_form_data

from .exceptions import Aborter, abort

def _get_all():
    for name, obj in globals().items():
        if name.startswith('_') and name != '_easteregg':
            continue
        if not hasattr(obj, '__module__') and \
           name not in ('exceptions', 'routing', 'script',
                        'HTTP_STATUS_CODES'):
            # Exclude most modules. HTTP_STATUS_CODES is also in here because
            # it is mistakenly identified as a module.
            continue
        yield name

__all__ = tuple(_get_all())
