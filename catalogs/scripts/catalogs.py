#!/usr/bin/python


import os
import plistlib
import sys

sys.path.append('/usr/local/munki')
import munkilib.updatecheck.manifestutils
sys.path.append('/usr/local/sal')
import utils


def main():
    client_manifest_path = munkilib.updatecheck.manifestutils.get_primary_manifest()
    if os.path.exists(client_manifest_path):
        client_manifest = plistlib.readPlist(client_manifest_path)
    else:
        client_manifest = {}

    # Drop any blank entries and trim WS.
    catalogs = [c.strip() for c in client_manifest.get("catalogs", []) if c]
    if not catalogs:
        catalogs = ["NO CATALOGS"]
    utils.add_plugin_results('Catalogs', {"Catalogs": "+".join(catalogs)})


if __name__ == "__main__":
    main()