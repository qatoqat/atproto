##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2023 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


from dataclasses import dataclass
from typing import List, Optional

from xrpc_client import models
from xrpc_client.models import base


@dataclass
class Params(base.ParamsModelBase):

    """Parameters model for :obj:`com.atproto.admin.getModerationReports`.

    Attributes:
        subject: Subject.
        resolved: Resolved.
        limit: Limit.
        cursor: Cursor.
    """

    cursor: Optional[str] = None
    limit: Optional[int] = None
    resolved: Optional[bool] = None
    subject: Optional[str] = None


@dataclass
class Response(base.ResponseModelBase):

    """Output data model for :obj:`com.atproto.admin.getModerationReports`.

    Attributes:
        cursor: Cursor.
        reports: Reports.
    """

    reports: List['models.ComAtprotoAdminDefs.ReportView']
    cursor: Optional[str] = None