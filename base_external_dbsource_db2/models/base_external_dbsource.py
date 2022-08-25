# Copyright 2011 Daniel Reis
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)

try:
    from odoo.addons.base_external_dbsource.models import (
        base_external_dbsource,
    )
    CONNECTORS = base_external_dbsource.BaseExternalDbsource.CONNECTORS
    try:
        import ibm_db
        import ibm_db_sa
        CONNECTORS.append(('db2', 'IBM DB2'))
        assert ibm_db
    except (ImportError, AssertionError):
        _logger.info('Ibm Db2 Server not available. Please install "ibm_db" and "ibm_db_sa" '
                     'python packages.')
except ImportError:
    _logger.info('base_external_dbsource Odoo module not found.')


class BaseExternalDbsource(models.Model):
    """ It provides logic for connection to a DB2 data source. """

    _inherit = "base.external.dbsource"

    #PWD_STRING_DB2 = 'Password=%s;'
    PWD_STRING_DB2 = '%s'

    @api.multi
    def connection_close_db2(self, connection):
        return connection.close()

    @api.multi
    def connection_open_db2(self):
        return self._connection_open_sqlalchemy()

    @api.multi
    def connection_test_db2(self):
        return self._connection_test_sqlalchemy()



    @api.multi
    def execute_db2(self, sqlquery, sqlparams, metadata):
        return self._execute_sqlalchemy(sqlquery, sqlparams, metadata)
