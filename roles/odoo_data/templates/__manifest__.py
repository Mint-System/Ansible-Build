{
    "name": "{{ item.display_name }}",
    "summary": """
        Generated module with data for {{ item.model }}.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Technical",
    "version": "{{ item.version }}",
    "license": "AGPL-3",
    "depends": ["{{ item.depends | default('base') }}"],
    "data": [
        "data/{{ item.model }}.data.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
