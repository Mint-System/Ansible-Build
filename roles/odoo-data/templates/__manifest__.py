{
    'name': "{{ item.display_name }} Data",

    'summary': """
        Generated module to configure {{ item.model }}.
    """,
    
    'author': 'Mint System GmbH, Odoo Community Association (OCA)',
    'website': 'https://www.mint-system.ch',
    'category': 'Technical',
    'version': '14.0.1.0.0',
    'license': 'AGPL-3',
    
    'depends': ['{{ depends }}'],

    'data': [
        'data/{{ item.model }}.data.xml',
    ],

    'installable': True,
    'application': False,
}
