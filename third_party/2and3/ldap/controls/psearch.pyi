from typing import Any, Optional

from ldap.controls import RequestControl, ResponseControl
from pyasn1.type import univ

CHANGE_TYPES_INT: Any
CHANGE_TYPES_STR: Any

class PersistentSearchControl(RequestControl):
    class PersistentSearchControlValue(univ.Sequence):
        componentType: Any = ...
    controlType: str = ...
    changeTypes: Any = ...
    def __init__(
        self, criticality: bool = ..., changeTypes: Optional[Any] = ..., changesOnly: bool = ..., returnECs: bool = ...
    ) -> None: ...
    def encodeControlValue(self): ...

class ChangeType(univ.Enumerated):
    namedValues: Any = ...
    subtypeSpec: Any = ...

class EntryChangeNotificationValue(univ.Sequence):
    componentType: Any = ...

class EntryChangeNotificationControl(ResponseControl):
    controlType: str = ...
    changeType: Any = ...
    previousDN: Any = ...
    changeNumber: Any = ...
    def decodeControlValue(self, encodedControlValue: Any): ...
