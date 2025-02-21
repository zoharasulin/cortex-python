"""
Copyright 2023 Cognitive Scale, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from .client import Cortex
from .message import Message

from .__version__ import __title__, __description__, __url__, __version__
from .__version__ import __author__, __author_email__, __license__
from .__version__ import __copyright__

__all__ = ["__version__", "Cortex", "Message"]
