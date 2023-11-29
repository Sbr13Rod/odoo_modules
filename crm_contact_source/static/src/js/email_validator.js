odoo.define('crm_contact_source.contactus', function(require) {
    "use strict";

    require('web.dom_ready');

    $("#form_contactus input[name='email_from']").change(function(){

        var email = $("input[name='email_from']").val()
        var len = email.split("@").length

        if (len != 2) {
            $("input[name='email_from']").val("")
            $("#div_change").show()
        }else{
            $("#div_change").hide()
        }
    });
});
