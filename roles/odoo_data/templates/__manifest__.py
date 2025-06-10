{
    "name": "{{ item.display_name }}",
    "summary": """
        Generated module to configure {{ item.model }}.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Technical",
    "version": "1.0",
    "license": "AGPL-3",
    "depends": ["{{ item.depends | default('base') }}"],
    "data": [
        "data/{{ item.model }}.data.xml",
    ],
    "installable": True,
    "application": False,
}
