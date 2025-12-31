from odoo import models

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def write(self, vals):
        res = super().write(vals)

        if 'user_id' in vals or 'team_id' in vals:
            for lead in self:
                user_id = lead.user_id.id
                team_id = lead.team_id.id

                # 🔥 Update ALL related Sale Orders
                sale_orders = lead.order_ids.filtered(
                    lambda o: o.state != 'cancel'
                )

                if sale_orders:
                    sale_orders.write({
                        'user_id': user_id,
                        'team_id': team_id,
                    })

                    # 🔥 Update invoices too (important for dashboards)
                    invoices = sale_orders.mapped('invoice_ids')
                    if invoices:
                        invoices.write({
                            'invoice_user_id': user_id,
                            'team_id': team_id,
                        })

        return res
