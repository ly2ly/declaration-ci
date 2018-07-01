from openerp.osv import  osv 
from openerp import models, fields, api, _
from datetime import datetime
from lxml import etree
from cStringIO import StringIO
from openerp.exceptions import except_orm, Warning, RedirectWarning
import xlwt, time, calendar, base64, logging, openerp.addons.decimal_precision as dp



class declaration_tva(osv.osv):
    _name="declaration.tva"
    _inherit="declaration.tva"

    def tva_report_xls(self, cr, uid, ids, context=None): # fonction report tva
        fl = StringIO()
        if context is None :
                context={}
        wbk=xlwt.Workbook()
        sheet=wbk.add_sheet('New_ sheeT', cell_overwrite_ok=True)
        font=xlwt.Font()
        font.bold=True
        borders=xlwt.Borders()
        bold_style=xlwt.XFStyle()
        bold_style.font=fontstyle=xlwt.easyxf('align:wrap no')
        new_style7=xlwt.easyxf('font:height 210;font:name Calibri;align:wrap no')
        borders.bottom=xlwt.Borders.THICK
        sheet.col(1).width=500*12
        sheet.row(5).height=70*5
        sheet.write(2,2,'Spellbound soft solution',new_style7)
        sheet.write(3,2,'Odoo ERP',new_style7)
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
                form_id= self.pool.get('ir.model.data').get_object_reference(cr, uid, 'tva_report_xls','tva_form')[1]
        except ValueError:
                form_id=False
        return{
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'tva.report.file',
            'views':[(form_id, 'form')],
            'view_id':form_id,
            'target':'new',
            'context':ctx,
        }