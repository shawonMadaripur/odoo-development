project_directory/
    |
    |--module_a/
    |   |--controllers/
    |   |   |--__init__.py
    |   |   |--controller.py
    |   |
    |   |--data/
    |   |   |--data.xml
    |   |
    |   |--models/
    |   |   |--__init__.py
    |   |   |--model.py
    |   |
    |   |--security/
    |   |   |--ir.model.access.csv
    |   |
    |   |--views/
    |   |   |
    |   |   |--templates.xml
    |   |   |--views.xml
    |   |
    |   |--__init__.py
    |   |--__manifest__.py



# simple fields :
    - Boolean (True, False)
    - char & Text (string)
    - selection (list of string)
    - Float & Integer (Number)
    - Date & Datetime (dates)
    - Binary (To store file)
    - Html (formated Text)



#: Fields Attributes
    - String (field name displayed in the views)
    - invisible (True or False, dispalys the field or not in the views)
    - Readonly (True or False, if true then field can't be edited by user)
    - Required (True or False, if true then record can't be saved in database with an empty/null value
    - Default (set value on the field automatically during record creation)


#: demo/demo.xml
    - addining demo data

#: creating new group.
<odoo>
    <record id="estate_manager" model="res.groups">
        <fields name="name">Estate Manager</fields>
    </record>
</odoo>
--------------------> I can create new group for security.


#: Access Rights
    - id (external identifier for the access rule)
    - name (name of the access rule)
    - model_id:id (ID of the model that the access rule applies to.)
    - group_id:id (ID of the group that the access rule applies to)
    - perm_read (read permission for the access rule)
    - perm_write (write permission for access rule)
    - perm_create (create permission for the access rule)
    - perm_unlink (unlink permission for the access rule)



