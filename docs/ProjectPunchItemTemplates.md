# ProjectPunchItemTemplates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Punch Item Template ID | [optional] 
**active** | **bool** | Flag that denotes if the Punch Item Template is available for use | [optional] 
**company_punch_item_template_id** | **int** | Parent Punch Item Template ID | [optional] 
**name** | **str** | Name of the Punch Item Template | [optional] 
**project_id** | **int** | Project ID | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**punch_item_manager** | [**PunchItem6CreatedBy**](PunchItem6CreatedBy.md) |  | [optional] 
**final_approver** | [**PunchItem6CreatedBy**](PunchItem6CreatedBy.md) |  | [optional] 
**template_category** | [**TemplateCategory**](TemplateCategory.md) |  | [optional] 
**assignee** | [**PunchItem6CreatedBy**](PunchItem6CreatedBy.md) |  | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 

## Example

```python
from procore_sdk.models.project_punch_item_templates import ProjectPunchItemTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPunchItemTemplates from a JSON string
project_punch_item_templates_instance = ProjectPunchItemTemplates.from_json(json)
# print the JSON string representation of the object
print(ProjectPunchItemTemplates.to_json())

# convert the object into a dict
project_punch_item_templates_dict = project_punch_item_templates_instance.to_dict()
# create an instance of ProjectPunchItemTemplates from a dict
project_punch_item_templates_from_dict = ProjectPunchItemTemplates.from_dict(project_punch_item_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


