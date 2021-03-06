import sudo

from typing import Tuple
import pwd


class SudoGroupPlugin(sudo.Plugin):
    """Example sudo input/output plugin

    Demonstrates how to use the sudo group plugin API. Typing annotations are
    just here for the help on the syntax (requires python >= 3.5).

    On detailed description of the functions refer to sudo_plugin manual (man
    sudo_plugin).

    Most functions can express error or reject through their "int" return value
    as documented in the manual. The sudo module also has constants for these:
        sudo.RC_ACCEPT / sudo.RC_OK  1
        sudo.RC_REJECT               0
        sudo.RC_ERROR               -1
        sudo.RC_USAGE_ERROR         -2

    If the function returns "None" (for example does not call return), it will
    be considered sudo.RC_OK. If an exception is raised, its backtrace will be
    shown to the user and the plugin function returns sudo.RC_ERROR. If that is
    not acceptable, catch it.
    """

    # -- Plugin API functions --
    def query(self, user: str, group: str, user_pwd: Tuple):
        """Query if user is part of the specified group.

        Beware that user_pwd can be None if user is not present in the password
        database. Otherwise it is a tuple convertible to pwd.struct_passwd.
        """
        hardcoded_user_groups = {
            "testgroup": [ "testuser1", "testuser2" ],
            "mygroup": [ "test" ]
        }

        group_has_user = user in hardcoded_user_groups.get(group, [])
        return sudo.RC_ACCEPT if group_has_user else sudo.RC_REJECT
