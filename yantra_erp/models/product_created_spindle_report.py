from odoo import models, fields
from odoo.fields import Datetime
from datetime import timedelta

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_send_today_spindle_report(self):
        today = fields.Date.today()

        start = Datetime.to_datetime(today)
        end = start + timedelta(days=1)

        Product = self.env['product.template']

        domain = [
            ('create_date', '>=', start),
            ('create_date', '<', end),
            ('spindle_type_id', '!=', False),
        ]

        total_products = Product.search_count(domain)

        grouped_data = Product.read_group(
            domain,
            ['spindle_type_id'],
            ['spindle_type_id']
        )

        if grouped_data:
            summary_html = ""
            for rec in grouped_data:
                spindle_name = rec['spindle_type_id'][1]
                count = rec['spindle_type_id_count']
                summary_html += f"<li>{spindle_name} : {count}</li>"
        else:
            summary_html = "<li>No Spindle Type products created today</li>"

        body = f"""
        <h2>📦 Daily Product Creation Report – {today}</h2>

        <p><b>Total Products Added Today :</b> {total_products}</p>

        <h3>Spindle Type Wise Count</h3>
        <ul>
            {summary_html}
        </ul>

        <br/>
        <i>Triggered manually from Product screen</i>
        """

        self.env['mail.mail'].create({
            'subject': f'Daily Product Created Summary – {today}',
            'body_html': body,
            'email_to': 'jaydptl.22@gmail.com',
        }).send()

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Report Sent',
                'message': 'Daily Product Created Report has been sent successfully.',
                'type': 'success',
                'sticky': False,
            }
        }
