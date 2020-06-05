# =============================================================================
# Minet CrowdTangle Search
# =============================================================================
#
# Function related to post search.
#
from urllib.parse import quote

from minet.crowdtangle.utils import make_paginated_iterator
from minet.crowdtangle.formatters import format_post

URL_TEMPLATE = "https://api.crowdtangle.com/links?count=100&sortBy=%(sort_by)s&token=%(token)s&link=%(link)s"


def url_forge(**kwargs):
    base_url = URL_TEMPLATE % {
        "sort_by": kwargs["sort_by"],
        "token": kwargs["token"],
        "link": quote(kwargs["link"]),
    }

    if kwargs.get("start_date") is not None:
        base_url += "&startDate=%s" % kwargs["start_date"]

    if kwargs.get("end_date") is not None:
        base_url += "&endDate=%s" % kwargs["end_date"]

    if kwargs.get("platforms") is not None:
        base_url += "&platforms=%s" % ",".join(kwargs["platforms"])

    if kwargs.get("include_summary") is not None:
        base_url += "&includeSummary=%s" % kwargs["include_summary"]

    return base_url


crowdtangle_links = make_paginated_iterator(
    url_forge, item_key="posts", formatter=format_post
)
