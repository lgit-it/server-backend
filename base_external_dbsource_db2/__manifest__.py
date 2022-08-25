# Copyright <2011> <Daniel Reis, Maxime Chambreuil, Savoir-faire Linux>
# Copyright 2016 LasLabs Inc.
# Copyright 2021 Luigi Gregori Information Technology srls
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    'name': 'External Database Source - DB2',
    'version': '14.0.1.0.1',
    'category': 'Tools',
    'author': "Luigi Gregori Information Technology, "
              "Daniel Reis, "
              "LasLabs, "
              "Odoo Community Association (OCA)",
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'base_external_dbsource_sqlite',
    ],
    'external_dependencies': {
        'python': [
            'sqlalchemy',
            'ibm_db',
        ],
    },
    'demo': [
        'demo/base_external_dbsource.xml',
    ],
    'installable': True,
}
