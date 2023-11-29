Tiempo total: 7,5 horas

1.ASOCIAR BLOGS/NOTICIAS A UNA COMPAÑIA
Modulo: website_blog_company_dependent
Tiempo: 1,5 horas
Observaciones: He asumido la compañia del usuario es su compañia actual, en el caso de que se quisiese ver todos los registros vinculados
a las compañias asociadas la regla seria la siguiente "['|',('company_id','=',False),('company_id','child_of',user.company_ids.ids)]". No habia tocado nunca este modulo por lo que parte del tiempo lo he dedicado a buscar que tenia que
	instalar y como funcionaba.
	
	
2.NO PERMITIR PEDIDOS DE VENTA CON CANTIDADES A CERO
Modulo: sale_order_no_zero_lines
Tiempo: 1 horas
Observaciones: No he desarrllado los test, he trabajado de forma esporadica con ellos para la OCA pero trabajo de normal usandolos y no creo que pueda diseñarlos actualmente con la calidad
que me gustaría.


3.MODIFICACIONES DE FORMULARIO DE CONTACTOS DE OPORTUNIDADES
Modulo: crm_contact_source
Tiempo: 5 horas
Observaciones: No tenía muy claro que hacer en la comprobación del email y he optado por una pequeña comprobación por
javascript. He observado que existe un campo llamado origen en Seguimiento/Marketing, en un caso real lo hubiese comentado
anteriormente para ver la posibilidad de usar ese campo del core.

