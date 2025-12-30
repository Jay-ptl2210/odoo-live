from odoo import models

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def write(self, vals):
        res = super().write(vals)

        # Lead transfer thaye tyare
        if 'user_id' in vals:
            for lead in self:
                # Related Quotations pan transfer
                if lead.order_ids:
                    lead.order_ids.filtered(
                        lambda o: o.state in ('draft', 'sent')
                    ).write({
                        'user_id': lead.user_id.id,
                        'team_id': lead.team_id.id,
                    })
        return res
