from odoo import models,fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'


    processor = fields.Char(string='Computer Processor') 
    
'''
processor is the name of the field and Computer Processor is field label 
we inherited the features of product.template for our model and this is how it is done 
and the processor field will be displayed in odoo environment     
'''