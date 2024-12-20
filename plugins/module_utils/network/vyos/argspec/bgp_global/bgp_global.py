# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the
# cli_rm_builder.
#
# Manually editing this file is not advised.
#
# To update the argspec make the desired changes
# in the module docstring and re-run
# cli_rm_builder.
#
#############################################

"""
The arg spec for the vyos_bgp_global module
"""


class Bgp_globalArgs(object):  # pylint: disable=R0903
    """The arg spec for the vyos_bgp_global module"""

    argument_spec = {
        "config": {
            "type": "dict",
            "options": {
                "as_number": {"type": "int"},
                "aggregate_address": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "prefix": {"type": "str"},
                        "as_set": {"type": "bool"},
                        "summary_only": {"type": "bool"},
                    },
                },
                "maximum_paths": {
                    "type": "list",
                    "elements": "dict",
                    "options": {"path": {"type": "str"}, "count": {"type": "int"}},
                },
                "neighbor": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "address": {"type": "str"},
                        "advertisement_interval": {"type": "int"},
                        "allowas_in": {"type": "int"},
                        "as_override": {"type": "bool"},
                        "attribute_unchanged": {
                            "type": "dict",
                            "options": {
                                "as_path": {"type": "bool"},
                                "med": {"type": "bool"},
                                "next_hop": {"type": "bool"},
                            },
                        },
                        "capability": {
                            "type": "dict",
                            "options": {
                                "dynamic": {"type": "bool"},
                                "orf": {
                                    "type": "str",
                                    "choices": ["send", "receive"],
                                },
                            },
                        },
                        "default_originate": {"type": "str"},
                        "description": {"type": "str"},
                        "disable_capability_negotiation": {"type": "bool"},
                        "disable_connected_check": {"type": "bool"},
                        "disable_send_community": {
                            "type": "str",
                            "choices": ["extended", "standard"],
                        },
                        "distribute_list": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "action": {
                                    "type": "str",
                                    "choices": ["export", "import"],
                                },
                                "acl": {"type": "int"},
                            },
                        },
                        "ebgp_multihop": {"type": "int"},
                        "filter_list": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "action": {
                                    "type": "str",
                                    "choices": ["export", "import"],
                                },
                                "path_list": {"type": "str"},
                            },
                        },
                        "local_as": {"type": "int"},
                        "maximum_prefix": {"type": "int"},
                        "nexthop_self": {"type": "bool"},
                        "override_capability": {"type": "bool"},
                        "passive": {"type": "bool"},
                        "password": {"type": "str", "no_log": True},
                        "peer_group_name": {"type": "str"},
                        "peer_group": {"type": "bool"},
                        "port": {"type": "int"},
                        "prefix_list": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "action": {
                                    "type": "str",
                                    "choices": ["export", "import"],
                                },
                                "prefix_list": {"type": "str"},
                            },
                        },
                        "remote_as": {"type": "int"},
                        "remove_private_as": {"type": "bool"},
                        "route_map": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "action": {
                                    "type": "str",
                                    "choices": ["export", "import"],
                                },
                                "route_map": {"type": "str"},
                            },
                        },
                        "route_reflector_client": {"type": "bool"},
                        "route_server_client": {"type": "bool"},
                        "shutdown": {"type": "bool"},
                        "soft_reconfiguration": {"type": "bool"},
                        "strict_capability_match": {"type": "bool"},
                        "unsuppress_map": {"type": "str"},
                        "update_source": {"type": "str"},
                        "weight": {"type": "int"},
                        "ttl_security": {"type": "int"},
                        "timers": {
                            "type": "dict",
                            "options": {
                                "connect": {"type": "int"},
                                "holdtime": {"type": "int"},
                                "keepalive": {"type": "int"},
                            },
                        },
                    },
                },
                "network": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "address": {"type": "str"},
                        "backdoor": {"type": "bool"},
                        "route_map": {"type": "str"},
                    },
                },
                "redistribute": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "protocol": {
                            "type": "str",
                            "choices": [
                                "connected",
                                "kernel",
                                "ospf",
                                "rip",
                                "static",
                            ],
                        },
                        "route_map": {"type": "str"},
                        "metric": {"type": "int"},
                    },
                },
                "timers": {
                    "type": "dict",
                    "options": {
                        "keepalive": {"type": "int"},
                        "holdtime": {"type": "int"},
                    },
                },
                "bgp_params": {
                    "type": "dict",
                    "options": {
                        "always_compare_med": {"type": "bool"},
                        "bestpath": {
                            "type": "dict",
                            "options": {
                                "as_path": {
                                    "type": "str",
                                    "choices": ["confed", "ignore"],
                                },
                                "compare_routerid": {"type": "bool"},
                                "med": {
                                    "type": "str",
                                    "choices": ["confed", "missing-as-worst"],
                                },
                            },
                        },
                        "cluster_id": {"type": "str"},
                        "confederation": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "identifier": {"type": "int"},
                                "peers": {"type": "int"},
                            },
                        },
                        "dampening": {
                            "type": "dict",
                            "options": {
                                "half_life": {"type": "int"},
                                "max_suppress_time": {"type": "int"},
                                "re_use": {"type": "int"},
                                "start_suppress_time": {"type": "int"},
                            },
                        },
                        "default": {
                            "type": "dict",
                            "options": {
                                "local_pref": {"type": "int"},
                                "no_ipv4_unicast": {"type": "bool"},
                            },
                        },
                        "deterministic_med": {"type": "bool"},
                        "disable_network_import_check": {"type": "bool"},
                        "distance": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "type": {
                                    "type": "str",
                                    "choices": ["external", "internal", "local"],
                                },
                                "value": {"type": "int"},
                                "prefix": {"type": "int"},
                            },
                        },
                        "enforce_first_as": {"type": "bool"},
                        "graceful_restart": {"type": "int"},
                        "log_neighbor_changes": {"type": "bool"},
                        "no_client_to_client_reflection": {"type": "bool"},
                        "no_fast_external_failover": {"type": "bool"},
                        "router_id": {"type": "str"},
                        "scan_time": {"type": "int"},
                    },
                },
            },
        },
        "state": {
            "type": "str",
            "choices": [
                "deleted",
                "merged",
                "purged",
                "replaced",
                "gathered",
                "rendered",
                "parsed",
            ],
            "default": "merged",
        },
        "running_config": {"type": "str"},
    }  # pylint: disable=C0301
