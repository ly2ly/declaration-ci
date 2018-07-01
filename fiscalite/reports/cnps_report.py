# -*- coding: utf-8 -*-
#from os import path2 as path
from openerp.osv import  osv 
from openerp import models, fields, api, _
from datetime import datetime
from lxml import etree
from cStringIO import StringIO
from openerp.exceptions import except_orm, Warning, RedirectWarning
import openpyxl, os.path, xlwt, time, calendar, base64, logging, openerp.addons.decimal_precision as dp
from openpyxl import load_workbook
from openpyxl import workbook



class declaration_cnps(osv.osv):
    _name="declaration.cnps"
    _inherit="declaration.cnps"


    def cnps_report_xls(self, cr, uid, ids, context=None): # fonction report cnps

       # p=os.path.dirname(os.path.realpath(_file_))
        #raise osv.except_osv(_("Error!"),_(p))
        #return False
        fl = StringIO()
        if context is None :
                context={}
        wbk = openpyxl.load_workbook('C:\\local_GIT\\ap_testing\\fiscalite\\templates\\cnps_template.xlsx')
        wks = wbk.active
        #wks['05'] = 22 
        #wbk.save('C:\\local_GIT\\cnps_template1.xlsx')
        wbk.save(fl)
        fl.seek(0)
        buf=base64.encodestring(fl.read())
        ctx=dict(context)
        ctx.update({'file':buf})
        if context is None:
            context={}
        data = {}
        res= self.read(cr, uid, ids, [], context=context)
        res=  res and res[0] or {}
        data['form'] = res
        try:
                form_id= self.pool.get('ir.model.data').get_object_reference(cr, uid, 'cnps_report_xls','cnps_form')[1]
        except ValueError:
                form_id=False
        return{
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'cnps.report.file',
            'views':[(form_id, 'form')],
            'view_id':form_id,
            'target':'new',
            'context':ctx,
        }

       



        