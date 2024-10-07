# ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | ID of the associated Project Inspection Template Item | 
**type** | **str** | Project Inspection Template Item Reference Type | 
**payload** | [**ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload**](ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload.md) |  | 

## Example

```python
from procore_sdk.models.project_inspection_template_item_reference_create_body_item_template_reference import ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReference

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReference from a JSON string
project_inspection_template_item_reference_create_body_item_template_reference_instance = ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReference.from_json(json)
# print the JSON string representation of the object
print(ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReference.to_json())

# convert the object into a dict
project_inspection_template_item_reference_create_body_item_template_reference_dict = project_inspection_template_item_reference_create_body_item_template_reference_instance.to_dict()
# create an instance of ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReference from a dict
project_inspection_template_item_reference_create_body_item_template_reference_from_dict = ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReference.from_dict(project_inspection_template_item_reference_create_body_item_template_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


