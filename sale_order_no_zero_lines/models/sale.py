from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        """Don't allow confirm sale order if it has zero quantity for products."""
        for order in self:
            if order.has_zero_lines():
                raise ValidationError(
                    _(
                        "Can't confirm draft order (%s) if has product quantities at 0"
                        % order.name
                    )
                )
        return super(SaleOrder, self).action_confirm()

    def has_zero_lines(self):
        """Check if the sale order has product lines with zero quantity."""
        self.ensure_one()
        return (
            len(
                self.order_line.filtered(
                    lambda x: not x.display_type and not x.product_uom_qty
                )
            )
            > 0
        )

    def action_delete_zero_quantity_lines(self):
        """Delete the sale order product lines with zero quantity."""
        self.ensure_one()
        self.order_line.filtered(
            lambda x: not x.display_type and not x.product_uom_qty
        ).unlink()
